> Cloud Native Fundamentals
Udacity // Cloud Native Fundamentals Scholarship Program

[TOC]

# Lesson 1: Introduction to Cloud-Native Fundamentals

## Introduction to Cloud Native

> Cloud-Native  
> Set of practices that empowers an organization to buil and manage applications at scale

Can be achieved by using private, hybrid or public cloud providers and in addition to scaling, the organization needs to be agile in integrating customer feedback and adaptability to the surrounding technology ecosystem.

Containers and cloud-native go hand-in-hand. Containers are used to run a single application with all its dependencies which makes it easy to manage, deploy and recover quickly. With that said, you will see a often see a microservice-based architecture with cloud-native tooling as you can manage and configure services in a container easily packaged and ready to be executed.

## CNCF and Cloud-Native Tooling

**Container Orchestrators** appeared over time to make it easy to manage containers, such as:
- Docker Swarm
- Apache Mesos
- Kubernetes (winner)

**Kubernetes**

_Automates_:
- Configuration
- Management
- Scalability

_Solutionizes the integration of the following functionalities_:
- Runtime: application execution environment
- Networking: application connectivity
- Storage: application resources
- Service Mesh: granular control for the traffic within a cluster
- Logs and Metrics: construct the observability stack
- Tracing: building the full request journey

> CNCF  
> Cloud Native Computing Foundation

- Founded in 2015
- Vendor-neutral home for open source projects like:
	- Kubernetes
	- Prometheus
	- ETCD
	- Envoy
	- and more (1,300)

## Stakeholders

Always consider the main stakeholders when adopting cloud-native tooling and principles. We need to evaluate the key-points assessed from a business and technical prospective before integrating.

Cloud-native tooling adoption has increased because of rapid delivery of value to customers and the ease to adjust and extend based on requirements.

**Business Stakeholders**
- Agility: perform strategic transformations
- Growth: quickly iterate on customer feedback
- Service Availability: ensures the product is available to customers 24/7

**Technical Stakeholders**
- Automation: release a service without human intervention
- Orchestration: introduce a container orchestrator to manage thousands of services with minimal effort
- Observability: ability to independently troubleshoot and debug each component