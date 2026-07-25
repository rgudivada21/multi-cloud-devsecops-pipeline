# Docker

## Purpose

Docker packages an application with all its dependencies into a container.

This ensures the application runs the same way on every machine without additional setup.

---

## Problem

Running an application directly on different computers can cause issues.

Example:

- Python version is different.
- Required packages are missing.
- Operating systems are different.
- The application works on one machine but fails on another.

Docker solves this problem by creating a consistent runtime environment.

---

## Developer Thinking

The application should:

1. Run on any machine.
2. Include all required dependencies.
3. Be easy to deploy.
4. Behave the same in development, testing, and production.

---

## Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

## Code Explanation

### Base Image

```dockerfile
FROM python:3.11-slim
```

Downloads a lightweight Python 3.11 image.

Every container starts from a base image.

---

### Working Directory

```dockerfile
WORKDIR /app
```

Creates and switches to the `/app` directory inside the container.

All following commands run from this directory.

---

### Copy Requirements

```dockerfile
COPY requirements.txt .
```

Copies the dependency file into the container.

Only this file is copied first to improve Docker layer caching.

---

### Install Dependencies

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

Installs all Python packages required by the application.

---

### Copy Application

```dockerfile
COPY app/ .
```

Copies the application source code into the container.

---

### Expose Port

```dockerfile
EXPOSE 5000
```

Documents that the application listens on port 5000.

---

### Start Application

```dockerfile
CMD ["python", "app.py"]
```

Runs the Flask application when the container starts.

---

## Build Flow

```
Application Code
        │
        ▼
Dockerfile
        │
        ▼
Docker Build
        │
        ▼
Docker Image
        │
        ▼
Docker Container
        │
        ▼
Running Application
```

---

## Image vs Container

### Image

- Blueprint
- Read-only
- Created using a Dockerfile

### Container

- Running instance of an image
- Can be started, stopped, and removed

Example:

```
Dockerfile
      │
      ▼
Image
      │
      ▼
Container
```

---

## Real-World Usage

Docker is commonly used to:

- Package web applications
- Deploy microservices
- Run APIs
- Maintain consistent environments
- Simplify cloud deployments

---

## Best Practices

- Use lightweight base images.
- Copy dependency files before application code.
- Keep images small.
- Store secrets outside the image.
- Use specific image versions instead of `latest`.

---

## Common Mistakes

- Using very large base images.
- Copying unnecessary files.
- Storing passwords inside the image.
- Installing unused packages.
- Forgetting to expose the required port.

---

## Interview Questions

### Why is Docker used?

Docker packages an application and its dependencies so it runs consistently across different environments.

### What is a Docker image?

A Docker image is a blueprint used to create containers.

### What is a Docker container?

A container is a running instance of a Docker image.

### Why is `WORKDIR` used?

It sets the default working directory inside the container.

### Why do we install `requirements.txt` before copying the application?

It improves Docker build performance by using layer caching.

### What is the difference between `CMD` and `RUN`?

- `RUN` executes commands while building the image.
- `CMD` executes commands when the container starts.
