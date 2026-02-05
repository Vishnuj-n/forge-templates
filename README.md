# Forge Templates

Official template collection for **Forge CLI**. These templates are used to scaffold new projects with predefined structure, commands, and safe file modifications.

---

## Table of Contents

1. [Overview](#overview)
2. [Repository Structure](#repository-structure)
3. [Using Templates](#using-templates)
4. [Template Resolution Order](#template-resolution-order)
5. [Editing Templates](#editing-templates)
6. [Creating New Templates](#creating-new-templates)
7. [Contributing Templates](#contributing-templates)
8. [Versioning](#versioning)
9. [Learn More](#learn-more)
10. [License](#license)

---

## Overview

Forge templates are reusable project blueprints. Each template can:

* Run initialization commands (e.g., `git init`)
* Copy predefined files into new projects
* Append safe patches to existing files
* Provide documentation and setup guidance

Templates allow developers to quickly bootstrap projects with consistent setup and configuration.

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

### template.yaml

Defines template behavior including commands and file operations.

### files/

Contains files and directories copied into generated projects.

### patches/

Contains append-only patches applied to existing project files.

### README.md

Explains the purpose and usage of the template.

---

## Using Templates

Templates in this repository are used with the Forge CLI.

### Pull a Template

```
forge pull <template-name>
```

### Create a Project

```
forge init <template-name> <project-directory>
```

### List Installed Templates

```
forge list
```

---

## Template Resolution Order

When running commands like `forge init` or `forge list`, Forge searches for templates in the following order:

### 1. Project-local Templates

```
./templates/<template-name>
```

Templates stored inside the current project directory.

---

### 2. Environment Variable Templates

```
$FORGE_TEMPLATES/<template-name>
```

If the `FORGE_TEMPLATES` environment variable is set, Forge searches this directory.

---

### 3. Global Templates

```
%USERPROFILE%\.forge\templates\<template-name>
```

Default global template storage.

---

Forge uses the **first matching template** found. This allows project-specific overrides and shared template directories.

---

## Editing Templates

You can edit installed templates locally.

### Step 1 — Navigate to Template Directory

Global templates are stored at:

```
%USERPROFILE%\.forge\templates
```

Open Command Prompt or PowerShell and run:

```
cd %USERPROFILE%\.forge\templates\<template-name>
```

---

### Step 2 — Open Template in VS Code

If Visual Studio Code is installed:

```
code .
```

---

### Step 3 — Modify Template Files

You can edit:

* `template.yaml` → Template behavior
* `files/` → Files copied into projects
* `patches/` → Append-only patches

---

### Step 4 — Test Template Changes

```
forge test <template-name>
```

---

## Creating New Templates

You can scaffold new templates using Forge:

```
forge new <template-name>
```

After creation, edit:

* `template.yaml` to define commands and file operations
* `files/` to include project files
* `patches/` to define append patches

---

## Contributing Templates

Contributions are welcome.

### Guidelines

* Keep templates deterministic and reproducible
* Avoid destructive commands
* Include clear documentation in template README files
* Ensure templates pass testing

---

### Testing Templates

```
forge test templates/<template-name>
```

---

## Versioning

Templates evolve independently from the Forge CLI. Pull templates regularly to receive updates and improvements.

---

## Learn More

See the main Forge CLI repository for:

* Full CLI documentation
* Template engine details
* Advanced configuration
* Usage examples

---

## License

Templates follow the same license as the Forge project unless stated otherwise.
