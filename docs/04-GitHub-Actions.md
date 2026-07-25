# GitHub Actions (CI Pipeline)

## Purpose

GitHub Actions automates project tasks whenever code is pushed to GitHub.

Instead of running tests and checks manually, GitHub Actions executes them automatically.

---

## Problem

Without automation, every developer must manually:

- Install dependencies
- Run the application
- Execute tests
- Check for errors

This process is repetitive and can lead to mistakes.

GitHub Actions solves this by running these tasks automatically.

---

## Developer Thinking

Every time new code is pushed:

1. Download the latest code.
2. Set up Python.
3. Install required packages.
4. Run the application checks.
5. Report success or failure.

---

## Workflow File

```yaml
name: CI Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install Dependencies
        run: |
          pip install -r requirements.txt

      - name: Verify Application
        run: |
          python -m py_compile app/app.py
```

---

## Code Explanation

### Workflow Name

```yaml
name: CI Pipeline
```

This is the name displayed in the GitHub Actions page.

---

### Trigger

```yaml
on:
  push:
```

Starts the workflow whenever code is pushed to the repository.

---

### Branch

```yaml
branches:
  - main
```

Runs the workflow only for the `main` branch.

---

### Job

```yaml
jobs:
```

A workflow can contain one or more jobs.

Each job performs a specific task.

---

### Runner

```yaml
runs-on: ubuntu-latest
```

GitHub creates a temporary Ubuntu virtual machine to execute the workflow.

---

### Checkout Repository

```yaml
uses: actions/checkout@v4
```

Downloads the repository code into the runner.

Without this step, the workflow cannot access project files.

---

### Setup Python

```yaml
uses: actions/setup-python@v5
```

Installs Python inside the GitHub runner.

---

### Python Version

```yaml
python-version: "3.11"
```

Specifies which Python version should be installed.

---

### Install Dependencies

```yaml
pip install -r requirements.txt
```

Installs all required Python packages.

---

### Verify Application

```yaml
python -m py_compile app/app.py
```

Checks whether the Python file contains syntax errors.

If the code contains invalid syntax, the workflow fails.

---

## Execution Flow

```
Developer Pushes Code

        │

        ▼

GitHub Detects Push

        │

        ▼

Create Runner

        │

        ▼

Download Repository

        │

        ▼

Install Python

        │

        ▼

Install Dependencies

        │

        ▼

Verify Application

        │

        ▼

Success / Failure
```

---

## Real-World Usage

Companies use GitHub Actions to:

- Build applications
- Run unit tests
- Execute security scans
- Build Docker images
- Deploy applications
- Send notifications

---

## Best Practices

- Keep workflows small and focused.
- Store secrets in GitHub Secrets.
- Use fixed action versions.
- Separate CI and CD workflows.
- Fail fast when errors occur.

---

## Common Mistakes

- Forgetting to checkout the repository.
- Installing the wrong Python version.
- Hardcoding passwords in workflows.
- Running unnecessary steps.
- Ignoring failed workflow results.

---

## Interview Questions

### What is GitHub Actions?

GitHub Actions is a CI/CD platform that automates software development workflows.

---

### What is a workflow?

A workflow is an automated process defined in a YAML file.

---

### What is a job?

A job is a collection of related steps executed on a runner.

---

### What is a step?

A step is a single task within a job.

---

### What is a runner?

A runner is the machine that executes the workflow.

---

### Why do we use `actions/checkout`?

It downloads the repository so the workflow can access the project files.

---

### What happens if one step fails?

The job stops, and the workflow is marked as failed unless configured otherwise.
