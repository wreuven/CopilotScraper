# GitHub Copilot Chat - Commands Reference

Version: 0.34.2025112801

Total commands: 95

---

## `github.copilot.chat.triggerPermissiveSignIn`

**%github.copilot.command.triggerPermissiveSignIn%**


## `github.copilot.claude.sessions.refresh`

**%github.copilot.command.refreshClaudeCodeSessions%**

Category: Claude Code


## `github.copilot.cli.sessions.refresh`

**%github.copilot.command.refreshAgentSessions%**

Category: Copilot CLI


## `github.copilot.cli.sessions.delete`

**%github.copilot.command.deleteAgentSession%**

Category: Copilot CLI


## `github.copilot.cli.sessions.resumeInTerminal`

**%github.copilot.command.cli.sessions.resumeInTerminal%**

Category: Copilot CLI


## `github.copilot.cli.sessions.newTerminalSession`

**%github.copilot.cli.sessions.newTerminalSession%**

Category: Copilot CLI


## `github.copilot.chat.replay`

**Start Chat Replay**

Enablement: `resourceFilename === 'benchRun.chatReplay.json' && !inDebugMode`


## `github.copilot.chat.replay.enableWorkspaceEditTracing`

**%github.copilot.command.enableEditTracing%**

Category: Developer

Enablement: `!github.copilot.chat.replay.workspaceEditTracing`


## `github.copilot.chat.replay.disableWorkspaceEditTracing`

**%github.copilot.command.disableEditTracing%**

Category: Developer

Enablement: `github.copilot.chat.replay.workspaceEditTracing`


## `github.copilot.chat.explain`

**%github.copilot.command.explainThis%**

Category: Chat

Enablement: `!github.copilot.interactiveSession.disabled`


## `github.copilot.chat.explain.palette`

**%github.copilot.command.explainThis%**

Category: Chat

Enablement: `!github.copilot.interactiveSession.disabled && !editorReadonly`


## `github.copilot.chat.review`

**%github.copilot.command.reviewAndComment%**

Category: Chat

Enablement: `config.github.copilot.chat.reviewSelection.enabled && !github.copilot.interactiveSession.disabled`


## `github.copilot.chat.review.apply`

**%github.copilot.command.applyReviewSuggestion%**

Category: Chat

Enablement: `commentThread =~ /hasSuggestion/`


## `github.copilot.chat.review.applyAndNext`

**%github.copilot.command.applyReviewSuggestionAndNext%**

Category: Chat

Enablement: `commentThread =~ /hasSuggestion/`


## `github.copilot.chat.review.discard`

**%github.copilot.command.discardReviewSuggestion%**

Category: Chat


## `github.copilot.chat.review.discardAndNext`

**%github.copilot.command.discardReviewSuggestionAndNext%**

Category: Chat


## `github.copilot.chat.review.discardAll`

**%github.copilot.command.discardAllReviewSuggestion%**

Category: Chat


## `github.copilot.chat.review.stagedChanges`

**%github.copilot.command.reviewStagedChanges%**

Category: Chat

Enablement: `github.copilot.chat.reviewDiff.enabled && !github.copilot.interactiveSession.disabled`


## `github.copilot.chat.review.unstagedChanges`

**%github.copilot.command.reviewUnstagedChanges%**

Category: Chat

Enablement: `github.copilot.chat.reviewDiff.enabled && !github.copilot.interactiveSession.disabled`


## `github.copilot.chat.review.changes`

**%github.copilot.command.reviewChanges%**

Category: Chat

Enablement: `github.copilot.chat.reviewDiff.enabled && !github.copilot.interactiveSession.disabled`


## `github.copilot.chat.review.stagedFileChange`

**%github.copilot.command.reviewFileChange%**

Category: Chat

Enablement: `github.copilot.chat.reviewDiff.enabled && !github.copilot.interactiveSession.disabled`


## `github.copilot.chat.review.unstagedFileChange`

**%github.copilot.command.reviewFileChange%**

Category: Chat

Enablement: `github.copilot.chat.reviewDiff.enabled && !github.copilot.interactiveSession.disabled`


## `github.copilot.chat.review.previous`

**%github.copilot.command.gotoPreviousReviewSuggestion%**

Category: Chat


## `github.copilot.chat.review.next`

**%github.copilot.command.gotoNextReviewSuggestion%**

Category: Chat


## `github.copilot.chat.review.continueInInlineChat`

**%github.copilot.command.continueReviewInInlineChat%**

Category: Chat


## `github.copilot.chat.review.continueInChat`

**%github.copilot.command.continueReviewInChat%**

Category: Chat


## `github.copilot.chat.review.markHelpful`

**%github.copilot.command.helpfulReviewSuggestion%**

Category: Chat

Enablement: `!(commentThread =~ /markedAsHelpful/)`


## `github.copilot.chat.openUserPreferences`

**%github.copilot.command.openUserPreferences%**

Category: Chat

Enablement: `config.github.copilot.chat.enableUserPreferences`


## `github.copilot.chat.tools.memory.openFolder`

**%github.copilot.command.openMemoryFolder%**

Category: Chat

Enablement: `config.github.copilot.chat.tools.memory.enabled`


## `github.copilot.chat.review.markUnhelpful`

**%github.copilot.command.unhelpfulReviewSuggestion%**

Category: Chat

Enablement: `!(commentThread =~ /markedAsUnhelpful/)`


## `github.copilot.chat.generate`

**%github.copilot.command.generateThis%**

Category: Chat

Enablement: `!github.copilot.interactiveSession.disabled && !editorReadonly`


## `github.copilot.chat.generateDocs`

**%github.copilot.command.generateDocs%**

Category: Chat

Enablement: `!github.copilot.interactiveSession.disabled && !editorReadonly`


## `github.copilot.chat.generateTests`

**%github.copilot.command.generateTests%**

Category: Chat

Enablement: `!github.copilot.interactiveSession.disabled && !editorReadonly`


## `github.copilot.chat.fix`

**%github.copilot.command.fixThis%**

Category: Chat

Enablement: `!github.copilot.interactiveSession.disabled && !editorReadonly`


## `github.copilot.interactiveSession.feedback`

**%github.copilot.command.sendChatFeedback%**

Category: Chat

Enablement: `github.copilot-chat.activated && !github.copilot.interactiveSession.disabled`


## `github.copilot.debug.workbenchState`

**%github.copilot.command.logWorkbenchState%**

Category: Developer


## `github.copilot.debug.showChatLogView`

**%github.copilot.command.showChatLogView%**

Category: Developer


## `github.copilot.debug.showOutputChannel`

**%github.copilot.command.showOutputChannel%**

Category: Developer


## `github.copilot.debug.showContextInspectorView`

**%github.copilot.command.showContextInspectorView%**

Category: Developer


## `github.copilot.debug.resetVirtualToolGroups`

**%github.copilot.command.resetVirtualToolGroups%**

Category: Developer


## `github.copilot.terminal.explainTerminalLastCommand`

**%github.copilot.command.explainTerminalLastCommand%**

Category: Chat


## `github.copilot.git.generateCommitMessage`

**%github.copilot.git.generateCommitMessage%**

Category: Chat

Enablement: `!github.copilot.interactiveSession.disabled`


## `github.copilot.git.resolveMergeConflicts`

**%github.copilot.git.resolveMergeConflicts%**

Category: Chat

Enablement: `!github.copilot.interactiveSession.disabled`


## `github.copilot.devcontainer.generateDevContainerConfig`

**%github.copilot.devcontainer.generateDevContainerConfig%**

Category: Chat


## `github.copilot.tests.fixTestFailure`

**%github.copilot.command.fixTestFailure%**

Category: Chat


## `github.copilot.tests.fixTestFailure.fromInline`

**%github.copilot.command.fixTestFailure%**


## `github.copilot.chat.attachFile`

**%github.copilot.chat.attachFile%**

Category: Chat


## `github.copilot.chat.attachSelection`

**%github.copilot.chat.attachSelection%**

Category: Chat


## `github.copilot.debug.collectDiagnostics`

**%github.copilot.command.collectDiagnostics%**

Category: Developer


## `github.copilot.debug.inlineEdit.clearCache`

**%github.copilot.command.inlineEdit.clearCache%**

Category: Developer


## `github.copilot.debug.inlineEdit.reportNotebookNESIssue`

**%github.copilot.command.inlineEdit.reportNotebookNESIssue%**

Category: Developer

Enablement: `config.github.copilot.chat.advanced.notebook.alternativeNESFormat.enabled || github.copilot.chat.enableEnhancedNotebookNES`


## `github.copilot.debug.generateSTest`

**%github.copilot.command.generateSTest%**

Category: Developer

Enablement: `github.copilot.debugReportFeedback`


## `github.copilot.open.walkthrough`

**%github.copilot.command.openWalkthrough%**

Category: Chat


## `github.copilot.debug.generateInlineEditTests`

**Generate Inline Edit Tests**

Category: Chat

Enablement: `resourceScheme == 'ccreq'`


## `github.copilot.buildLocalWorkspaceIndex`

**%github.copilot.command.buildLocalWorkspaceIndex%**

Category: Chat

Enablement: `github.copilot-chat.activated`


## `github.copilot.buildRemoteWorkspaceIndex`

**%github.copilot.command.buildRemoteWorkspaceIndex%**

Category: Chat

Enablement: `github.copilot-chat.activated`


## `github.copilot.report`

**Report Issue**

Category: Chat


## `github.copilot.chat.rerunWithCopilotDebug`

**%github.copilot.command.rerunWithCopilotDebug%**

Category: Chat


## `github.copilot.chat.startCopilotDebugCommand`

**Start Copilot Debug**


## `github.copilot.chat.clearTemporalContext`

**Clear Temporal Context**

Category: Developer


## `github.copilot.search.markHelpful`

**Helpful**

Enablement: `!github.copilot.search.feedback.sent`


## `github.copilot.search.markUnhelpful`

**Unhelpful**

Enablement: `!github.copilot.search.feedback.sent`


## `github.copilot.search.feedback`

**Feedback**

Enablement: `!github.copilot.search.feedback.sent`


## `github.copilot.chat.debug.showElements`

**Show Rendered Elements**


## `github.copilot.chat.debug.hideElements`

**Hide Rendered Elements**


## `github.copilot.chat.debug.showTools`

**Show Tools**


## `github.copilot.chat.debug.hideTools`

**Hide Tools**


## `github.copilot.chat.debug.showNesRequests`

**Show NES Requests**


## `github.copilot.chat.debug.hideNesRequests`

**Hide NES Requests**


## `github.copilot.chat.debug.showRawRequestBody`

**Show Raw Request Body**


## `github.copilot.chat.debug.exportLogItem`

**Export as...**


## `github.copilot.chat.debug.exportPromptArchive`

**Export All as Archive...**


## `github.copilot.chat.debug.exportPromptLogsAsJson`

**Export All as JSON...**


## `github.copilot.chat.debug.exportAllPromptLogsAsJson`

**Export All Prompt Logs as JSON...**


## `github.copilot.chat.showAsChatSession`

**Show as chat session**


## `github.copilot.debug.collectWorkspaceIndexDiagnostics`

**%github.copilot.command.collectWorkspaceIndexDiagnostics%**

Category: Developer


## `github.copilot.chat.mcp.setup.check`

**MCP Check: is supported**


## `github.copilot.chat.mcp.setup.validatePackage`

**MCP Check: validate package**


## `github.copilot.chat.mcp.setup.flow`

**MCP Check: do prompts**


## `github.copilot.chat.generateAltText`

**Generate/Refine Alt Text**


## `github.copilot.chat.notebook.enableFollowCellExecution`

**Enable Follow Cell Execution from Chat**


## `github.copilot.chat.notebook.disableFollowCellExecution`

**Disable Follow Cell Execution from Chat**


## `github.copilot.chat.manageBYOK`

**Manage Bring Your Own Key Vendor**

Enablement: `false`


## `github.copilot.chat.manageBYOKAPIKey`

**Manage Bring Your Own Key API Key**

Enablement: `false`


## `github.copilot.cloud.sessions.refresh`

**%github.copilot.command.refreshAgentSessions%**


## `github.copilot.cloud.resetWorkspaceConfirmations`

**%github.copilot.command.resetCloudAgentWorkspaceConfirmations%**


## `github.copilot.cloud.sessions.openInBrowser`

**%github.copilot.command.openCopilotAgentSessionsInBrowser%**


## `github.copilot.cloud.sessions.proxy.closeChatSessionPullRequest`

**%github.copilot.command.closeChatSessionPullRequest.title%**


## `github.copilot.chat.openSuggestionsPanel`

**Open Completions Panel**

Category: GitHub Copilot

Enablement: `github.copilot.extensionUnification.activated && !isWeb`


## `github.copilot.chat.toggleStatusMenu`

**Open Status Menu**

Category: GitHub Copilot

Enablement: `github.copilot.extensionUnification.activated`


## `github.copilot.chat.completions.disable`

**Disable Inline Suggestions**

Category: GitHub Copilot

Enablement: `github.copilot.extensionUnification.activated && github.copilot.activated && config.editor.inlineSuggest.enabled && github.copilot.completions.enabled`


## `github.copilot.chat.completions.enable`

**Enable Inline Suggestions**

Category: GitHub Copilot

Enablement: `github.copilot.extensionUnification.activated && github.copilot.activated && !(config.editor.inlineSuggest.enabled && github.copilot.completions.enabled)`


## `github.copilot.chat.completions.toggle`

**Toggle (Enable/Disable) Inline Suggestions**

Category: GitHub Copilot

Enablement: `github.copilot.extensionUnification.activated && github.copilot.activated`


## `github.copilot.chat.openModelPicker`

**Change Completions Model**

Category: GitHub Copilot

Enablement: `github.copilot.extensionUnification.activated && !isWeb`


## `github.copilot.chat.applyCopilotCLIAgentSessionChanges`

**%github.copilot.command.applyCopilotCLIAgentSessionChanges%**

Category: GitHub Copilot


