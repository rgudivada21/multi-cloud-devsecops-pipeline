# Kubernetes

## Purpose

Kubernetes is a container orchestration platform.

It automates the deployment, scaling, networking, and management of containerized applications.

Instead of managing containers manually, Kubernetes manages them automatically.

---

## Problem

Docker can run containers.

Example:

```
Docker

↓

Container Running
```

But what happens if:

- The container crashes?
- Traffic increases?
- Multiple containers are needed?
- The application must be updated without downtime?

Docker alone cannot handle all these situations efficiently.

Kubernetes solves these problems.

---

## Developer Thinking

The application should:

1. Run continuously.
2. Restart automatically if it crashes.
3. Scale when traffic increases.
4. Distribute traffic across multiple containers.
5. Update without downtime.

---

## Project Files

```
kubernetes/

├── deployment.yaml
└── service.yaml
```

---

# deployment.yaml

```yaml
apiVersion: apps/v1

kind: Deployment

metadata:
  name: flask-app

spec:
  replicas: 2

  selector:
    matchLabels:
      app: flask-app

  template:

    metadata:
      labels:
        app: flask-app

    spec:

      containers:

      - name: flask-app

        image: flask-app:latest

        ports:

        - containerPort: 5000
```

---

## Code Explanation

### apiVersion

```yaml
apiVersion: apps/v1
```

Specifies which Kubernetes API version is used.

---

### kind

```yaml
kind: Deployment
```

Creates a Deployment resource.

A Deployment manages Pods automatically.

---

### metadata

```yaml
metadata:
  name: flask-app
```

Gives the Deployment a unique name.

---

### replicas

```yaml
replicas: 2
```

Runs two identical application instances.

Example:

```
Pod 1

Running

Pod 2

Running
```

If one Pod fails, another continues serving users.

---

### selector

```yaml
selector:
  matchLabels:
    app: flask-app
```

Tells Kubernetes which Pods belong to this Deployment.

---

### template

Defines the blueprint for creating Pods.

Every new Pod is created from this template.

---

### container

```yaml
containers:
```

Lists the containers that will run inside the Pod.

---

### image

```yaml
image: flask-app:latest
```

Specifies which Docker image Kubernetes should run.

---

### containerPort

```yaml
containerPort: 5000
```

Indicates that the application listens on port 5000.

---

# service.yaml

```yaml
apiVersion: v1

kind: Service

metadata:
  name: flask-service

spec:

  selector:
    app: flask-app

  ports:

  - port: 80

    targetPort: 5000

  type: LoadBalancer
```

---

## Service Explanation

### kind

```yaml
kind: Service
```

Creates a Kubernetes Service.

A Service provides stable network access to Pods.

---

### selector

```yaml
selector:
  app: flask-app
```

Connects the Service to Pods with the label `app: flask-app`.

---

### port

```yaml
port: 80
```

The port exposed by the Service.

Users connect using this port.

---

### targetPort

```yaml
targetPort: 5000
```

The port used by the container.

Traffic is forwarded from the Service to the application.

---

### type

```yaml
type: LoadBalancer
```

Creates an external load balancer (when supported by the cloud provider).

Users can access the application through the load balancer.

---

## Kubernetes Workflow

```
Deployment

        │

        ▼

Creates Pods

        │

        ▼

Pods Run Containers

        │

        ▼

Service Finds Pods

        │

        ▼

Load Balancer

        │

        ▼

Users Access Application
```

---

## Docker vs Kubernetes

| Docker | Kubernetes |
|---------|------------|
| Runs containers | Manages containers |
| Single container management | Multiple container management |
| Manual scaling | Automatic scaling |
| Manual recovery | Automatic recovery |
| No built-in load balancing | Built-in load balancing |

---

## Real-World Usage

Companies use Kubernetes to:

- Deploy microservices
- Scale applications automatically
- Perform rolling updates
- Recover from failures
- Run applications across multiple servers

---

## Best Practices

- Keep one application per container.
- Use Deployments instead of standalone Pods.
- Use Services for communication.
- Define resource requests and limits.
- Store secrets using Kubernetes Secrets.

---

## Common Mistakes

- Running only one replica.
- Using the `latest` image tag in production.
- Forgetting labels and selectors.
- Exposing unnecessary ports.
- Deploying without health checks.

---

## Interview Questions

### What is Kubernetes?

Kubernetes is a container orchestration platform that automates the deployment, scaling, and management of containerized applications.

---

### Why do we need Kubernetes if Docker already exists?

Docker creates and runs containers.

Kubernetes manages containers across multiple machines, provides scaling, self-healing, load balancing, and rolling updates.

---

### What is a Pod?

A Pod is the smallest deployable unit in Kubernetes. It contains one or more containers.

---

### What is a Deployment?

A Deployment manages Pods and ensures the desired number of replicas are always running.

---

### What is a Service?

A Service provides a stable network endpoint for accessing Pods.

---

### What is the purpose of `replicas`?

It specifies how many copies of the application should run.

---

### Why is `LoadBalancer` used?

It exposes the application externally and distributes incoming traffic to the available Pods.
