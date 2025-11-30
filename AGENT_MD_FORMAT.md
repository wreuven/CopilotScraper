# .agent.md File Format Specification

## Research Process Documentation

### Step 1: Search Documentation JSONL ✅
**Method:** Searched `copilot_docs_with_images.jsonl` for mentions of `.agent.md`
**Found:** 9 chunks referencing the format across 2 main pages:
- `https://code.visualstudio.com/docs/copilot/customization/custom-agents`
- `https://code.visualstudio.com/docs/copilot/guides/context-engineering-guide`

### Step 2: Extract Code Examples ✅
**Method:** Extracted code blocks from sections mentioning `.agent.md`
**Found:** 3 complete examples with different levels of complexity

### Step 3: Check Extension Metadata ✅
**Method:** Searched `extension_metadata/copilot-chat_package.json` for schema definitions
**Result:** No additional schema beyond documentation (format is document-based, not JSON schema)

### Step 4: Fetch Live Documentation ✅
**Method:** Direct fetch from official VS Code documentation
**Result:** Complete specification with all fields and their descriptions

---

## Complete .agent.md File Format

### File Structure

```
---
[YAML Frontmatter]
---
[Markdown Body]
```

### Location
- **Workspace agents**: `.github/agents/` folder in your workspace
- **User profile agents**: User profile folder (reusable across workspaces)

**Note:** VS Code automatically detects any `.md` files in `.github/agents/` as custom agents.

---

## YAML Frontmatter Fields

### Required Fields
None are strictly required, but `description` is highly recommended.

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | Brief description shown as placeholder text in chat input field |
| `name` | string | Agent name. If not specified, filename is used |
| `argument-hint` | string | Optional hint text shown in chat input to guide user interaction |
| `tools` | array of strings | List of tool/tool set names available to this agent. Can include:<br/>- Built-in tools (`search`, `fetch`, `githubRepo`, etc.)<br/>- Tool sets<br/>- MCP tools<br/>- Extension-contributed tools<br/>- Use `<server-name>/*` to include all tools from an MCP server |
| `model` | string | AI model to use (e.g., `Claude Sonnet 4`). If not specified, uses current model picker selection |
| `target` | string | Target environment: `vscode` or `github-copilot` |
| `mcp-servers` | array | Optional list of MCP server config JSON for GitHub Copilot custom agents (requires `target: github-copilot`) |
| `handoffs` | array of objects | List of suggested next actions for transitioning between agents |

### Handoffs Object Structure

Each handoff in the `handoffs` array has:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `label` | string | ✅ Yes | Display text shown on the handoff button |
| `agent` | string | ✅ Yes | Target agent identifier to switch to |
| `prompt` | string | ✅ Yes | Prompt text to send to target agent |
| `send` | boolean | No | Auto-submit the prompt (default: `false`) |

---

## Markdown Body

The body contains the agent's instructions formatted as Markdown.

### Features:
- **Markdown formatting**: Use headings, lists, code blocks, etc.
- **File references**: Use Markdown links to reference other files (e.g., instructions files)
- **Tool references**: Use `#tool:<tool-name>` syntax to reference tools
  - Example: `#tool:githubRepo` references the GitHub repository tool
  - Example: `#tool:runSubagent` references the subagent tool

### Behavior:
When you select the custom agent in Chat view, the body text is prepended to your chat prompt.

---

## Complete Example

```markdown
---
description: Generate an implementation plan for new features or refactoring existing code.
name: Planner
tools: ['fetch', 'githubRepo', 'search', 'usages']
model: Claude Sonnet 4
handoffs:
  - label: Implement Plan
    agent: agent
    prompt: Implement the plan outlined above.
    send: false
---
# Planning instructions

You are in planning mode. Your task is to generate an implementation plan for a new feature or for refactoring existing code.

Don't make any code edits, just generate a plan.

The plan consists of a Markdown document that describes the implementation plan, including the following sections:

* Overview: A brief description of the feature or refactoring task.
* Requirements: A list of requirements for the feature or refactoring task.
* Implementation Steps: A detailed list of steps to implement the feature or refactoring task.
* Testing: A list of tests that need to be implemented to verify the feature or refactoring task.
```

---

## Minimal Example

```markdown
---
description: Generate an implementation plan
tools: ['search', 'fetch']
handoffs:
  - label: Start Implementation
    agent: implementation
    prompt: Now implement the plan outlined above.
    send: false
---
```

Even simpler (no frontmatter):

```markdown
# Code Reviewer

Review the code for:
- Security vulnerabilities
- Performance issues
- Best practices
```

---

## Advanced Example (with MCP and subagents)

```markdown
---
description: Architect and planner to create detailed implementation plans.
tools: [
  'fetch',
  'githubRepo',
  'problems',
  'usages',
  'search',
  'todos',
  'runSubagent',
  'github/github-mcp-server/get_issue',
  'github/github-mcp-server/get_issue_comments',
  'github/github-mcp-server/list_issues'
]
handoffs:
  - label: Start Implementation
    agent: tdd
    prompt: Now implement the plan outlined above using TDD principles.
    send: true
---
# Planning Agent

You are an architect focused on creating detailed and comprehensive implementation plans for new features and bug fixes. Your goal is to break down complex requirements into clear, actionable tasks that can be easily understood and executed by developers.

## Workflow

1. Analyze and understand: Gather context from the codebase and any provided documentation to fully understand the requirements and constraints. Run #tool:runSubagent tool, instructing the agent to work autonomously without pausing for user feedback.

2. Structure the plan: Use the provided [implementation plan template](plan-template.md) to structure the plan.

3. Pause for review: Based on user feedback or questions, iterate and refine the plan as needed.
```

---

## Built-in Tool Names

Common tool names you can use in the `tools` array:

### Read-only Tools
- `search` - Semantic code search
- `fetch` - Read file contents
- `githubRepo` - GitHub repository information
- `usages` - Find symbol usages
- `problems` - Workspace problems/diagnostics
- `todos` - TODO comments

### Edit Tools
- `edits` - Make file edits
- `terminal` - Terminal commands
- `runSubagent` - Run autonomous subagent

### MCP Tools
- Format: `<server-name>/<tool-name>` or `<server-name>/*` for all tools
- Example: `github/github-mcp-server/get_issue`

---

## File Naming

- Extension: `.agent.md`
- Location: `.github/agents/` in workspace OR user profile directory
- Name becomes agent ID (unless `name` field overrides it)

Example filenames:
- `.github/agents/planner.agent.md`
- `.github/agents/code-reviewer.agent.md`
- `.github/agents/security.agent.md`

---

## Legacy Format

**Previous format:** `.chatmode.md` in `.github/chatmodes/`

VS Code still recognizes old `.chatmode.md` files but recommends migrating:
1. Rename file extension: `.chatmode.md` → `.agent.md`
2. Move to new folder: `.github/chatmodes/` → `.github/agents/`
3. Use Quick Fix in VS Code to auto-migrate

---

## Validation & Behavior

### What happens if a field is invalid?
- Unknown tools are **ignored** (agent still works)
- Invalid model name falls back to **current model picker selection**
- Missing frontmatter is **allowed** (body-only agents work fine)

### Priority Order for Tools
When both prompt files and agents specify tools:

1. Tools from prompt file (highest priority)
2. Tools from referenced agent in prompt file
3. Default tools for selected agent (lowest priority)

---

## Creating an Agent (UI Flow)

1. Open agent dropdown in Chat view
2. Select "Configure Custom Agents"
3. Click "Create new custom agent"
4. Choose location:
   - **Workspace** → `.github/agents/`
   - **User profile** → profile directory
5. Enter filename (without extension)
6. VS Code creates `.agent.md` file with template
7. Edit YAML frontmatter and Markdown body
8. Save file
9. Agent appears in dropdown immediately

---

## Key Differences from Other Formats

| Feature | .agent.md | .prompt.md | .instructions.md |
|---------|-----------|------------|------------------|
| Purpose | Define custom AI persona | Reusable prompts | Workspace instructions |
| Tools config | ✅ Yes | ✅ Yes | ❌ No |
| Model selection | ✅ Yes | ✅ Yes | ❌ No |
| Handoffs | ✅ Yes | ❌ No | ❌ No |
| Auto-applies | When selected | When invoked | Always (workspace) |

---

## Official Documentation References

- Primary: https://code.visualstudio.com/docs/copilot/customization/custom-agents
- Examples: https://code.visualstudio.com/docs/copilot/guides/context-engineering-guide
- Community examples: https://github.com/github/awesome-copilot

---

## Schema Version

**As of:** VS Code 1.106 (November 2024)
**Format:** Markdown with YAML frontmatter
**Stability:** Stable (migrated from `.chatmode.md`)

---

## Summary

**Precise Format:**
1. Optional YAML frontmatter between `---` delimiters
2. Markdown body with agent instructions
3. File extension: `.agent.md`
4. Location: `.github/agents/` or user profile
5. All fields are optional
6. Tools use `#tool:<name>` syntax in body
7. Handoffs enable agent-to-agent workflows

**Most Common Pattern:**
```markdown
---
description: <what agent does>
tools: [<list of tools>]
handoffs:
  - label: <button text>
    agent: <target agent>
    prompt: <transition prompt>
    send: false
---
# <Agent Name>

<Instructions in Markdown>
```
