import os
import time
import json
from collections import deque
from urllib.parse import urljoin, urlparse
from pathlib import Path

import requests
from bs4 import BeautifulSoup, Tag

BASE = "https://code.visualstudio.com"
START_URL = BASE + "/docs/copilot/overview"
OUT_JSONL = "copilot_docs_with_images.jsonl"
IMAGES_DIR = "images"

REQUEST_DELAY = 0.5  # be polite

session = requests.Session()
session.headers.update({
    "User-Agent": "CopilotDocsAI-Scraper/2.0 (+personal use)"
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


def is_content_image(img_src: str) -> bool:
    """
    Filter to identify content images (screenshots, diagrams) vs UI icons.
    Content images are typically in /assets/docs/ path.
    """
    if not img_src:
        return False

    # Exclude UI icons and theme images
    exclude_patterns = [
        "/assets/icons/",
        "theme-icon",
        "search-icon",
        ".svg"  # Most SVGs are icons, not content
    ]

    for pattern in exclude_patterns:
        if pattern in img_src:
            return False

    # Include documentation images
    include_patterns = [
        "/assets/docs/copilot/",
        ".png",
        ".jpg",
        ".jpeg",
        ".gif"
    ]

    return any(pattern in img_src for pattern in include_patterns)


def download_image(img_url: str, save_path: str) -> bool:
    """Download an image and save it locally."""
    try:
        resp = session.get(img_url, timeout=20, stream=True)
        resp.raise_for_status()

        # Create directory if needed
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with open(save_path, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)

        return True
    except Exception as e:
        print(f"  Failed to download {img_url}: {e}")
        return False


def extract_images(soup: BeautifulSoup, page_url: str, page_path: str) -> list:
    """
    Extract all content images from the page.
    Returns list of dicts with image metadata.
    """
    images = []
    main = soup.find("main") or soup.find("article") or soup.body or soup

    for img in main.find_all("img"):
        img_src = img.get("src", "")
        if not img_src:
            continue

        # Make absolute URL
        img_url = urljoin(page_url, img_src)

        # Filter content images only
        if not is_content_image(img_url):
            continue

        # Get image metadata
        alt_text = img.get("alt", "")

        # Find surrounding context (heading or paragraph)
        context = ""
        parent = img.find_parent(["figure", "p", "div"])
        if parent:
            # Look for nearby heading
            heading = parent.find_previous(["h1", "h2", "h3", "h4"])
            if heading:
                context = heading.get_text(" ", strip=True)

        # Find caption (often in <figcaption> or next <p>)
        caption = ""
        figure = img.find_parent("figure")
        if figure:
            figcaption = figure.find("figcaption")
            if figcaption:
                caption = figcaption.get_text(" ", strip=True)

        # Create local filename based on URL path
        parsed_img = urlparse(img_url)
        # e.g., /assets/docs/copilot/overview/image.png -> copilot/overview/image.png
        local_path_parts = Path(parsed_img.path).parts

        # Find 'copilot' in path and take everything after it
        if 'copilot' in local_path_parts:
            copilot_idx = local_path_parts.index('copilot')
            relative_path = Path(*local_path_parts[copilot_idx:])
        else:
            # Fallback: use last few parts
            relative_path = Path(*local_path_parts[-3:])

        local_path = os.path.join(IMAGES_DIR, str(relative_path))

        # Download image
        print(f"  Downloading image: {img_url}")
        success = download_image(img_url, local_path)

        if success:
            images.append({
                "url": img_url,
                "local_path": local_path,
                "alt_text": alt_text,
                "caption": caption,
                "context": context,
            })
            time.sleep(0.2)  # Small delay between image downloads

    return images


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
    Returns a list of dicts: {heading, anchor, text, code_blocks, images, tables}
    """
    main = get_main_content(soup)
    sections = []
    current = {
        "heading": None,
        "anchor": None,
        "text_parts": [],
        "code_blocks": [],
        "images": [],
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
            "images": current["images"][:],
        })

    # Track current section's starting element for image association
    current_section_start = None

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
            current["images"] = []
            current["tables"] = []
            current_section_start = el
            continue

        # Paragraph-like text
        if el.name in ("p", "li"):
            txt = el.get_text(" ", strip=True)
            if txt:
                current["text_parts"].append(txt)

        # Tables
        if el.name == "table":
            # Skip if already processed (nested tables)
            if not any(el in processed_el for processed_el in [el]):
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

        # Images - associate with current section
        if el.name == "img":
            img_src = el.get("src", "")
            if img_src and is_content_image(img_src):
                # We'll process images separately at the page level
                # but note their presence in this section
                pass

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

    # Create images directory
    os.makedirs(IMAGES_DIR, exist_ok=True)

    stats = {
        "pages": 0,
        "chunks": 0,
        "images": 0,
    }

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

            # Extract images first (downloads them)
            page_images = extract_images(soup, url, path)
            stats["images"] += len(page_images)

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
                    "images": [],
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
                        "images": page_images,  # All images from page
                        "source": "vscode-copilot-docs",
                    }
                    out_f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    stats["chunks"] += 1

            stats["pages"] += 1

            # Enqueue new links
            for a in soup.find_all("a", href=True):
                href = a["href"]
                next_url = urljoin(url, href)
                if is_in_scope(next_url):
                    n = normalize_url(next_url)
                    if n not in visited:
                        queue.append(n)

            time.sleep(REQUEST_DELAY)

    print(f"\n{'='*60}")
    print(f"Scraping complete!")
    print(f"{'='*60}")
    print(f"Pages scraped: {stats['pages']}")
    print(f"Chunks created: {stats['chunks']}")
    print(f"Images downloaded: {stats['images']}")
    print(f"Output: {OUT_JSONL}")
    print(f"Images directory: {IMAGES_DIR}/")
    print(f"{'='*60}")


if __name__ == "__main__":
    scrape()
