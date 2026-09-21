# AIZTA Core Standard v0.1

**Status**: Public draft
**Owner**: AI Zero Trust Alliance
**Audience**: Organizations that design, build, operate, assess, or procure AI systems

## 1. Purpose

AIZTA Core defines a vendor-neutral baseline for making AI actions verifiable, bounded, auditable, and reversible. It applies to AI applications, agents, models, data, tools, runtimes, and their supply chains.

AIZTA is an independent community standard. It is not a law, a regulatory approval, a certification claim, or a guarantee that a system is safe for every use. An implementation claim must identify the covered assets, workflows, risk levels, evidence period, and exceptions.

## 2. Core Promise

An AI system MUST NOT receive authority merely because it has a valid identity, uses an approved model, or runs inside a trusted network. Authority MUST be evaluated for the current subject, action, resource, context, risk, and evidence.

The AIZTA decision model is:

```text
Decision = Policy(subject, action, resource, context, risk, evidence)
```

Every protected action results in one of four effects:

- **ALLOW**: Permit the action within an explicit scope and lifetime.
- **CONSTRAIN**: Permit only after reducing scope, data, capability, or rate.
- **DENY**: Reject the action and record a stable reason.
- **QUARANTINE**: Isolate the subject, context, asset, or action pending review.

## 3. Applicability

This standard applies when an AI system can do one or more of the following:

- Access non-public data.
- Select or invoke a tool.
- Change a record or configuration.
- Communicate with an external party.
- Generate a decision with material impact.
- Operate with delegated authority.
- Ingest content from an untrusted source.

An organization MAY apply a stricter local policy. It MUST document any scope reduction, compensating control, or exception.

## 4. Trust Boundaries

AIZTA treats each of these as an explicit trust boundary:

1. User to application.
2. Application to agent.
3. Agent to model.
4. Agent to data and retrieval.
5. Agent to tool.
6. Runtime to external system.
7. Organization to supplier.
8. Control plane to evidence store.

A request crossing a trust boundary MUST be authenticated, authorized, constrained by policy, and recorded at the boundary that enforces the decision.

## 5. Control Principles

### 5.1 Explicit Authority

Authority MUST be represented by a unique subject, a stated purpose, an action, a resource scope, and an expiry. Historical approval or network location MUST NOT substitute for a current decision.

### 5.2 Least Privilege and Least Context

A system MUST provide only the data, tools, fields, records, and capability required for the current task. Untrusted instructions MUST NOT expand authority.

### 5.3 Independent Enforcement

The component making a decision MUST be distinct from untrusted model output and client claims. The enforcement point MUST reject a request when the decision is missing, expired, outside scope, or invalid.

### 5.4 Safe Failure

High-impact actions MUST fail closed when critical policy, identity, risk, or evidence dependencies are unavailable. A degraded mode MUST define which low-risk, side-effect-free actions remain available.

### 5.5 Human Control

R2 and above actions MUST support confirmation, approval, revocation, rollback, or a documented compensating action. R3 actions MUST have a human-controlled path before execution.

### 5.6 Evidence

A system MUST record enough evidence to reconstruct who or what requested an action, which policy was used, what assets and context were involved, what decision was made, and what result occurred.

Evidence MUST minimize sensitive content. A digest or controlled reference SHOULD be used instead of copying complete prompts, outputs, or personal data into ordinary audit logs.

## 6. Risk Levels

| Level | Meaning | Minimum posture |
|---|---|---|
| R0 | Low-impact observation or public information | Identity and basic audit |
| R1 | Internal assistance, retrieval, or low-impact generation | Data scope and input/output checks |
| R2 | Business data changes or external communication | Strong authentication, constrained scope, confirmation or approval |
| R3 | High-impact, production, financial, medical, or release action | Human approval, dual review, isolated execution, recovery path |
| R4 | Irreversible, large-scale, or unacceptable impact | Prohibited by default; exceptional governance required |

Risk MUST be assigned before a protected workflow is released. The effective level MUST be the highest applicable level across the subject, action, resource, context, and outcome.

## 7. Required Control Domains

A conforming implementation MUST address the following domains appropriate to its scope:

| Domain | Required outcome |
|---|---|
| Governance | Ownership, scope, risk, exceptions, and change control are defined |
| Identity | Users, services, agents, and workloads have unique, revocable identities |
| Delegation | Agent authority is bound to a principal, purpose, scope, and lifetime |
| Policy | Decisions are explicit, versioned, reviewable, and testable |
| Enforcement | Gateways enforce decisions independently of model output |
| Data | Classification, provenance, minimization, redaction, and tenant isolation are applied |
| Model | Model identity, version, source, capability, and evaluation status are known |
| Agent | Goals, tools, context, and delegation boundaries are controlled |
| Tool | Calls are registered, scoped, validated, rate-limited, and recoverable |
| Safety | Inputs and outputs are checked for applicable abuse and safety risks |
| Supply chain | Dependencies, assets, changes, and integrity claims are tracked |
| Evidence | Decisions and outcomes are tamper-evident, searchable, and retention-controlled |
| Response | Assets, sessions, tokens, and actions can be revoked or isolated |
| Assessment | Controls are tested with positive and negative cases |

## 8. Minimum Conformance

An implementation claiming AIZTA Core conformance MUST:

1. Define its system boundary and covered assets.
2. Assign risk levels to protected workflows.
3. Use unique and revocable identities for protected subjects.
4. Evaluate protected actions using a versioned policy.
5. Enforce decisions at a server-side boundary.
6. Apply least privilege to data and tools.
7. Treat external content and model output as untrusted.
8. Deny high-risk actions when critical control dependencies fail.
9. Produce decision and execution evidence.
10. Test at least one negative case for every claimed control domain.

A claim MUST publish the standard version, profile, scope, assessment date, exceptions, and evidence coverage.

## 9. Exceptions

An exception MUST have an owner, reason, affected control, risk acceptance, compensating control, approval, start date, expiry date, and review status. Expired exceptions MUST NOT silently continue.

A system MUST NOT use an exception to remove identity, server-side enforcement, evidence, or the ability to revoke high-risk authority without an explicit executive risk decision.

## 10. Versioning

AIZTA Core uses `MAJOR.MINOR.PATCH` for published specifications:

- **MAJOR**: Incompatible changes to normative behavior, control identifiers, or evidence contracts.
- **MINOR**: Backward-compatible controls, clarifications, profiles, or assessment additions.
- **PATCH**: Editorial corrections or backward-compatible defect fixes.

A published version MUST NOT be modified in place. Every change MUST produce a new version and a change record.

## 11. Independence Statement

AIZTA is an independent, vendor-neutral community standard. Product names, platform profiles, and implementation examples do not imply endorsement, certification, partnership, or affiliation. The AIZTA Core requirements apply regardless of provider, model family, hosting location, or implementation technology.

## 12. Next Documents

- AIZTA Control Catalog v0.1: Machine-readable control requirements and evidence.
- AIZTA Assessment Methodology v0.1: Test procedures, scoring, exceptions, and reports.
- AIZTA Implementation Profiles: Deployment-specific guidance that does not change Core requirements.
