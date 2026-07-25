# Trivy Security Scanner

## Purpose

Trivy is a security scanner that detects vulnerabilities in:

- Docker images
- Operating system packages
- Application dependencies
- Configuration files
- Infrastructure as Code (IaC)

It helps identify security issues before deploying an application.

---

## Problem

Applications often use many third-party packages.

Example:

Application

↓

Flask

↓

Werkzeug

↓

Jinja2

↓

Other Libraries

If any library contains a known vulnerability, attackers may exploit it.

Checking every dependency manually is impossible.

Trivy automates this process.

---

## Developer Thinking

Before deploying the application:

1. Scan the project.
2. Find security vulnerabilities.
3. Generate a report.
4. Fix issues before deployment.

---

## Workflow

```yaml
name: Trivy Security Scan

on:
  push:
    branches:
      - main

jobs:
  trivy:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v4

      - name: Run Trivy

        uses: aquasecurity/trivy-action@master

        with:
          scan-type: fs
          scan-ref: .
```

---

## Code Explanation

### Workflow Name

```yaml
name: Trivy Security Scan
```

Displays the workflow name in GitHub Actions.

---

### Trigger

```yaml
on:
  push:
```

Runs the security scan whenever code is pushed.

---

### Runner

```yaml
runs-on: ubuntu-latest
```

Creates a temporary Ubuntu machine for scanning.

---

### Checkout Repository

```yaml
uses: actions/checkout@v4
```

Downloads the project code.

Without this step, Trivy cannot scan the repository.

---

### Trivy Action

```yaml
uses: aquasecurity/trivy-action@master
```

Runs the official Trivy GitHub Action.

---

### Scan Type

```yaml
scan-type: fs
```

`fs` means **File System Scan**.

Trivy scans the project directory.

---

### Scan Reference

```yaml
scan-ref: .
```

`.` refers to the current project directory.

Everything inside the repository is scanned.

---

## Execution Flow

```
Developer Pushes Code

        │

        ▼

GitHub Actions

        │

        ▼

Download Repository

        │

        ▼

Run Trivy

        │

        ▼

Scan Project Files

        │

        ▼

Generate Report

        │

        ▼

Pass / Fail
```

---

## What Does Trivy Detect?

- High vulnerabilities
- Critical vulnerabilities
- Vulnerable dependencies
- Misconfigurations
- Secrets (optional)
- Infrastructure security issues

---

## Real-World Usage

Companies use Trivy to:

- Scan Docker images
- Scan Kubernetes manifests
- Scan Terraform code
- Scan Git repositories
- Scan CI/CD pipelines

---

## Best Practices

- Run Trivy in every CI pipeline.
- Fix Critical vulnerabilities immediately.
- Keep dependencies updated.
- Scan Docker images before deployment.
- Review reports regularly.

---

## Common Mistakes

- Ignoring High and Critical vulnerabilities.
- Using outdated dependencies.
- Scanning only Docker images.
- Running security scans only before production.
- Not updating Trivy.

---

## Interview Questions

### What is Trivy?

Trivy is an open-source security scanner used to detect vulnerabilities in containers, dependencies, repositories, and Infrastructure as Code.

---

### Why is Trivy used?

It helps identify security issues before deploying an application.

---

### What does `scan-type: fs` mean?

It scans the project files stored in the repository.

---

### Can Trivy scan Docker images?

Yes.

It can scan Docker images, repositories, Kubernetes manifests, Terraform files, and more.

---

### Why run Trivy in GitHub Actions?

It automatically checks every code change for security vulnerabilities before deployment.
