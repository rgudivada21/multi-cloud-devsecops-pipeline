# Interview Questions and Answers

## Project Overview

### 1. Explain your project.

This project demonstrates a complete Multi-Cloud DevSecOps pipeline.

The application is built using Flask, containerized with Docker, automated using GitHub Actions, secured using Trivy and OWASP Dependency Check, infrastructure is managed using Terraform, deployed using Kubernetes, monitored using Prometheus, and visualized using Grafana.

---

### 2. Why did you choose this project?

This project covers the complete DevSecOps lifecycle using modern tools that are widely used in the industry.

---

### 3. Which technologies are used?

- Python (Flask)
- Docker
- Docker Compose
- GitHub Actions
- Trivy
- OWASP Dependency Check
- Terraform
- Kubernetes
- Prometheus
- Grafana

---

# Flask

### 4. Why did you use Flask?

Flask is a lightweight Python framework used to build web applications and REST APIs.

---

### 5. What happens when a user opens the application?

The browser sends a request to Flask.

Flask matches the request with the route, executes the function, and returns the response.

---

# Docker

### 6. Why did you use Docker?

Docker packages the application with all its dependencies so it runs consistently across different environments.

---

### 7. What is the difference between an Image and a Container?

Image:

- Blueprint
- Read-only

Container:

- Running instance of an image

---

### 8. Why is Docker better than installing everything manually?

Docker provides a consistent environment, simplifies deployment, and avoids dependency conflicts.

---

### 9. Why not use a Virtual Machine instead?

Virtual Machines include a complete operating system, making them larger and slower to start.

Docker containers share the host operating system, making them lightweight and faster.

---

# Docker Compose

### 10. Why is Docker Compose used?

Docker Compose manages multiple containers using one configuration file.

---

### 11. What problem does Docker Compose solve?

It starts multiple services together and automatically creates networking between them.

---

# GitHub Actions

### 12. What is GitHub Actions?

GitHub Actions is a CI/CD platform used to automate software development workflows.

---

### 13. What happens when code is pushed?

GitHub automatically starts the workflow, installs dependencies, runs validation, and executes security scans.

---

### 14. What is a Runner?

A Runner is the machine that executes the workflow.

---

# Trivy

### 15. Why is Trivy used?

Trivy scans containers, repositories, dependencies, and Infrastructure as Code for security vulnerabilities.

---

### 16. What is a vulnerability?

A vulnerability is a weakness that attackers can exploit.

---

# OWASP Dependency Check

### 17. Why use OWASP Dependency Check?

It detects known vulnerabilities in third-party libraries.

---

### 18. Why use both Trivy and OWASP?

Trivy provides broad security scanning, while OWASP Dependency Check focuses on dependency analysis.

Using both provides better security coverage.

---

# Terraform

### 19. What is Terraform?

Terraform is an Infrastructure as Code tool used to create and manage cloud resources.

---

### 20. Why use Infrastructure as Code?

Infrastructure becomes repeatable, version-controlled, and easier to maintain.

---

### 21. What is a Provider?

A Provider connects Terraform to cloud platforms such as AWS, Azure, or GCP.

---

### 22. What is a Variable?

A Variable allows values to be reused without modifying the Terraform configuration.

---

### 23. What is an Output?

An Output displays useful information after Terraform completes.

---

# Kubernetes

### 24. Why is Kubernetes used?

Kubernetes manages containers automatically by providing scaling, self-healing, and load balancing.

---

### 25. What is a Pod?

A Pod is the smallest deployable unit in Kubernetes.

---

### 26. What is a Deployment?

A Deployment manages Pods and ensures the required number of replicas are always running.

---

### 27. What is a Service?

A Service provides stable network access to Pods.

---

### 28. Why are replicas used?

Replicas improve availability and reliability by running multiple copies of the application.

---

### 29. What happens if one Pod crashes?

Kubernetes automatically creates a new Pod to maintain the desired number of replicas.

---

# Prometheus

### 30. What is Prometheus?

Prometheus collects and stores monitoring metrics.

---

### 31. What are metrics?

Metrics are numerical values such as CPU usage, memory usage, request count, and response time.

---

# Grafana

### 32. What is Grafana?

Grafana displays monitoring data using dashboards and graphs.

---

### 33. Does Grafana collect metrics?

No.

Grafana visualizes data collected by tools such as Prometheus.

---

# Security

### 34. Why is security integrated into CI?

Security issues are detected early before deployment.

---

### 35. What is a CVE?

A CVE (Common Vulnerabilities and Exposures) is a publicly documented security vulnerability with a unique identifier.

---

# Scenario-Based Questions

### 36. A Docker container stops unexpectedly. What happens?

If managed by Kubernetes, Kubernetes automatically creates a replacement Pod.

---

### 37. Why not deploy directly without CI?

CI automatically validates code and detects issues before deployment, reducing manual errors.

---

### 38. Why scan dependencies before deployment?

To identify known vulnerabilities before they reach production.

---

### 39. Why should Terraform files be stored in Git?

Version control makes infrastructure changes traceable, reviewable, and repeatable.

---

### 40. Why should monitoring be implemented?

Monitoring helps detect failures, performance issues, and resource usage before they impact users.

---

# Explain the Complete Project

### 41. Explain the project in two minutes.

The developer writes the Flask application and pushes the code to GitHub.

GitHub Actions automatically starts the CI pipeline.

Dependencies are installed, the application is verified, and security scans are executed using Trivy and OWASP Dependency Check.

The application is containerized using Docker.

Terraform manages the cloud infrastructure.

Kubernetes deploys and manages the application.

Prometheus collects monitoring metrics.

Grafana visualizes the metrics through dashboards.

This creates a complete DevSecOps workflow from development to monitoring.

---

# Best Practices

- Keep Docker images small.
- Use Infrastructure as Code.
- Automate CI pipelines.
- Scan dependencies regularly.
- Monitor applications continuously.
- Keep secrets outside source code.
- Review security reports frequently.
- Use version control for everything.

---

# Key Takeaways

This project demonstrates practical knowledge of:

- Application Development
- Containerization
- Continuous Integration
- Security Automation
- Infrastructure as Code
- Kubernetes Deployment
- Monitoring
- DevSecOps Best Practices
