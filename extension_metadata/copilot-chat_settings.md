# GitHub Copilot Chat - Settings Reference

Version: 0.34.2025112801

Total settings: 114

---

## `github.copilot.chat.agent.autoFix`

%github.copilot.config.autoFix%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.agent.currentEditorContext.enabled`

%github.copilot.config.agent.currentEditorContext.enabled%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.agent.delegate.autoCommitAndPush`

%github.copilot.config.agent.delegate.autoCommitAndPush%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.agent.temperature`

%github.copilot.config.agent.temperature%

- **Type**: `['number', 'null']`

## `github.copilot.chat.agentHistorySummarizationForceGpt41`

%github.copilot.config.agentHistorySummarizationForceGpt41%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.agentHistorySummarizationMode`

%github.copilot.config.agentHistorySummarizationMode%

- **Type**: `['string', 'null']`

## `github.copilot.chat.agentHistorySummarizationWithPromptCache`

%github.copilot.config.agentHistorySummarizationWithPromptCache%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.alternateGptPrompt.enabled`

%github.copilot.config.alternateGptPrompt.enabled%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.anthropic.thinking.budgetTokens`

%github.copilot.config.anthropic.thinking.budgetTokens%

- **Type**: `['number', 'null']`

## `github.copilot.chat.anthropic.tools.websearch.allowedDomains`

%github.copilot.config.anthropic.tools.websearch.allowedDomains%

- **Type**: `array`
- **Default**: `[]`

## `github.copilot.chat.anthropic.tools.websearch.blockedDomains`

%github.copilot.config.anthropic.tools.websearch.blockedDomains%

- **Type**: `array`
- **Default**: `[]`

## `github.copilot.chat.anthropic.tools.websearch.enabled`

%github.copilot.config.anthropic.tools.websearch.enabled%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.anthropic.tools.websearch.maxUses`

%github.copilot.config.anthropic.tools.websearch.maxUses%

- **Type**: `number`
- **Default**: `5`

## `github.copilot.chat.anthropic.tools.websearch.userLocation`

%github.copilot.config.anthropic.tools.websearch.userLocation%

- **Type**: `['object', 'null']`
- **Default**: `null`

## `github.copilot.chat.azureAuthType`

%github.copilot.config.azureAuthType%

- **Type**: `string`
- **Default**: `"entraId"`
- **Options**: `entraId`, `apiKey`

## `github.copilot.chat.azureModels`

Configure custom Azure OpenAI models. Each key should be a unique model ID, and the value should be an object with model configuration including name, url, toolCalling, vision, maxInputTokens, and maxOutputTokens properties.

- **Type**: `object`
- **Default**: `{}`

## `github.copilot.chat.byok.ollamaEndpoint`

%github.copilot.config.byok.ollamaEndpoint%

- **Type**: `string`
- **Default**: `"http://localhost:11434"`

## `github.copilot.chat.claudeCode.debug`

%github.copilot.config.claudeCode.debug%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.claudeCode.enabled`

%github.copilot.config.claudeCode.enabled%

- **Type**: `['boolean', 'string']`
- **Default**: `false`

## `github.copilot.chat.cli.customAgents.enabled`

%github.copilot.config.cli.customAgents.enabled%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.cli.isolation.enabled`

%github.copilot.config.cli.isolation.enabled%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.cli.mcp.enabled`

%github.copilot.config.cli.mcp.enabled%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.codeGeneration.instructions`

%github.copilot.config.codeGeneration.instructions%

- **Type**: `array`
- **Default**: `[]`

## `github.copilot.chat.codeGeneration.useInstructionFiles`

%github.copilot.config.codeGeneration.useInstructionFiles%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.codesearch.agent.enabled`

%github.copilot.config.codesearch.agent.enabled%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.codesearch.enabled`

%github.copilot.config.codesearch.enabled%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.commitMessageGeneration.instructions`

%github.copilot.config.commitMessageGeneration.instructions%

- **Type**: `array`
- **Default**: `[]`

## `github.copilot.chat.completionsFetcher`

%github.copilot.config.completionsFetcher%

- **Type**: `['string', 'null']`
- **Options**: `electron-fetch`, `node-fetch`

## `github.copilot.chat.copilotCLI.enabled`

%github.copilot.config.copilotCLI.enabled%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.copilotDebugCommand.enabled`

%github.copilot.chat.copilotDebugCommand.enabled%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.customAgents.showOrganizationAndEnterpriseAgents`

%github.copilot.config.customAgents.showOrganizationAndEnterpriseAgents%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.customInstructionsInSystemMessage`

%github.copilot.config.customInstructionsInSystemMessage%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.customOAIModels`

Configure custom OpenAI-compatible models. Each key should be a unique model ID, and the value should be an object with model configuration including name, url, toolCalling, vision, maxInputTokens, and maxOutputTokens properties.

- **Type**: `object`
- **Default**: `{}`

## `github.copilot.chat.debug.overrideChatEngine`

%github.copilot.config.debug.overrideChatEngine%

- **Type**: `['string', 'null']`

## `github.copilot.chat.debug.requestLogger.maxEntries`

%github.copilot.config.debug.requestLogger.maxEntries%

- **Type**: `number`
- **Default**: `100`

## `github.copilot.chat.debugTerminalCommandPatterns`

%github.copilot.config.debugTerminalCommandPatterns%

- **Type**: `array`
- **Default**: `[]`

## `github.copilot.chat.editRecording.enabled`

%github.copilot.config.editRecording.enabled%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.edits.gemini3MultiReplaceString`

Enable the modern `multi_replace_string_in_file` edit tool when generating edits with Gemini 3 models.

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.edits.gemini3ReplaceStringOnly`

Use only the modern `replace_string_in_file` edit tool when generating edits with Gemini 3 models.

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.edits.suggestRelatedFilesForTests`

%github.copilot.chat.edits.suggestRelatedFilesForTests%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.edits.suggestRelatedFilesFromGitHistory`

%github.copilot.config.edits.suggestRelatedFilesFromGitHistory%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.enableUserPreferences`

%github.copilot.config.enableUserPreferences%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.feedback.onChange`

%github.copilot.config.feedback.onChange%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.generateTests.codeLens`

%github.copilot.config.generateTests.codeLens%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.githubMcpServer.enabled`

%github.copilot.config.githubMcpServer.enabled%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.githubMcpServer.lockdown`

%github.copilot.config.githubMcpServer.lockdown%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.githubMcpServer.readonly`

%github.copilot.config.githubMcpServer.readonly%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.githubMcpServer.toolsets`

%github.copilot.config.githubMcpServer.toolsets%

- **Type**: `array`
- **Default**: `["default"]`

## `github.copilot.chat.gpt5AlternativePatch`

%github.copilot.config.gpt5AlternativePatch%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.imageUpload.enabled`

%github.copilot.config.imageUpload.enabled%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.inlineEdits.diagnosticsContextProvider.enabled`

%github.copilot.config.inlineEdits.diagnosticsContextProvider.enabled%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.inlineEdits.nextCursorPrediction.currentFileMaxTokens`

%github.copilot.config.inlineEdits.nextCursorPrediction.currentFileMaxTokens%

- **Type**: `number`
- **Default**: `2000`

## `github.copilot.chat.inlineEdits.nextCursorPrediction.displayLine`

%github.copilot.config.inlineEdits.nextCursorPrediction.displayLine%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.inlineEdits.renameSymbolSuggestions`

%github.copilot.config.inlineEdits.renameSymbolSuggestions%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.inlineEdits.triggerOnEditorChangeAfterSeconds`

%github.copilot.config.inlineEdits.triggerOnEditorChangeAfterSeconds%

- **Type**: `['number', 'null']`

## `github.copilot.chat.instantApply.shortContextLimit`

%github.copilot.config.instantApply.shortContextLimit%

- **Type**: `number`
- **Default**: `8000`

## `github.copilot.chat.instantApply.shortContextModelName`

%github.copilot.config.instantApply.shortContextModelName%

- **Type**: `string`
- **Default**: `"gpt-4o-instant-apply-full-ft-v66-short"`

## `github.copilot.chat.languageContext.fix.typescript.enabled`

%github.copilot.chat.languageContext.fix.typescript.enabled%

- **Type**: `boolean`
- **Default**: `false`
- **Scope**: resource

## `github.copilot.chat.languageContext.inline.typescript.enabled`

%github.copilot.chat.languageContext.inline.typescript.enabled%

- **Type**: `boolean`
- **Default**: `false`
- **Scope**: resource

## `github.copilot.chat.languageContext.typescript.cacheTimeout`

%github.copilot.chat.languageContext.typescript.cacheTimeout%

- **Type**: `number`
- **Default**: `500`
- **Scope**: resource

## `github.copilot.chat.languageContext.typescript.enabled`

%github.copilot.chat.languageContext.typescript.enabled%

- **Type**: `boolean`
- **Default**: `false`
- **Scope**: resource

## `github.copilot.chat.languageContext.typescript.includeDocumentation`

%github.copilot.chat.languageContext.typescript.includeDocumentation%

- **Type**: `boolean`
- **Default**: `false`
- **Scope**: resource

## `github.copilot.chat.languageContext.typescript.items`

%github.copilot.chat.languageContext.typescript.items%

- **Type**: `string`
- **Default**: `"double"`
- **Options**: `minimal`, `double`, `fillHalf`, `fill`
- **Scope**: resource

## `github.copilot.chat.localWorkspaceRecording.enabled`

%github.copilot.config.localWorkspaceRecording.enabled%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.localeOverride`

%github.copilot.config.localeOverride%

- **Type**: `string`
- **Default**: `"auto"`
- **Options**: `auto`, `en`, `fr`, `it`, `de`, `es`, `ru`, `zh-CN`, `zh-TW`, `ja`, `ko`, `cs`, `pt-br`, `tr`, `pl`

## `github.copilot.chat.nesFetcher`

%github.copilot.config.nesFetcher%

- **Type**: `['string', 'null']`
- **Options**: `electron-fetch`, `node-fetch`

## `github.copilot.chat.newWorkspace.useContext7`

%github.copilot.config.newWorkspace.useContext7%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.newWorkspaceCreation.enabled`

%github.copilot.config.newWorkspaceCreation.enabled%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.notebook.alternativeFormat`

%github.copilot.config.notebook.alternativeFormat%

- **Type**: `string`
- **Default**: `"xml"`
- **Options**: `xml`, `markdown`

## `github.copilot.chat.notebook.alternativeNESFormat.enabled`

%github.copilot.config.notebook.alternativeNESFormat.enabled%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.notebook.enhancedNextEditSuggestions.enabled`

%github.copilot.config.notebook.enhancedNextEditSuggestions%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.notebook.followCellExecution.enabled`

%github.copilot.config.notebook.followCellExecution%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.notebook.summaryExperimentEnabled`

%github.copilot.config.notebook.summaryExperimentEnabled%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.notebook.variableFilteringEnabled`

%github.copilot.config.notebook.variableFilteringEnabled%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.omitBaseAgentInstructions`

%github.copilot.config.omitBaseAgentInstructions%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.projectLabels.chat`

%github.copilot.config.projectLabels.chat%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.projectLabels.expanded`

%github.copilot.config.projectLabels.expanded%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.projectLabels.inline`

%github.copilot.config.projectLabels.inline%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.promptFileContextProvider.enabled`

%github.copilot.config.promptFileContextProvider.enabled%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.pullRequestDescriptionGeneration.instructions`

%github.copilot.config.pullRequestDescriptionGeneration.instructions%

- **Type**: `array`
- **Default**: `[]`

## `github.copilot.chat.responsesApiReasoningEffort`

%github.copilot.config.responsesApiReasoningEffort%

- **Type**: `string`
- **Default**: `"default"`
- **Options**: `low`, `medium`, `high`, `default`

## `github.copilot.chat.responsesApiReasoningSummary`

%github.copilot.config.responsesApiReasoningSummary%

- **Type**: `string`
- **Default**: `"detailed"`
- **Options**: `off`, `detailed`

## `github.copilot.chat.review.intent`

%github.copilot.config.review.intent%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.reviewAgent.enabled`

%github.copilot.config.reviewAgent.enabled%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.reviewSelection.enabled`

%github.copilot.config.reviewSelection.enabled%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.reviewSelection.instructions`

%github.copilot.config.reviewSelection.instructions%

- **Type**: `array`
- **Default**: `[]`

## `github.copilot.chat.scopeSelection`

%github.copilot.config.scopeSelection%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.setupTests.enabled`

%github.copilot.config.setupTests.enabled%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.suggestRelatedFilesFromGitHistory.useEmbeddings`

%github.copilot.config.suggestRelatedFilesFromGitHistory.useEmbeddings%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.summarizeAgentConversationHistory.enabled`

%github.copilot.config.summarizeAgentConversationHistory.enabled%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.summarizeAgentConversationHistoryThreshold`

%github.copilot.config.summarizeAgentConversationHistoryThreshold%

- **Type**: `['number', 'null']`

## `github.copilot.chat.temporalContext.maxAge`

%github.copilot.config.temporalContext.maxAge%

- **Type**: `number`
- **Default**: `100`

## `github.copilot.chat.temporalContext.preferSameLang`

%github.copilot.config.temporalContext.preferSameLang%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.terminalChatLocation`

%github.copilot.config.terminalChatLocation%

- **Type**: `string`
- **Default**: `"chatView"`
- **Options**: `chatView`, `quickChat`, `terminal`

## `github.copilot.chat.testGeneration.instructions`

%github.copilot.config.testGeneration.instructions%

- **Type**: `array`
- **Default**: `[]`

## `github.copilot.chat.tools.defaultToolsGrouped`

%github.copilot.config.tools.defaultToolsGrouped%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.tools.memory.enabled`

%github.copilot.config.tools.memory.enabled%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.useProjectTemplates`

%github.copilot.config.useProjectTemplates%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.useResponsesApi`

%github.copilot.config.useResponsesApi%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.useResponsesApiTruncation`

%github.copilot.config.useResponsesApiTruncation%

- **Type**: `boolean`
- **Default**: `false`

## `github.copilot.chat.virtualTools.threshold`

%github.copilot.config.virtualTools.threshold%

- **Type**: `number`
- **Default**: `128`

## `github.copilot.chat.workspace.enableCodeSearch`

%github.copilot.config.workspace.enableCodeSearch%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.workspace.enableEmbeddingsSearch`

%github.copilot.config.workspace.enableEmbeddingsSearch%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.workspace.enableFullWorkspace`

%github.copilot.config.workspace.enableFullWorkspace%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.chat.workspace.maxLocalIndexSize`

%github.copilot.config.workspace.maxLocalIndexSize%

- **Type**: `number`
- **Default**: `100000`

## `github.copilot.chat.workspace.preferredEmbeddingsModel`

%github.copilot.config.workspace.preferredEmbeddingsModel%

- **Type**: `string`
- **Default**: `""`

## `github.copilot.chat.workspace.prototypeAdoCodeSearchEndpointOverride`

%github.copilot.config.workspace.prototypeAdoCodeSearchEndpointOverride%

- **Type**: `string`
- **Default**: `""`

## `github.copilot.editor.enableCodeActions`

%github.copilot.config.enableCodeActions%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.enable`

Enable or disable auto triggering of Copilot completions for specified [languages](https://code.visualstudio.com/docs/languages/identifiers). You can still trigger suggestions manually using `Alt + \`

- **Type**: `object`
- **Default**: `{"*": true, "plaintext": false, "markdown": false, "scminput": false}`
- **Scope**: window

## `github.copilot.nextEditSuggestions.allowWhitespaceOnlyChanges`

%github.copilot.nextEditSuggestions.allowWhitespaceOnlyChanges%

- **Type**: `boolean`
- **Default**: `true`
- **Scope**: language-overridable

## `github.copilot.nextEditSuggestions.enabled`

%github.copilot.nextEditSuggestions.enabled%

- **Type**: `boolean`
- **Default**: `false`
- **Scope**: language-overridable

## `github.copilot.nextEditSuggestions.fixes`

%github.copilot.nextEditSuggestions.fixes%

- **Type**: `boolean`
- **Default**: `true`
- **Scope**: language-overridable

## `github.copilot.renameSuggestions.triggerAutomatically`

%github.copilot.config.renameSuggestions.triggerAutomatically%

- **Type**: `boolean`
- **Default**: `true`

## `github.copilot.selectedCompletionModel`

The currently selected completion model ID. To select from a list of available models, use the __"Change Completions Model"__ command or open the model picker (from the Copilot menu in the VS Code title bar, select __"Configure Code Completions"__ then __"Change Completions Model"__. The value must be a valid model ID. An empty value indicates that the default model will be used.

- **Type**: `string`
- **Default**: `""`

