# AIZTA Standard Deployment Profile v0.1

**Status**: Public draft
**Applies to**: AI applications, agents, models, data, and tools with R0-R2 workflows

## 1. Profile Objective

This profile defines the minimum deployment shape for an organization operating ordinary internal or customer-facing AI workflows. It selects and clarifies AIZTA Core controls without changing their meaning.

## 2. Required Architecture

A conforming deployment MUST include:

- A registered identity for every user, service, agent, and workload.
- An AI access boundary that authenticates requests.
- A policy decision service and an independent enforcement point.
- A registered model and tool inventory.
- A data access boundary that enforces tenant and classification rules.
- An append-only or tamper-evident evidence store.
- A revocation path for identities, sessions, agents, and tools.

## 3. Required Controls

The profile MUST implement all AIZTA Core controls applicable to R1 and R2 workflows. At minimum, the following capabilities MUST be operational before production use:

1. Unique and short-lived identity.
2. Bounded agent delegation.
3. Explicit policy decision before protected action.
4. Server-side enforcement.
5. Data classification and tenant isolation.
6. Model and tool registration.
7. Tool request validation.
8. Input and output safety checks.
9. Decision evidence.
10. Revocation.
11. Positive and negative control tests.

## 4. Evidence Package

The deployment evidence package MUST contain:

- System boundary and asset register.
- Workflow risk register.
- Current policy versions.
- Model and tool approval records.
- Sample decision and execution events.
- Negative test results.
- Revocation exercise result.
- Active exception register.

## 5. Release Gate

A workflow MUST NOT enter production when any required control is `fail`, when a critical exception is expired, or when high-risk actions can bypass the enforcement boundary.
