# AIZTA High-Impact Deployment Profile v0.1

**Status**: Public draft
**Applies to**: AI workflows with R3 or R4 actions

## 1. Profile Objective

This profile defines additional safeguards for workflows that can materially affect people, finances, production systems, safety, regulated records, or irreversible external state.

## 2. Additional Requirements

A high-impact deployment MUST:

- Require an accountable human owner for every protected workflow.
- Require two-person review for policy publication and R3 approval.
- Bind approval to the exact subject, action, resource scope, request digest, and expiry.
- Execute high-impact tools in an isolated runtime with explicit outbound boundaries.
- Provide rollback, compensation, or an approved recovery path before release.
- Maintain a tested emergency revocation and quarantine procedure.
- Record model, data, tool, policy, and runtime versions for every R3 decision.
- Run adversarial, misuse, injection, privilege, and data-isolation tests before release and after material change.
- Review exceptions at least every 30 days.

## 3. R4 Default

R4 workflows are prohibited by default. A release requires documented necessity, executive risk acceptance, independent review, a defined operating limit, human takeover, emergency stop, and a recovery plan.

An R4 approval MUST NOT authorize unrestricted autonomous operation. It MUST define a finite scope, duration, resource set, and maximum impact.

## 4. Operating Evidence

The evidence package MUST include:

- Impact assessment and accountable owner.
- Dual approval records.
- Isolation and recovery test results.
- Emergency stop exercise.
- Decision replay sample.
- Change impact records.
- Exception and risk acceptance records.

## 5. Release Gate

A high-impact workflow MUST be denied release if human approval, isolation, recovery, revocation, evidence integrity, or negative testing is incomplete.
