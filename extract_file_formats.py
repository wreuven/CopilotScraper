"""
Extract and document special Copilot file formats from scraped documentation.
"""

import json
import re
from collections import defaultdict

JSONL_FILE = "copilot_docs_with_images.jsonl"
OUTPUT = "copilot_file_formats.md"

# File formats to extract
FILE_FORMATS = {
    ".agent.md": "Custom agent definitions",
    ".chatmode.md": "Legacy custom chat modes (deprecated)",
    ".instructions.md": "Workspace instruction files",
    ".prompt.md": "Reusable prompt templates",
    ".plan.md": "Planning documents",
    ".copilotignore": "Files to exclude from Copilot context",
    "copilot-instructions.md": "Workspace-level instructions",
}

def extract_file_format_info():
    """Extract documentation and examples for each file format."""

    format_data = defaultdict(lambda: {
        "description": "",
        "sections": [],
        "code_examples": [],
        "urls": set(),
    })

    with open(JSONL_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                chunk = json.loads(line)
                content = chunk.get('content', '')
                code_blocks = chunk.get('code_blocks', [])
                url = chunk.get('url', '')
                section = chunk.get('section_heading', '')

                # Check for mentions of file formats
                for fmt, desc in FILE_FORMATS.items():
                    pattern = re.escape(fmt)
                    if re.search(pattern, content, re.IGNORECASE):
                        format_data[fmt]['sections'].append({
                            'url': url,
                            'section': section,
                            'content': content[:500],  # First 500 chars
                        })
                        format_data[fmt]['urls'].add(url)

                        # Extract code blocks that might be examples
                        for code_block in code_blocks:
                            if any(keyword in code_block.lower() for keyword in
                                   [fmt.lower(), 'yaml', 'markdown', '---']):
                                format_data[fmt]['code_examples'].append(code_block)

            except json.JSONDecodeError:
                continue

    return format_data


def generate_documentation(format_data):
    """Generate markdown documentation for file formats."""

    output = []
    output.append("# GitHub Copilot File Formats\n")
    output.append("Complete guide to special file formats used by GitHub Copilot in VS Code.\n")
    output.append(f"Generated from {JSONL_FILE}\n\n")
    output.append("---\n\n")

    for fmt, desc in FILE_FORMATS.items():
        data = format_data.get(fmt, {})

        output.append(f"## {fmt}\n")
        output.append(f"**{desc}**\n\n")

        if data.get('urls'):
            output.append("### Documentation References\n")
            for url in sorted(data['urls'])[:5]:  # Top 5 URLs
                output.append(f"- {url}\n")
            output.append("\n")

        if data.get('code_examples'):
            output.append("### Examples\n\n")
            # Get unique examples (first 3)
            unique_examples = []
            seen = set()
            for example in data['code_examples']:
                # Normalize for comparison
                normalized = example.strip().lower()
                if normalized not in seen and len(unique_examples) < 3:
                    unique_examples.append(example)
                    seen.add(normalized)

            for i, example in enumerate(unique_examples, 1):
                output.append(f"**Example {i}:**\n\n")
                output.append(f"{example}\n\n")

        if data.get('sections'):
            output.append("### Key Information\n\n")
            # Get unique content snippets
            seen_content = set()
            for section_info in data['sections'][:3]:
                content = section_info['content'].strip()
                if content not in seen_content:
                    output.append(f"**{section_info.get('section', 'General')}**\n\n")
                    output.append(f"{content}...\n\n")
                    output.append(f"[Source]({section_info['url']})\n\n")
                    seen_content.add(content)

        output.append("---\n\n")

    return "".join(output)


def main():
    print("Extracting file format information...")
    format_data = extract_file_format_info()

    print("\nGenerating documentation...")
    documentation = generate_documentation(format_data)

    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(documentation)

    print(f"\n✓ Documentation written to {OUTPUT}")

    # Print summary
    print("\n" + "="*60)
    print("File Formats Found:")
    print("="*60)
    for fmt, desc in FILE_FORMATS.items():
        data = format_data.get(fmt, {})
        mentions = len(data.get('sections', []))
        examples = len(data.get('code_examples', []))
        print(f"{fmt:30} | Mentions: {mentions:3} | Examples: {examples:2}")


if __name__ == "__main__":
    main()
