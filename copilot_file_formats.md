# GitHub Copilot File Formats
Complete guide to special file formats used by GitHub Copilot in VS Code.
Generated from copilot_docs_with_images.jsonl

---

## .agent.md
**Custom agent definitions**

### Documentation References
- https://code.visualstudio.com/docs/copilot/customization/custom-agents
- https://code.visualstudio.com/docs/copilot/guides/context-engineering-guide

### Examples

**Example 1:**

```
---
title
: [
Short descriptive title of the feature
]
version
: [
optional version number
]
date_created
: [
YYYY-MM-DD
]
last_updated
: [
YYYY-MM-DD
]
---
# Implementation Plan:
<
feature
>
[Brief description of the requirements and goals of the feature]
## Architecture and design
Describe the high-level architecture and design considerations.
## Tasks
Break down the implementation into smaller, manageable tasks using a Markdown checklist format.
## Open questions
Outline 1-3 open questions or uncertainties that need to be clarified.
```

**Example 2:**

```
---
description
:
'Architect and planner to create detailed implementation plans.'
tools
: [
'fetch'
,
'githubRepo'
,
'problems'
,
'usages'
,
'search'
,
'todos'
,
'runSubagent'
,
'github/github-mcp-server/get_issue'
,
'github/github-mcp-server/get_issue_comments'
,
'github/github-mcp-server/list_issues'
]
handoffs
:
-
label
:
Start Implementation
agent
:
tdd
prompt
:
Now implement the plan outlined above using TDD principles.
send
:
true
---
# Planning Agent
You are an architect focused on creating detailed and comprehensive implementation plans for new features and bug fixes. Your goal is to break down complex requirements into clear, actionable tasks that can be easily understood and executed by developers.
## Workflow
1.
Analyze and understand: Gather context from the codebase and any provided documentation to fully understand the requirements and constraints. Run #tool:runSubagent tool, instructing the agent to work autonomously without pausing for user feedback.
2.
Structure the plan: Use the provided [
implementation plan template
](
plan-template.md
) to structure the plan.
3.
Pause for review: Based on user feedback or questions, iterate and refine the plan as needed.
```

**Example 3:**

```
---
agent
:
plan
description
:
Create a detailed implementation plan.
---
Briefly analyze my feature request, then ask me 3 questions to clarify the requirements. Only then start the planning workflow.
```

### Key Information

**What are custom agents?**

The built-in agents provide general-purpose configurations for chat in VS Code. For a more tailored chat experience, you can create your own custom agents.
Custom agents consist of a set of instructions and tools that are applied when you switch to that agent. For example, a "Plan" agent could include instructions for generating an implementation plan and only use read-only tools. By creating a custom agent, you can quickly switch to that specific configuration without having to manually select...

[Source](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

**Custom agent file structure**

Custom agent files are Markdown files and use the .agent.md extension and have the following structure.
VS Code detects any .md files in the .github/agents folder of your workspace as custom agents....

[Source](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

**Create a custom agent**

User profile : create the custom agent definition file in the current profile folder to use it across all your workspaces
User profile : create the custom agent definition file in the current profile folder to use it across all your workspaces
Enter a file name for the custom agent. This is the default name that appears in the agents dropdown.
Enter a file name for the custom agent. This is the default name that appears in the agents dropdown.
Provide the details for the custom agent in the newl...

[Source](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

---

## .chatmode.md
**Legacy custom chat modes (deprecated)**

### Documentation References
- https://code.visualstudio.com/docs/copilot/customization/custom-agents

### Key Information

**Create a custom agent**

If you've previously created custom chat modes with a .chatmode.md extension in the .github/chatmodes folder of your workspace, VS Code still recognizes those files as custom agents. You can use a Quick Fix action to rename and move them to the new .github/agents folder with a .agent.md extension....

[Source](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

**Are custom agents different from chat modes?**

Custom agents were previously known as custom chat modes. The functionality remains the same, but the terminology has been updated to better reflect their purpose in customizing AI behavior for specific tasks.
VS Code still recognizes any existing .chatmode.md files as custom agents. You can use a Quick Fix action to rename and move them to the new .github/agents folder with a .agent.md extension....

[Source](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

---

## .instructions.md
**Workspace instruction files**

### Documentation References
- https://code.visualstudio.com/docs/copilot/copilot-tips-and-tricks
- https://code.visualstudio.com/docs/copilot/customization/custom-instructions

### Examples

**Example 1:**

```
---
applyTo
:
"**/*.py"
---
# Project coding standards for Python
-
Follow the PEP 8 style guide for Python.
-
Always prioritize readability and clarity.
-
Write clear and concise comments for each function.
-
Ensure functions have descriptive names and include type hints.
-
Maintain proper indentation (use 4 spaces for each level of indentation).
```

**Example 2:**

```
---
applyTo
:
"**/*.ts"
---
Coding practices for TypeScript files.
...
```

### Key Information

**None**

Remote Overview SSH Dev Containers Windows Subsystem for Linux GitHub Codespaces VS Code Server Tunnels SSH Tutorial WSL Tutorial Tips and Tricks FAQ
Overview
SSH
Dev Containers
Windows Subsystem for Linux
GitHub Codespaces
VS Code Server
Tunnels
SSH Tutorial
WSL Tutorial
Tips and Tricks
FAQ
Dev Containers Overview Tutorial Attach to Container Create Dev Container Advanced Containers devcontainer.json Dev Container CLI Tips and Tricks FAQ
Overview
Tutorial
Attach to Container
Create Dev Containe...

[Source](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)

**Type of instructions files**

VS Code supports multiple types of Markdown-based instructions files. If you have multiple types of instructions files in your project, VS Code combines and adds them to the chat context, no specific order is guaranteed.
A single .github/copilot-instructions.md file Automatically applies to all chat requests in the workspace Stored within the workspace
A single .github/copilot-instructions.md file
Automatically applies to all chat requests in the workspace
Stored within the workspace
One or more...

[Source](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)

**Use .instructions.md files**

Instead of using a single instructions file that applies to all chat requests, you can create multiple .instructions.md files that apply to specific file types or tasks. For example, you can create instructions files for different programming languages, frameworks, or project types.
By using the applyTo frontmatter property in the instructions file header, you can specify a glob pattern to define which files the instructions should be applied to automatically. Instructions files are used when cr...

[Source](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)

---

## .prompt.md
**Reusable prompt templates**

### Documentation References
- https://code.visualstudio.com/docs/copilot/chat/chat-planning
- https://code.visualstudio.com/docs/copilot/chat/chat-sessions
- https://code.visualstudio.com/docs/copilot/copilot-tips-and-tricks
- https://code.visualstudio.com/docs/copilot/customization/prompt-files
- https://code.visualstudio.com/docs/copilot/guides/context-engineering-guide

### Examples

**Example 1:**

```
---
title
: [
Short descriptive title of the feature
]
version
: [
optional version number
]
date_created
: [
YYYY-MM-DD
]
last_updated
: [
YYYY-MM-DD
]
---
# Implementation Plan:
<
feature
>
[Brief description of the requirements and goals of the feature]
## Architecture and design
Describe the high-level architecture and design considerations.
## Tasks
Break down the implementation into smaller, manageable tasks using a Markdown checklist format.
## Open questions
Outline 1-3 open questions or uncertainties that need to be clarified.
```

**Example 2:**

```
---
description
:
'Architect and planner to create detailed implementation plans.'
tools
: [
'fetch'
,
'githubRepo'
,
'problems'
,
'usages'
,
'search'
,
'todos'
,
'runSubagent'
,
'github/github-mcp-server/get_issue'
,
'github/github-mcp-server/get_issue_comments'
,
'github/github-mcp-server/list_issues'
]
handoffs
:
-
label
:
Start Implementation
agent
:
tdd
prompt
:
Now implement the plan outlined above using TDD principles.
send
:
true
---
# Planning Agent
You are an architect focused on creating detailed and comprehensive implementation plans for new features and bug fixes. Your goal is to break down complex requirements into clear, actionable tasks that can be easily understood and executed by developers.
## Workflow
1.
Analyze and understand: Gather context from the codebase and any provided documentation to fully understand the requirements and constraints. Run #tool:runSubagent tool, instructing the agent to work autonomously without pausing for user feedback.
2.
Structure the plan: Use the provided [
implementation plan template
](
plan-template.md
) to structure the plan.
3.
Pause for review: Based on user feedback or questions, iterate and refine the plan as needed.
```

**Example 3:**

```
---
agent
:
plan
description
:
Create a detailed implementation plan.
---
Briefly analyze my feature request, then ask me 3 questions to clarify the requirements. Only then start the planning workflow.
```

### Key Information

**Save a chat session as a reusable prompt**

You can save a chat session as a reusable prompt to reuse for similar tasks.
To save a chat session as a reusable prompt:
Open the chat session you want to save in the Chat view.
Open the chat session you want to save in the Chat view.
Type /savePrompt in the chat input box and press Enter . The command creates a .prompt.md file that generalizes your current chat conversation into a reusable prompt. The prompt file has placeholders where appropriate.
Type /savePrompt in the chat input box and pr...

[Source](https://code.visualstudio.com/docs/copilot/chat/chat-sessions)

**How to plan a task**

The plan agent provides a high-level summary and a breakdown of steps, including any open questions for clarification.
Stay in plan mode to refine your plan before implementation. You can iterate multiple times to clarify requirements, adjust scope, or address open questions. This ensures a solid foundation before any code changes are made.
Once finalized, choose to save the plan or hand off to an implementation agent to start coding by using the corresponding controls. When starting to implemen...

[Source](https://code.visualstudio.com/docs/copilot/chat/chat-planning)

**Prompt file structure**

Prompt files are Markdown files and use the .prompt.md extension and have this structure:...

[Source](https://code.visualstudio.com/docs/copilot/customization/prompt-files)

---

## .plan.md
**Planning documents**

### Documentation References
- https://code.visualstudio.com/docs/copilot/chat/chat-sessions

### Key Information

**Invoke a subagent**

By default, a subagent inherits the agent from the main chat session. If you invoke a subagent from a custom agent, that subagent also runs with that agent.
With the experimental chat.customAgentInSubagent.enabled setting, subagents can run with a different (custom) agent.
To run a subagent with a specific agent:
Enable the chat.customAgentInSubagent.enabled setting
Enable the chat.customAgentInSubagent.enabled setting
Prompt the AI to use a custom or built-in agent for the subagent. For example...

[Source](https://code.visualstudio.com/docs/copilot/chat/chat-sessions)

---

## .copilotignore
**Files to exclude from Copilot context**

---

## copilot-instructions.md
**Workspace-level instructions**

### Documentation References
- https://code.visualstudio.com/docs/copilot/chat/mcp-servers
- https://code.visualstudio.com/docs/copilot/customization/custom-instructions
- https://code.visualstudio.com/docs/copilot/customization/mcp-servers
- https://code.visualstudio.com/docs/copilot/customization/overview
- https://code.visualstudio.com/docs/copilot/getting-started

### Examples

**Example 1:**

```
---
description
:
'Review code for quality and adherence to best practices.'
tools
: [
'usages'
,
'vscodeAPI'
,
'problems'
,
'fetch'
,
'githubRepo'
,
'search'
]
---
# Code Reviewer agent
You are an experienced senior developer conducting a thorough code review. Your role is to review the code for quality, best practices, and adherence to [
project standards
](
../copilot-instructions.md
) without making direct code changes.
When reviewing code, structure your feedback with clear headings and specific examples from the code being reviewed.
## Analysis Focus
-
Analyze code quality, structure, and best practices
-
Identify potential bugs, security issues, or performance problems
-
Evaluate accessibility and user experience considerations
## Important Guidelines
-
Ask clarifying questions about design decisions when appropriate
-
Focus on explaining what should be changed and why
-
DO NOT write or suggest specific code changes directly
```

### Key Information

**Create custom instructions**

Custom instructions tell the AI about your coding preferences and standards. These apply automatically to all chat interactions.
Create a new folder called .github in your project root.
Create a new folder called .github in your project root.
Inside the .github folder, create a file called copilot-instructions.md .
Inside the .github folder, create a file called copilot-instructions.md .
Add the following content: # Project general coding guidelines ## Code Style - Use semantic HTML5 elements (h...

[Source](https://code.visualstudio.com/docs/copilot/getting-started)

**Create a custom agent for code reviews**

Replace the file contents with the following content. Note that this custom agent doesn't allow code changes. --- description : 'Review code for quality and adherence to best practices.' tools : [ 'usages' , 'vscodeAPI' , 'problems' , 'fetch' , 'githubRepo' , 'search' ] --- # Code Reviewer agent You are an experienced senior developer conducting a thorough code review. Your role is to review the code for quality, best practices, and adherence to [ project standards ]( ../copilot-instructions.md...

[Source](https://code.visualstudio.com/docs/copilot/getting-started)

**2. Set up basic guidelines**

Create custom instructions for consistent results across all your chat interactions. Create a .github/copilot-instructions.md file with your coding standards and preferences. This automatically improves all chat responses without extra effort. Create different instructions files for different parts of your codebase using glob patterns to target specific languages or frameworks....

[Source](https://code.visualstudio.com/docs/copilot/customization/overview)

---

