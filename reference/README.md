# AIZTA Reference Implementation

This directory contains a small, deterministic Policy Decision Point (PDP) used to make the AIZTA Core decision model executable and testable.

## Scope

The reference evaluator demonstrates:

- Unique subject and agent delegation checks.
- Purpose, tenant, resource, and risk validation.
- Trusted-context quarantine.
- Tool registration checks.
- High-impact approval constraints.
- Field-scope reduction.
- Evidence references on every decision.

It is intentionally small and has no production dependencies. It is not a production authorization service and does not provide authentication, storage, transport security, or a complete policy language.

## Run

From this directory:

```text
python3 -m unittest -v
```

The implementation is a reference for behavior and test cases. Deployments MUST adapt it to their identity, policy, data, tool, and evidence systems.
