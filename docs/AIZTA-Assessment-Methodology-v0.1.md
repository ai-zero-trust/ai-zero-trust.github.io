# AIZTA Assessment Methodology v0.1

**Status**: Public draft
**Purpose**: Assess implementation of AIZTA Core controls and deployment profiles

## 1. Assessment Principles

An assessment MUST be evidence-based, scoped, reproducible, and independent from the person who implemented the control where practical. An assessment is a point-in-time statement about the declared scope; it is not a permanent safety guarantee.

The assessment report MUST identify:

- Organization and system boundary.
- Covered workflows, assets, tenants, and risk levels.
- Standard and profile versions.
- Assessment period and assessor.
- Exclusions and exceptions.
- Evidence references and test results.

## 2. Control Results

Each control receives one result:

| Result | Meaning |
|---|---|
| `pass` | Requirement is implemented and evidence supports its operation. |
| `partial` | Material parts are implemented, but coverage or effectiveness is incomplete. |
| `fail` | Requirement is absent, bypassable, expired, or unsupported by evidence. |
| `not_applicable` | Requirement is outside the declared scope with a documented reason. |

A control MUST NOT be marked `pass` solely because a policy or design document exists. The assessor MUST verify operation through evidence or testing.

## 3. Assessment Procedure

### Step 1: Scope

Record the system boundary, assets, workflows, tenants, data classes, models, tools, and risk levels. Confirm that the scope matches the organization’s claim.

### Step 2: Design Review

Review identity, delegation, policy, enforcement, data, model, agent, tool, evidence, response, and exception design. Record missing requirements and ambiguous ownership.

### Step 3: Evidence Sampling

Sample current policies, decision events, execution events, approvals, inventories, tests, exercises, and exceptions. Sampling MUST cover the highest-risk workflows and at least one recently changed asset.

### Step 4: Positive Testing

Execute representative allowed requests and verify that the system grants only the declared scope, records the decision, and produces the expected outcome.

### Step 5: Negative Testing

Attempt expired identity, missing policy, out-of-scope resource, cross-tenant access, invalid parameters, unregistered asset, prompt injection, replay, and dependency-failure paths as applicable.

### Step 6: Results and Remediation

Assign control results, record evidence references, describe impact, identify an owner, and set remediation due dates. A critical failure MUST prevent a conformance claim for the affected profile.

## 4. Minimum Sampling Guidance

| Risk | Minimum sample |
|---|---|
| R0 | One current configuration and one audit sample |
| R1 | Three decisions across two workflows, including one negative test |
| R2 | Five decisions across two workflows, one approval, one revocation, and two negative tests |
| R3 | Ten decisions, two independent approvals, isolation test, recovery test, and decision replay |
| R4 | Special assessment with independent review, bounded pilot, emergency stop, and recovery evidence |

The assessor MAY increase sampling when results are inconsistent, systems changed materially, or evidence integrity is uncertain.

## 5. Conformance Decision

A profile claim is:

- **Conformant** when all required controls pass and exceptions are within policy.
- **Conditionally conformant** when partial controls have approved remediation with a defined due date and no disqualifying failure.
- **Not conformant** when a required control fails, evidence is unavailable, or the declared scope cannot be verified.

R3 and R4 claims MUST NOT be conformant when high-impact approval, isolation, recovery, revocation, evidence integrity, or negative testing fails.

## 6. Report Format

The final report MUST include:

```text
assessment_id
organization
system_boundary
standard_version
profile_version
assessment_period
assessor
scope
control_results
evidence_references
exceptions
remediation_plan
conformance_decision
signatures
```

## 7. Reassessment

A reassessment is REQUIRED after a material change to a model, agent, policy, data source, tool, runtime, tenant boundary, or risk level. At minimum, the changed control, dependent controls, and affected negative tests MUST be rerun.
