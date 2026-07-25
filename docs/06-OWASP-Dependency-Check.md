# OWASP Dependency Check

## Purpose

OWASP Dependency Check is a Software Composition Analysis (SCA) tool.

It scans third-party libraries used in an application and detects known security vulnerabilities.

The tool compares project dependencies against the National Vulnerability Database (NVD).

---

## Problem

Modern applications use many external libraries.

Example:

Application

↓

Flask

↓

Jinja2

↓

Werkzeug

↓

Click

↓

ItsDangerous

If one library contains a security vulnerability, the application may become vulnerable.

Checking every library manually is not practical.

OWASP Dependency Check automates this process.

---

## Developer Thinking

Before deploying the application:

1. Identify all project dependencies.
2. Compare them with known vulnerabilities.
3. Generate a security report.
4. Fix vulnerable libraries before deployment.

---

## Workflow

```yaml
name: OWASP Dependency Check

on:
  push:
    branches:
      - main

jobs:
  dependency-check:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v4

      - name: Run OWASP Dependency Check

        uses: dependency-check/Dependency-Check_Action@main

        with:
          project: Multi-Cloud-DevSecOps
          path: .
          format: HTML
```

---

## Code Explanation

### Workflow Name

```yaml
name: OWASP Dependency Check
```

Displays the workflow name in GitHub Actions.

---

### Trigger

```yaml
on:
  push:
```

Runs the scan whenever code is pushed.

---

### Runner

```yaml
runs-on: ubuntu-latest
```

Creates a temporary Ubuntu virtual machine.

---

### Checkout Repository

```yaml
uses: actions/checkout@v4
```

Downloads the project source code.

---

### Dependency Check Action

```yaml
uses: dependency-check/Dependency-Check_Action@main
```

Runs the OWASP Dependency Check GitHub Action.

---

### Project Name

```yaml
project: Multi-Cloud-DevSecOps
```

Specifies the project name shown in the generated report.

---

### Scan Path

```yaml
path: .
```

Scans the current project directory.

---

### Report Format

```yaml
format: HTML
```

Generates the security report in HTML format.

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

Identify Dependencies

        │

        ▼

Compare with NVD

        │

        ▼

Generate Security Report

        │

        ▼

Pass / Fail
```

---

## What Does It Detect?

- Vulnerable libraries
- Known CVEs
- Outdated dependencies
- Dependency security risks

---

## Trivy vs OWASP Dependency Check

| Trivy | OWASP Dependency Check |
|-------|-------------------------|
| Scans containers, repositories, IaC, and dependencies | Focuses mainly on third-party libraries |
| Detects vulnerabilities in multiple targets | Performs detailed dependency analysis |
| Fast scanning | Deep dependency analysis |

Using both tools provides better security coverage.

---

## Real-World Usage

Companies use OWASP Dependency Check to:

- Scan open-source libraries
- Detect vulnerable dependencies
- Generate compliance reports
- Improve application security
- Integrate security into CI/CD pipelines

---

## Best Practices

- Run dependency scans in every CI pipeline.
- Update vulnerable libraries regularly.
- Review reports after every scan.
- Remove unused dependencies.
- Keep dependency versions up to date.

---

## Common Mistakes

- Ignoring vulnerability reports.
- Using outdated libraries.
- Keeping unused dependencies.
- Running scans only before production.
- Not updating dependencies regularly.

---

## Interview Questions

### What is OWASP Dependency Check?

It is an open-source Software Composition Analysis (SCA) tool that identifies known vulnerabilities in project dependencies.

---

### Why is it used?

It helps detect insecure third-party libraries before deployment.

---

### What database does it use?

It primarily uses the National Vulnerability Database (NVD) to identify known CVEs.

---

### Why use OWASP Dependency Check if Trivy is already used?

Trivy provides broad security scanning, while OWASP Dependency Check performs deeper analysis of application dependencies.

Using both tools improves overall security.

---

### What is a CVE?

A CVE (Common Vulnerabilities and Exposures) is a publicly documented security vulnerability with a unique identifier.
