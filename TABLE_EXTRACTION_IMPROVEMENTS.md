# Table Extraction Improvements

## Problem Identified

The original scrapers (`scrape.py` and `scrape_with_images.py`) only extracted:
- Headings (h2, h3)
- Paragraphs (`<p>`)
- List items (`<li>`)
- Code blocks (`<pre>`)

**Missing:** HTML `<table>` elements were completely ignored!

This meant critical structured data like the `.agent.md` field specifications table was not captured.

## Solution Implemented

Added comprehensive table extraction to both scrapers with markdown conversion.

### New Function: `extract_table_as_markdown()`

Converts HTML tables to markdown format:

```python
def extract_table_as_markdown(table: Tag) -> str:
    """Convert HTML table to markdown format."""
    # Extracts:
    # - Headers from <thead> or first <tr>
    # - Body rows from <tbody>
    # - Converts to markdown table syntax
```

### Features:
- ✅ Detects headers from `<thead>` or first row
- ✅ Handles `<tbody>` or direct `<tr>` elements
- ✅ Cleans cell text (strips whitespace, handles multiline)
- ✅ Outputs proper markdown table format
- ✅ Appends tables to section text content

## Before vs After

### Before (Missing Table)
```json
{
  "section_heading": "Header (optional)",
  "content": "The header is formatted as YAML frontmatter with the following fields:\nIf a given tool is not available when using the custom agent, it is ignored."
}
```

**Missing:** All field descriptions!

### After (With Table)
```json
{
  "section_heading": "Header (optional)",
  "content": "The header is formatted as YAML frontmatter with the following fields:\nIf a given tool is not available when using the custom agent, it is ignored.\n\n| Field | Description |\n| --- | --- |\n| description | A brief description of the custom agent, shown as placeholder text in the chat input field. |\n| name | The name of the custom agent. If not specified, the file name is used. |\n| argument-hint | Optional hint text shown in the chat input field to guide users on how to interact with the custom agent. |\n| tools | A list of tool or tool set names that are available for this custom agent. Can include built-in tools, tool sets, MCP tools, or tools contributed by extensions. To include all tools of an MCP server, use the <server name>/* format. |\n| model | The AI model to use when running the prompt. If not specified, the currently selected model in model picker is used. |\n| target | The target environment or context for the custom agent ( vscode or github-copilot ). |\n| mcp-servers | Optional list of Model Context Protocol (MCP) server config json to use with custom agents in GitHub Copilot (target: github-copilot ). |\n| handoffs | Optional list of suggested next actions or prompts to transition between custom agents. Handoff buttons appear as interactive suggestions after a chat response completes. |\n| handoffs.label | The display text shown on the handoff button. |\n| handoffs.agent | The target agent identifier to switch to. |\n| handoffs.prompt | The prompt text to send to the target agent. |\n| handoffs.send | Optional boolean flag to auto-submit the prompt (default is false ) |"
}
```

**Now includes:** Complete field reference table!

## Implementation Details

### Modified Files:
1. **`scrape.py`** - Basic scraper
2. **`scrape_with_images.py`** - Enhanced scraper with images

### Changes Made:

#### 1. Added `extract_table_as_markdown()` function
```python
def extract_table_as_markdown(table: Tag) -> str:
    # Converts HTML <table> to markdown
    # Returns: "| Header | Header |\n| --- | --- |\n| Cell | Cell |"
```

#### 2. Updated `extract_sections()` to track tables
```python
current = {
    "heading": None,
    "anchor": None,
    "text_parts": [],
    "code_blocks": [],
    "tables": []  # NEW: Track tables
}
```

#### 3. Added table detection in element loop
```python
# Tables
if el.name == "table":
    table_md = extract_table_as_markdown(el)
    if table_md:
        current["tables"].append(table_md)
```

#### 4. Append tables to section text
```python
def flush_current():
    text = "\n".join(p.strip() for p in current["text_parts"] if p.strip())

    # Append tables to text
    if current["tables"]:
        text += "\n\n" + "\n\n".join(current["tables"])
```

## Test Results

### Test Case: Custom Agents Documentation

**Page:** `https://code.visualstudio.com/docs/copilot/customization/custom-agents`

**Tables Found:** 1 table with 12 rows

**Sample Output:**
```markdown
| Field | Description |
| --- | --- |
| description | A brief description of the custom agent, shown as placeholder text in the chat input field. |
| name | The name of the custom agent. If not specified, the file name is used. |
| argument-hint | Optional hint text shown in the chat input field to guide users on how to interact with the custom agent. |
| tools | A list of tool or tool set names that are available for this custom agent... |
...
```

### Verification Command:
```bash
python /tmp/test_single_page.py
```

Output:
```
Testing table extraction on: https://code.visualstudio.com/docs/copilot/customization/custom-agents

=== Header (optional) ===
The header is formatted as YAML frontmatter with the following fields:
If a given tool is not available when using the custom agent, it is ignored.

| Field | Description |
| --- | --- |
| description | A brief description of the custom agent...

✓ Table detected in content!
```

## Impact

### What This Fixes:

1. **Complete .agent.md specification** - Field descriptions now captured
2. **Settings tables** - Configuration tables in documentation
3. **Command tables** - Command reference tables
4. **Comparison tables** - Feature comparison matrices
5. **Any structured data** - All HTML tables in documentation

### Pages Affected:

Pages with tables that will now be properly scraped:
- `/docs/copilot/customization/custom-agents` - Agent field specifications ✓
- `/docs/copilot/customization/prompt-files` - Prompt file fields
- `/docs/copilot/reference/*` - Reference documentation
- Settings pages with configuration tables
- Any other documentation with structured data

## Usage

### Re-run Scraper with Table Support:

**Basic scraper:**
```bash
python scrape.py
```

**Enhanced scraper (with images):**
```bash
python scrape_with_images.py
```

Both now include table extraction!

### Query Tables in JSONL:

```bash
# Find all sections with tables (contain markdown table syntax)
jq -r 'select(.content | test("\\| .* \\|")) | {url, section: .section_heading}' \
  copilot_docs_with_images.jsonl

# Extract table content
jq -r 'select(.section_heading == "Header (optional)") | .content' \
  copilot_docs_with_images.jsonl | grep "^|"
```

## Markdown Table Format

Tables are converted to standard markdown format:

```markdown
| Column 1 | Column 2 | Column 3 |
| --- | --- | --- |
| Value 1 | Value 2 | Value 3 |
| Value 4 | Value 5 | Value 6 |
```

**Benefits:**
- ✅ Human-readable in JSONL
- ✅ Can be rendered in markdown viewers
- ✅ Preserves structure for AI processing
- ✅ Easy to parse programmatically

## Next Steps

To get the complete dataset with tables:

1. **Delete old JSONL** (optional):
   ```bash
   rm copilot_docs_with_images.jsonl
   ```

2. **Re-run enhanced scraper**:
   ```bash
   python scrape_with_images.py
   ```

3. **Verify table extraction**:
   ```bash
   jq -r 'select(.content | test("\\| .* \\|")) | .section_heading' \
     copilot_docs_with_images.jsonl | sort -u
   ```

You should see sections like:
- "Header (optional)"
- "Frontmatter fields"
- "Settings reference"
- Etc.

## Summary

**Problem:** Tables were ignored during scraping
**Solution:** Added markdown table extraction to both scrapers
**Result:** Complete structured data now captured in documentation

All HTML tables are now converted to markdown and included in the section `content` field!
