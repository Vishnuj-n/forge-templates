# Forge Templates

Official template collection for the Forge CLI. Templates scaffold new projects with predefined structure, commands, and safe file modifications.

---

## Table of Contents

1. Overview
2. Repository Structure
3. Using Templates
4. Template Resolution Order
5. Editing Templates
6. Creating New Templates
7. Contributing Templates
8. Versioning
9. Learn More
10. License

---

## Overview

Forge templates are reusable project blueprints. Each template can:
- Run initialization commands (e.g., `git init`)
- Copy predefined files into new projects
- Apply append-only patches to existing files
- Provide documentation and setup guidance

Templates let developers quickly bootstrap projects with consistent setup and configuration.

---

## Quick Guide

- Templates must include a `template.yaml` with at least a `name` field.
- Optional fields: `description`, `version` (e.g., `0.1.0`).
- Use token-array `cmd` entries (array of strings; do not use a shell string).
- Use `files.copy` to add files, and `files.append` to patch existing files.
- Test templates locally with: `forge test <template-path-or-name>`.

Interactive example:

```yaml
commands:
   - cmd: ["npm", "init"]
      interactive: true
      test_cmd: ["npm", "init", "-y"]
```

- `interactive: true` marks a command that prompts the user; `test_cmd` provides a non-interactive substitute used by `forge test`.

---

## Repository Structure

```
templates/
 ├── <template-name>/
 │   ├── template.yaml
 │   ├── README.md
 │   ├── files/
 │   └── patches/
```

- `template.yaml`: Defines template behavior (commands, file ops).
- `files/`: Files and directories copied into generated projects.
- `patches/`: Append-only patches applied to existing project files.
- `README.md`: Usage and purpose for the template.

---

## Using Templates

Pull a template (from remote templates repo) with:

```
forge pull <template-name>
```

Create a new project from a template:

```
forge init <template-name> <project-directory>
```

List installed templates:

```
forge list
```

Test a template locally (recommended after edits):

```
forge test <template-path-or-name>
```

(You can pass a path like `templates/<template-name>` or an installed template name.)

---

## Template Resolution Order

When locating templates, Forge searches in this order (first match wins):

1. Project-local templates
   - `./templates/<template-name>`
2. Environment variable directory
   - `$FORGE_TEMPLATES/<template-name>`  (on Windows PowerShell use `%USERPROFILE%\.forge\templates` or set `FORGE_TEMPLATES` accordingly)
3. Global templates
   - `%USERPROFILE%\.forge\templates` on Windows
   - `$HOME/.forge/templates` on Unix-like systems

---

## Editing Templates

1. Navigate to the template directory:
   - Windows PowerShell:
     ```
     cd $env:USERPROFILE\.forge\templates\<template-name>
     ```
   - Unix/macOS:
     ```
     cd ~/.forge/templates/<template-name>
     ```
2. Open in editor:
   ```
   code .
   ```
3. Modify `template.yaml`, `files/`, and `patches/`.
4. Test changes:
   ```
   forge test <template-path-or-name>
   ```

---

## Creating New Templates

Scaffold a new template:

```
forge new <template-name>
```

Then edit:
- `template.yaml` to define commands and file operations
- `files/` to include project files
- `patches/` to define append patches

Example `template.yaml` (minimal):

```yaml
name: example-template
description: "A minimal example template"
version: "0.1.0"

cmd:
  - ["git", "init"]
  - ["go", "mod", "init", "example.com/myproject"]

files:
  copy:
    - src/main.go: files/main.go

files:
  append:
    - README.md: patches/README_add.txt
```

Notes:
- `cmd` entries are arrays of tokens: `["git","init"]` (not a shell string).
- `files.copy` maps destination to a source path inside the template.
- `files.append` maps destination to a patch file that will be appended.

---

## Contributing Templates

Guidelines:
- Keep templates deterministic and reproducible.
- Avoid destructive commands (do not delete user files).
- Include clear documentation in the template `README.md`.
- Ensure templates pass local testing (`forge test`).

Testing locally:

```
forge test templates/<template-name>
```

---

## Versioning

Templates are versioned independently from the Forge CLI. Pull templates regularly to receive updates.

---

## Learn More

See the main Forge CLI repository for:
- Full CLI documentation
- Template engine details
- Advanced configuration and examples

---

## License

Templates use the same license as the Forge project unless otherwise stated.
