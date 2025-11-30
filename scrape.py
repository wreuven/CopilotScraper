import os
import time
import json
from collections import deque
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup, Tag

BASE = "https://code.visualstudio.com"
START_URL = BASE + "/docs/copilot/overview"
OUT_JSONL = "copilot_docs.jsonl"

REQUEST_DELAY = 0.5  # be polite

session = requests.Session()
session.headers.update({
    "User-Agent": "CopilotDocsAI-Scraper/1.0 (+personal use)"
})


def is_in_scope(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https", ""):
        return False
    if parsed.netloc and parsed.netloc != "code.visualstudio.com":
        return False
    path = parsed.path or ""
    return path.startswith("/docs/copilot")


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    parsed = parsed._replace(fragment="")  # drop fragment
    return parsed.geturl()


def get_main_content(soup: BeautifulSoup) -> Tag:
    # VS Code docs use <main>; fallback to body if needed
    main = soup.find("main")
    if not main:
        main = soup.find("article") or soup.body or soup
    return main


def extract_table_as_markdown(table: Tag) -> str:
    """Convert HTML table to markdown format."""
    lines = []

    # Extract headers
    headers = []
    header_row = table.find('thead')
    if header_row:
        for th in header_row.find_all(['th', 'td']):
            headers.append(th.get_text(strip=True))

    # If no thead, try first tr
    if not headers:
        first_row = table.find('tr')
        if first_row:
            for th in first_row.find_all(['th', 'td']):
                headers.append(th.get_text(strip=True))

    if headers:
        lines.append('| ' + ' | '.join(headers) + ' |')
        lines.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')

    # Extract body rows
    tbody = table.find('tbody') or table
    for tr in tbody.find_all('tr'):
        # Skip if this is the header row we already processed
        if headers and tr == table.find('tr'):
            continue

        cells = []
        for td in tr.find_all(['td', 'th']):
            # Clean cell text and handle multiline
            cell_text = td.get_text(' ', strip=True).replace('\n', ' ')
            cells.append(cell_text)

        if cells:
            lines.append('| ' + ' | '.join(cells) + ' |')

    return '\n'.join(lines)


def extract_sections(soup: BeautifulSoup):
    """
    Split main content into sections based on h2/h3.
    Returns a list of dicts: {heading, anchor, text, code_blocks}
    """
    main = get_main_content(soup)
    sections = []
    current = {
        "heading": None,
        "anchor": None,
        "text_parts": [],
        "code_blocks": [],
        "tables": []
    }

    def flush_current():
        if not current["heading"] and not "".join(current["text_parts"]).strip():
            return
        text = "\n".join(p.strip() for p in current["text_parts"] if p.strip())

        # Append tables to text
        if current["tables"]:
            text += "\n\n" + "\n\n".join(current["tables"])

        sections.append({
            "heading": current["heading"],
            "anchor": current["anchor"],
            "text": text,
            "code_blocks": current["code_blocks"][:],
        })

    for el in main.descendants:
        if not isinstance(el, Tag):
            continue

        # New section on h2 / h3
        if el.name in ("h2", "h3"):
            # close previous
            flush_current()
            current["heading"] = el.get_text(" ", strip=True)
            current["anchor"] = el.get("id")
            current["text_parts"] = []
            current["code_blocks"] = []
            current["tables"] = []
            continue

        # Paragraph-like text
        if el.name in ("p", "li"):
            txt = el.get_text(" ", strip=True)
            if txt:
                current["text_parts"].append(txt)

        # Tables
        if el.name == "table":
            table_md = extract_table_as_markdown(el)
            if table_md:
                current["tables"].append(table_md)

        # Code blocks
        if el.name == "pre":
            code_text = el.get_text("\n", strip=True)
            if code_text:
                # Try to guess language from <code class="language-xyz">
                code_el = el.find("code")
                lang = None
                if code_el and code_el.has_attr("class"):
                    for c in code_el["class"]:
                        if c.startswith("language-"):
                            lang = c.replace("language-", "")
                            break
                if lang:
                    fenced = f"```{lang}\n{code_text}\n```"
                else:
                    fenced = f"```\n{code_text}\n```"
                current["code_blocks"].append(fenced)

    # flush last section
    flush_current()
    return sections


def chunk_text(text: str, max_chars: int = 1200):
    """
    Simple character-based chunking by paragraphs, to keep chunks reasonably sized.
    """
    if len(text) <= max_chars:
        return [text]

    paras = [p for p in text.split("\n") if p.strip()]
    chunks = []
    buf = []

    for p in paras:
        candidate = ("\n".join(buf + [p])).strip()
        if len(candidate) > max_chars and buf:
            chunks.append("\n".join(buf).strip())
            buf = [p]
        else:
            buf.append(p)

    if buf:
        chunks.append("\n".join(buf).strip())

    return chunks


def scrape():
    visited = set()
    queue = deque([START_URL])

    # open once; append as we go
    with open(OUT_JSONL, "w", encoding="utf-8") as out_f:
        while queue:
            url = queue.popleft()
            url = normalize_url(url)
            if url in visited:
                continue
            visited.add(url)

            if not is_in_scope(url):
                continue

            parsed = urlparse(url)
            path = parsed.path
            print(f"\nFetching {url}")

            try:
                resp = session.get(url, timeout=20)
                resp.raise_for_status()
            except requests.RequestException as e:
                print(f"  ERROR: {e}")
                continue

            html = resp.text
            soup = BeautifulSoup(html, "html.parser")

            # Document title (usually h1)
            h1 = soup.find("h1")
            doc_title = h1.get_text(" ", strip=True) if h1 else None

            # Extract sections
            sections = extract_sections(soup)
            if not sections:
                # fallback: whole main as one section
                main = get_main_content(soup)
                text = main.get_text("\n", strip=True)
                sections = [{
                    "heading": None,
                    "anchor": None,
                    "text": text,
                    "code_blocks": [],
                }]

            # Write JSONL chunks
            for s_idx, sec in enumerate(sections):
                base_chunk_id = (path.strip("/") or "root")
                if sec["anchor"]:
                    base_chunk_id += f"#{sec['anchor']}"
                else:
                    base_chunk_id += f"#section-{s_idx}"

                chunks = chunk_text(sec["text"], max_chars=1200)

                for c_idx, chunk_text_part in enumerate(chunks):
                    rec = {
                        "url": url,
                        "path": path,
                        "doc_title": doc_title,
                        "section_heading": sec["heading"],
                        "anchor": sec["anchor"],
                        "chunk_id": f"{base_chunk_id}-{c_idx}",
                        "content": chunk_text_part,
                        "code_blocks": sec["code_blocks"],
                        "source": "vscode-copilot-docs",
                    }
                    out_f.write(json.dumps(rec, ensure_ascii=False) + "\n")

            # Enqueue new links
            for a in soup.find_all("a", href=True):
                href = a["href"]
                next_url = urljoin(url, href)
                if is_in_scope(next_url):
                    n = normalize_url(next_url)
                    if n not in visited:
                        queue.append(n)

            time.sleep(REQUEST_DELAY)


if __name__ == "__main__":
    scrape()
    print(f"\nDone. Wrote chunks to {OUT_JSONL}")

