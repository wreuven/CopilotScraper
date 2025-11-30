# GitHub Copilot Documentation Scraper

Complete scraper for GitHub Copilot documentation in VS Code, including text, code examples, images, and special file formats.

## What's Included

### 📄 Documentation Content
- **30 pages** of official Copilot documentation
- **918 content chunks** in JSONL format
- Full text, code examples, and metadata

### 🖼️ Images & Diagrams
- **126 screenshots and diagrams** downloaded locally
- Organized by topic in `images/` directory
- **15MB** of visual content
- Metadata includes: alt text, context, captions

### 📋 Special File Formats
Documented with examples:
- **`.agent.md`** - Custom agent definitions (9 mentions, 8 examples)
- **`.prompt.md`** - Reusable prompt templates (6 mentions, 5 examples)
- **`.instructions.md`** - Workspace instruction files (8 mentions, 2 examples)
- **`copilot-instructions.md`** - Workspace-level instructions (12 mentions)
- **`.chatmode.md`** - Legacy custom modes (deprecated)
- **`.plan.md`** - Planning documents

## Files Generated

### Main Output Files
```
copilot_docs_with_images.jsonl  # 2.5MB - All documentation chunks with metadata
copilot_file_formats.md         # Guide to special file formats
images/                         # 15MB - All screenshots and diagrams
```

### Scripts
```
scrape.py                       # Original basic scraper
scrape_with_images.py          # Enhanced scraper with image downloads
extract_file_formats.py        # Extract file format documentation
```

## JSONL Structure

Each line in `copilot_docs_with_images.jsonl` contains:

```json
{
  "url": "https://code.visualstudio.com/docs/copilot/...",
  "path": "/docs/copilot/...",
  "doc_title": "Page title",
  "section_heading": "Section name",
  "anchor": "section-anchor",
  "chunk_id": "unique-id",
  "content": "Text content...",
  "code_blocks": ["```python\\n...\\n```"],
  "images": [
    {
      "url": "https://...",
      "local_path": "images/copilot/...",
      "alt_text": "Description",
      "caption": "Caption if present",
      "context": "Surrounding section"
    }
  ],
  "source": "vscode-copilot-docs"
}
```

## Image Organization

Images are organized by topic:
```
images/
├── copilot/
│   ├── overview/
│   ├── setup/
│   ├── getting-started/
│   ├── chat/
│   ├── chat-checkpoints/
│   ├── chat-sessions/
│   ├── customization/
│   └── ...
└── ai/
    └── mcp/
```

## Usage Examples

### Search for specific topics
```bash
# Find all mentions of MCP servers
jq -r 'select(.content | test("MCP|Model Context Protocol"; "i")) | {url, section: .section_heading, content: .content[:200]}' copilot_docs_with_images.jsonl
```

### Extract code examples
```bash
# Get all Python code examples
jq -r '.code_blocks[] | select(test("```python"))' copilot_docs_with_images.jsonl
```

### Find images for a topic
```bash
# Get images related to agents
jq -r 'select(.images | length > 0) | select(.content | test("agent"; "i")) | .images[].local_path' copilot_docs_with_images.jsonl | sort -u
```

### List all pages
```bash
jq -r '.url' copilot_docs_with_images.jsonl | sort -u
```

## Creating Slides

The scraped data is perfect for creating presentations:

1. **Use images**: 126 high-quality screenshots in `images/`
2. **Use code examples**: Extracted and formatted code blocks
3. **Use structured content**: Section headings and organized text
4. **Use metadata**: Context and descriptions for each image

Example workflow:
```python
import json

# Load all data
with open('copilot_docs_with_images.jsonl') as f:
    docs = [json.loads(line) for line in f]

# Create slide about custom agents
agent_docs = [d for d in docs if 'agent' in d.get('section_heading', '').lower()]
for doc in agent_docs[:5]:
    print(f"Slide: {doc['section_heading']}")
    print(f"Content: {doc['content'][:200]}")
    if doc['images']:
        print(f"Image: {doc['images'][0]['local_path']}")
    print()
```

## What's NOT Included

### Settings Schema
The official docs describe settings, but the complete JSON schema is in the extension's `package.json`. To get ALL settings:

1. Download the GitHub Copilot extension `.vsix` from the marketplace
2. Extract and parse `extension/package.json`
3. Look for `contributes.configuration`

### Undocumented Features
- Internal/experimental settings
- Extension API details (for building Copilot extensions)
- Some advanced edge cases

### How to Get Complete Settings

```bash
# Download extension (example - URL may change)
curl -L "https://marketplace.visualstudio.com/_apis/public/gallery/publishers/GitHub/vsextensions/copilot/latest/vspackage" -o copilot.vsix

# Extract
unzip copilot.vsix

# Parse package.json
jq '.contributes.configuration' extension/package.json
```

## Documentation Coverage

### Topics Covered
✅ Overview and setup
✅ Chat and inline suggestions
✅ Custom agents and modes
✅ Instructions and prompts
✅ MCP servers
✅ Language models
✅ Planning and checkpoints
✅ Smart actions
✅ Security and FAQ

### File Format Schemas
✅ `.agent.md` - Full YAML frontmatter structure
✅ `.prompt.md` - Template format
✅ `.instructions.md` - Instruction syntax
✅ `copilot-instructions.md` - Workspace instructions
✅ MCP server config - JSON schema

## Run the Scraper

### Basic scraper (text only)
```bash
python scrape.py
```

### Enhanced scraper (text + images)
```bash
python scrape_with_images.py
```

### Extract file format docs
```bash
python extract_file_formats.py
```

## Dependencies

```bash
pip install requests beautifulsoup4
```

## Use Cases

1. **Create presentations** - Use images and structured content
2. **Build AI assistants** - Feed the JSONL to RAG systems
3. **Generate documentation** - Extract and reorganize content
4. **Search and analysis** - Query specific features and examples
5. **Training data** - Use for fine-tuning or prompt engineering
6. **Reference guide** - Offline access to all Copilot docs

## Statistics

- **Pages scraped**: 30
- **Content chunks**: 918
- **Images**: 126 screenshots/diagrams
- **Code examples**: ~200+
- **File format examples**: 15+
- **Total size**: ~17.5MB (2.5MB JSONL + 15MB images)

## License & Attribution

This scraper is for personal/educational use. All documentation content and images are:
- © Microsoft Corporation
- Source: https://code.visualstudio.com/docs/copilot/

Always attribute and link back to the official documentation.
