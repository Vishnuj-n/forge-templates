# Template: my-first-template

## Overview

This is a Forge template for bootstrapping my-first-template projects.

## What This Template Does

1. Initializes a git repository
2. Copies template files
3. Applies custom patches

## Getting Started

### Edit the template

1. template.yaml — Define commands and file operations
2. files/ — Add files/directories to copy into projects
3. patches/ — Add content to append to existing files

### Test the template

Run: forge test templates/my-first-template

### Use the template

Run: forge init templates/my-first-template ./my-project

## Prerequisites

- Git (for git init commands)
- Any other tools used in the commands section

## Customization

### Add files to copy
1. Add files to the files/ directory
2. In template.yaml, add to files.copy:
   copy:
     - files/README.md
     - files/config.json

### Add append patches
1. Create patch files in patches/
2. In template.yaml, add to files.append:
   append:
     - target: ".gitignore"
       source: "patches/gitignore.append"

### Add commands
In template.yaml, add to the commands section:
commands:
  - cmd: ["git", "init"]
  - cmd: ["echo", "Hello from template!"]

## Tips

- Commands are executed in token-array format (no shell strings)
- Target files for append operations must be created by commands or copy operations
- Use forge test to debug templates without committing
- Keep commands simple and deterministic

# Forge Template Guide (Short)

Templates are folders that include a `template.yaml` and optional `files/`, `patches/`, and `README.md`.

Minimum required: `template.yaml` with `name`.

Short example:

```yaml
name: example
description: "Short description"
version: "1.0.0"

commands:
  - cmd: ["git", "init"]

files:
  copy:
    - files/README.md
  append:
    - target: ".gitignore"
      source: "patches/gitignore.append"
```

Quick rules:

- `name` is required.
- `cmd` is an array of tokens (no shell strings).
- Use `interactive: true` for commands that prompt; add `test_cmd` for non-interactive test runs.
- `files.copy` paths are relative to the template and must exist when used.
- `files.append.source` is relative to the template and `target` must exist in the project.

Testing and troubleshooting:

- `forge test <template>` runs commands in a temp workspace (non-interactive). Interactive steps are replaced by `test_cmd` or skipped.
- "target file not found" → ensure the file exists before appending.

Keep templates small, documented, and testable.

## For More Information

See the main Forge documentation:
- README.md — Project overview
- TEMPLATE-GUIDE.md — Complete template guide
