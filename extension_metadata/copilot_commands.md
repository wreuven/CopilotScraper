# GitHub Copilot - Commands Reference

Version: 1.388.0

Total commands: 19

---

## `github.copilot.toggleStatusMenu`

**Open Status Menu**

Category: GitHub Copilot


## `github.copilot.signIn`

**Sign In**

Category: GitHub Copilot

Enablement: `!github.copilot.activated`


## `github.copilot.acceptCursorPanelSolution`

**Accept Panel Suggestion at the Cursor**

Category: GitHub Copilot

Enablement: `github.copilot.panelVisible`


## `github.copilot.previousPanelSolution`

**Navigate to the Previous Panel Suggestion**

Category: GitHub Copilot

Enablement: `github.copilot.panelVisible`


## `github.copilot.nextPanelSolution`

**Navigate to the Next Panel Suggestion**

Category: GitHub Copilot

Enablement: `github.copilot.panelVisible`


## `github.copilot.generate`

**Open Completions Panel**

Category: GitHub Copilot

Enablement: `github.copilot.activated && !isWeb`


## `github.copilot.generateComparison`

**Open Comparison Panel**

Category: GitHub Copilot

Enablement: `github.copilot.activated && !isWeb && github.copilot.comparisonPanelEnabled`


## `github.copilot.acceptCursorComparisonPanelSolution`

**Accept Comparison Panel Suggestion at the Cursor**

Category: GitHub Copilot

Enablement: `github.copilot.comparisonPanelVisible && github.copilot.comparisonPanelEnabled`


## `github.copilot.previousComparisonPanelSolution`

**Navigate to the Previous Comparison Panel Suggestion**

Category: GitHub Copilot

Enablement: `github.copilot.comparisonPanelVisible && github.copilot.comparisonPanelEnabled`


## `github.copilot.nextComparisonPanelSolution`

**Navigate to the Next Comparison Panel Suggestion**

Category: GitHub Copilot

Enablement: `github.copilot.comparisonPanelVisible && github.copilot.comparisonPanelEnabled`


## `github.copilot.completions.disable`

**Disable Completions**

Category: GitHub Copilot

Enablement: `github.copilot.activated && config.editor.inlineSuggest.enabled && github.copilot.completions.enabled`


## `github.copilot.completions.enable`

**Enable Completions**

Category: GitHub Copilot

Enablement: `github.copilot.activated && !(config.editor.inlineSuggest.enabled && github.copilot.completions.enabled)`


## `github.copilot.completions.toggle`

**Toggle (Enable/Disable) Completions**

Category: GitHub Copilot

Enablement: `github.copilot.activated`


## `github.copilot.sendFeedback`

**Send Feedback**

Category: GitHub Copilot


## `github.copilot.collectDiagnostics`

**Collect Diagnostics**

Category: GitHub Copilot

Enablement: `!isWeb`


## `github.copilot.openLogs`

**Open Logs**

Category: GitHub Copilot


## `github.copilot.openModelPicker`

**Change Completions Model**

Category: GitHub Copilot

Enablement: `!isWeb`


## `github.copilot.sendCompletionFeedback`

**Send Copilot Completion Feedback**

Category: GitHub Copilot

Enablement: `!isWeb`


## `github-copilot-completions-debugger-view.refresh`

**Refresh**


