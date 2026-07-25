# Prometheus

## Purpose

Prometheus is an open-source monitoring and alerting tool.

It collects metrics from applications and infrastructure, stores them as time-series data, and helps monitor system health.

---

## Problem

Once an application is deployed, developers need answers to questions like:

- Is the application running?
- How many requests are received?
- What is the CPU usage?
- How much memory is being used?
- Is the response time increasing?

Checking these values manually is not practical.

Prometheus collects this information automatically.

---

## Developer Thinking

The monitoring system should:

1. Collect application metrics.
2. Store metrics over time.
3. Allow querying the collected data.
4. Send metrics to visualization tools like Grafana.
5. Trigger alerts when necessary.

---

## Configuration File

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "flask-app"

    static_configs:
      - targets:
          - "localhost:5000"
```

---

## Code Explanation

### Global Configuration

```yaml
global:
```

Defines settings that apply to the entire Prometheus server.

---

### Scrape Interval

```yaml
scrape_interval: 15s
```

Prometheus collects metrics every 15 seconds.

This interval can be adjusted depending on monitoring requirements.

---

### Scrape Configurations

```yaml
scrape_configs:
```

Defines the list of applications or services that Prometheus should monitor.

---

### Job Name

```yaml
job_name: "flask-app"
```

Assigns a name to the monitoring job.

This name appears in Prometheus queries and dashboards.

---

### Static Configurations

```yaml
static_configs:
```

Specifies a fixed list of targets.

---

### Targets

```yaml
targets:
  - "localhost:5000"
```

Prometheus sends requests to this application to collect metrics.

---

## Monitoring Workflow

```
Application

      │

      ▼

Exports Metrics

      │

      ▼

Prometheus

      │

      ▼

Stores Metrics

      │

      ▼

Grafana

      │

      ▼

Dashboard
```

---

## What Are Metrics?

Metrics are numerical values collected over time.

Examples:

- CPU Usage
- Memory Usage
- Disk Usage
- Request Count
- Response Time
- Error Rate

---

## Real-World Usage

Companies use Prometheus to monitor:

- Applications
- Kubernetes clusters
- Docker containers
- Databases
- Virtual Machines
- Cloud infrastructure

---

## Best Practices

- Use meaningful job names.
- Monitor only required services.
- Keep scrape intervals reasonable.
- Store metrics securely.
- Configure alerts for critical failures.

---

## Common Mistakes

- Monitoring too many unnecessary metrics.
- Using very short scrape intervals.
- Forgetting to expose application metrics.
- Ignoring failed scrape targets.
- Not configuring alerts.

---

## Interview Questions

### What is Prometheus?

Prometheus is an open-source monitoring system that collects and stores application and infrastructure metrics.

---

### What is a metric?

A metric is a numerical measurement collected over time, such as CPU usage or request count.

---

### What is `scrape_interval`?

It defines how often Prometheus collects metrics from monitored applications.

---

### What is a target?

A target is the application or service that Prometheus monitors.

---

### Why is Prometheus used with Grafana?

Prometheus stores metrics, while Grafana displays those metrics through dashboards.

---

### Can Prometheus send alerts?

Yes.

Prometheus can work with Alertmanager to send alerts when predefined conditions are met.
