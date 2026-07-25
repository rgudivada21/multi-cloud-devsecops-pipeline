# Terraform

## Purpose

Terraform is an Infrastructure as Code (IaC) tool used to create, update, and manage cloud infrastructure using code.

Instead of creating resources manually through the cloud console, Terraform allows infrastructure to be defined in configuration files.

---

## Problem

Suppose a project needs:

- Virtual Machine
- Storage Account
- Network
- Database
- Load Balancer

Creating these resources manually every time is:

- Time-consuming
- Error-prone
- Difficult to maintain
- Difficult to reproduce

Terraform solves this problem by managing infrastructure through code.

---

## Developer Thinking

The infrastructure should:

1. Be created automatically.
2. Be reproducible.
3. Be version controlled.
4. Work across different cloud providers.
5. Be easy to update.

---

## Project Structure

```
terraform/

├── aws/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── azure/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
└── gcp/
    ├── main.tf
    ├── variables.tf
    └── outputs.tf
```

Each cloud provider has its own Terraform configuration.

---

## main.tf

```hcl
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}
```

### Explanation

#### terraform

Defines Terraform settings.

---

#### required_providers

Specifies which provider Terraform should download.

Example:

- AWS
- Azure
- Google Cloud

---

#### provider

Configures the cloud provider.

Example:

```hcl
provider "aws" {
    region = "us-east-1"
}
```

This tells Terraform to create resources in the **US East (N. Virginia)** region.

---

## variables.tf

```hcl
variable "aws_region" {
    description = "AWS Region"
    type = string
    default = "us-east-1"
}
```

### Why Variables?

Instead of changing the code every time, values can be changed using variables.

Without variables:

```hcl
region = "us-east-1"
```

To use another region, the code must be modified.

With variables:

```hcl
var.aws_region
```

Only the variable value changes.

The application code remains the same.

---

## outputs.tf

```hcl
output "aws_region" {
    value = var.aws_region
}
```

Outputs display useful information after Terraform completes.

Example:

```
aws_region = us-east-1
```

---

## Terraform Workflow

```
Write Configuration

        │

        ▼

terraform init

        │

        ▼

Download Providers

        │

        ▼

terraform plan

        │

        ▼

Preview Changes

        │

        ▼

terraform apply

        │

        ▼

Create Infrastructure

        │

        ▼

Resources Available
```

---

## Multi-Cloud Support

Terraform supports multiple cloud providers.

Example:

```
Terraform

        │

 ┌──────┼──────┐

 ▼      ▼      ▼

AWS   Azure   GCP
```

A single tool can manage infrastructure across different cloud platforms.

---

## Real-World Usage

Companies use Terraform to create:

- Virtual Machines
- Kubernetes Clusters
- Networks
- Databases
- Storage Accounts
- Load Balancers
- DNS Records

Everything is managed using code.

---

## Best Practices

- Store Terraform files in Git.
- Use variables instead of hardcoded values.
- Keep each cloud provider in a separate folder.
- Review changes using `terraform plan`.
- Use remote state for team projects.

---

## Common Mistakes

- Hardcoding values.
- Editing cloud resources manually after Terraform creates them.
- Skipping `terraform plan`.
- Not using variables.
- Mixing resources for multiple cloud providers in one file.

---

## Interview Questions

### What is Terraform?

Terraform is an Infrastructure as Code (IaC) tool used to create and manage cloud infrastructure using configuration files.

---

### What is Infrastructure as Code?

Infrastructure is defined and managed using code instead of manual configuration.

---

### What is a Provider?

A provider allows Terraform to communicate with a cloud platform such as AWS, Azure, or GCP.

---

### Why are variables used?

Variables make Terraform configurations reusable and easier to maintain.

---

### What are outputs?

Outputs display useful values after Terraform finishes creating infrastructure.

---

### What is the difference between `terraform plan` and `terraform apply`?

- `terraform plan` previews the changes that Terraform will make.
- `terraform apply` creates or updates the infrastructure based on the configuration.

---

### Why is Terraform called a Multi-Cloud tool?

Because the same Terraform workflow can manage infrastructure across AWS, Azure, GCP, and many other providers using different provider configurations.
