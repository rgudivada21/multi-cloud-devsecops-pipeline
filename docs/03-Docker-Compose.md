# Docker Compose

## Purpose

Docker Compose is used to run multiple containers together using a single configuration file.

Instead of starting each container manually, Docker Compose manages them as one application.

---

## Problem

Imagine a project contains:

- Flask Application
- MySQL Database
- Redis Cache
- Prometheus
- Grafana

Starting each container one by one is time-consuming and error-prone.

Docker Compose allows all services to start with a single command.

---

## Developer Thinking

The application should:

1. Start all required containers together.
2. Configure networking automatically.
3. Map ports between the host and containers.
4. Keep configuration in one file.

---

## Docker Compose File

```yaml
version: "3.9"

services:

  flask-app:
    build:
      context: .
      dockerfile: docker/Dockerfile

    container_name: flask-app

    ports:
      - "5000:5000"
```

---

## Code Explanation

### Version

```yaml
version: "3.9"
```

Specifies the Docker Compose file format version.

---

### Services

```yaml
services:
```

Defines all containers that belong to the application.

Every container is created under the `services` section.

---

### Service Name

```yaml
flask-app:
```

Defines the service name.

Docker Compose uses this name to identify the container.

---

### Build

```yaml
build:
```

Tells Docker Compose to build an image instead of downloading one.

---

### Context

```yaml
context: .
```

Uses the current project directory as the build context.

Docker can access files inside this directory.

---

### Dockerfile

```yaml
dockerfile: docker/Dockerfile
```

Specifies which Dockerfile should be used to build the image.

---

### Container Name

```yaml
container_name: flask-app
```

Creates a container with a readable name.

Without this, Docker generates a random container name.

---

### Port Mapping

```yaml
ports:
  - "5000:5000"
```

Maps ports between the host machine and the container.

```
Host Machine
Port 5000
      │
      ▼
Container
Port 5000
```

Now the application can be accessed from:

```
http://localhost:5000
```

---

## Execution Flow

```
docker-compose up

        │

        ▼

Read docker-compose.yml

        │

        ▼

Build Image

        │

        ▼

Create Container

        │

        ▼

Start Application

        │

        ▼

Application Running
```

---

## Real-World Usage

Docker Compose is commonly used for:

- Local development
- Integration testing
- Running multiple services
- Creating repeatable development environments

Example:

```
Application

↓

Database

↓

Redis

↓

Prometheus

↓

Grafana

↓

Started together
```

---

## Best Practices

- Keep one service for one container.
- Use meaningful service names.
- Store environment variables separately.
- Keep the compose file simple.
- Use volumes for persistent data when required.

---

## Common Mistakes

- Using incorrect port mappings.
- Forgetting to build the image.
- Using duplicate container names.
- Keeping secrets inside the compose file.
- Running unnecessary services.

---

## Interview Questions

### Why is Docker Compose used?

Docker Compose manages multiple containers using a single configuration file.

---

### What is the difference between Docker and Docker Compose?

Docker creates and runs individual containers.

Docker Compose manages multiple containers together.

---

### What does `services` mean?

It defines all containers that belong to the application.

---

### What does `build` do?

It builds a Docker image using the specified Dockerfile.

---

### What is port mapping?

Port mapping connects a port on the host machine to a port inside the container.

Example:

```
Host:5000

↓

Container:5000
```

---

### Can Docker Compose be used in production?

It is mainly used for development and testing.

Production environments commonly use container orchestration platforms such as Kubernetes.
