# GitHub Copilot - Settings Reference

Version: 1.388.0

Total settings: 3

---

## `github.copilot.advanced`

No description

- **Type**: `object`

## `github.copilot.enable`

Enable or disable auto triggering of Copilot completions for specified [languages](https://code.visualstudio.com/docs/languages/identifiers). You can still trigger suggestions manually using `Alt + \`

- **Type**: `object`
- **Default**: `{"*": true, "plaintext": false, "markdown": false, "scminput": false}`
- **Scope**: window

## `github.copilot.selectedCompletionModel`

The currently selected completion model ID. To select from a list of available models, use the __"Change Completions Model"__ command or open the model picker (from the Copilot menu in the VS Code title bar, select __"Configure Code Completions"__ then __"Change Completions Model"__. The value must be a valid model ID. An empty value indicates that the default model will be used.

- **Type**: `string`
- **Default**: `""`

