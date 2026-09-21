# AIZTA Strategy and Roadmap

> Internal working reference. This document is not part of the public AIZTA standard and should not be linked from public product or standards material.

**Status**: Working reference v0.1  
**Organization**: AI Zero Trust Alliance (AIZTA)  
**Last reviewed**: 2026-09-21

## Purpose

This document records the strategic direction for AIZTA. It is a working reference for future standards, profiles, implementation guides, assessment tooling, and community discussions.

AIZTA should begin as a small, public, implementation-oriented standard. The scope can grow over time, but the first release must be understandable, testable, and useful without requiring an organization to adopt a specific cloud, model vendor, or programming language.

## Strategic Positioning

AIZTA is a vendor-neutral technical control standard for enforcing zero trust across AI applications, agents, models, data, tools, and AI supply chains.

AIZTA is not:

- A replacement for laws, regulations, or sector-specific obligations.
- A replacement for ISO/IEC 42001 certification.
- An official ACSC, ASD, CIS, or Microsoft standard.
- A certification claim until an independent governance and assessment program exists.

AIZTA may describe its relationships using precise terms such as **aligned with**, **mapped to**, **informed by**, and **compatible with**. It must not imply endorsement, affiliation, or certification by another organization without a written agreement.

## Relationship to Existing Frameworks

### ISO/IEC 42001

ISO/IEC 42001:2023 defines requirements for an Artificial Intelligence Management System (AIMS). It provides the organizational governance layer for managing AI-related risks and opportunities.

AIZTA provides technical controls and evidence that can support an AIMS. AIZTA should produce an informative mapping to ISO/IEC 42001 and must not claim that implementing AIZTA alone achieves certification.

Reference: [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html)

### ACSC and ASD

ACSC and ASD guidance is a high-value public-sector and Australian security reference. Relevant material includes secure AI system development, secure deployment, AI data security, AI/ML supply-chain risk, agentic AI, the Essential Eight, and the Information Security Manual.

AIZTA should provide an **Australia Profile** that maps AIZTA controls to selected ACSC/ASD guidance. The profile should identify where the mapping is direct, partial, or out of scope.

Reference: [ACSC Artificial Intelligence guidance](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence)

### CIS

CIS is a useful model for turning expert guidance into practical controls, implementation groups, benchmarks, and assessment material. AIZTA should learn from this operating model while remaining an independent project.

The proposed AIZTA structure is:

```text
AIZTA Framework
	-> AIZTA Controls
	-> AI Safeguards
	-> Risk Profiles
	-> Platform Profiles
	-> Assessment Methodology
	-> Evidence Packs
```

Reference: [Center for Internet Security](https://www.cisecurity.org/)

### RFC and BCP 14

AIZTA normative documents should use the requirements language defined by RFC 2119 and clarified by RFC 8174. The words `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`, and related terms have special meaning only when written in uppercase.

The standard should also use RFC 9457 Problem Details for machine-readable HTTP API errors where an API needs a common error representation.

References: [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119), [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174), [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457)

### Microsoft Foundry

Microsoft Foundry is a valuable implementation reference and an early platform profile candidate. Its model catalog, agent services, tools, observability, evaluation, control plane, and content safety features provide concrete integration points.

Microsoft-specific features must be documented as an **implementation profile**, not as the vendor-neutral AIZTA Core Standard. AIZTA must remain implementable on other clouds, on-premises platforms, and open-source stacks.

Reference: [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/foundry/)

## Guardrail Strategy

Microsoft Foundry default safety controls may be used as a baseline implementation for the input and output safety portion of AIZTA. They do not constitute the complete AIZTA guardrail model.

The core requirement should be capability-based:

```text
An implementation MUST apply input and output safety controls appropriate to
the risk profile, record whether the controls executed, and define behavior
when a safety dependency is unavailable.
```

Guardrails do not replace identity, delegation, authorization, data classification, tenant isolation, model and tool provenance, tool parameter validation, action approval, revocation, rollback, audit evidence, or incident response.

## Standard Architecture

The standard should be published as four related layers:

| Layer | Purpose | Initial artifact |
|---|---|---|
| Framework | Principles, scope, terminology, architecture, maturity | AIZTA Framework v0.1 |
| Controls | Testable requirements and evidence | AIZTA Control Catalog v0.1 |
| Profiles | Platform, industry, and jurisdiction adaptations | Platform and jurisdiction profiles |
| Assessment | Test procedures, scoring, exceptions, and reports | AIZTA Assessment Methodology v0.1 |

The existing HLD and LLD remain supporting architecture documents. They should be aligned to the Framework and Control Catalog as those artifacts mature.

## Initial Risk Profiles

The first release should avoid a large, abstract taxonomy. Start with three operational profiles:

| Profile | Target | Intent |
|---|---|---|
| AIZTA-Core | Any AI platform | Minimum vendor-neutral controls |
| AIZTA-Microsoft-Foundry | Microsoft Foundry deployments | Concrete platform mappings and evidence examples |
| AIZTA-Australia | Organizations using Australian guidance | ACSC/ASD and Essential Eight mapping |

Risk tiers remain useful across profiles:

- **R0**: Low-impact, public information.
- **R1**: Internal assistance and retrieval.
- **R2**: Business data changes and external communications.
- **R3**: High-impact or production actions requiring human control.
- **R4**: Irreversible or large-scale high-impact automation, prohibited by default.

## Control Catalog Requirements

The first catalog should contain approximately 30 controls. Each control must include a stable ID, security objective, risk tier, normative requirement, responsible party, implementation guidance, test method, negative test, minimum evidence, exception expiry, profile mappings, and version history.

Initial domains are identity, delegation, policy, enforcement, data, context, models, agents, tools, safety, supply chain, observability, response, testing, and exceptions.

## Assessment Model

An assessment should produce one of four results per control:

```text
pass | partial | fail | not_applicable
```

Every result must reference evidence, test time, asset version, policy version, and exception ID where applicable. A report must distinguish conformance, effectiveness, and coverage.

An AIZTA report must not be presented as ISO certification, government approval, or vendor endorsement.

## Roadmap

### Phase 1: Foundation

- Publish AIZTA Framework v0.1.
- Add BCP 14 normative-language rules.
- Define the 30-control catalog schema.
- Add an explicit independence and non-affiliation statement.

### Phase 2: Executable Controls

- Publish AIZTA Control Catalog v0.1 in Markdown and machine-readable YAML.
- Define control tests, negative tests, evidence examples, and exception handling.
- Add RFC 9457 error examples to the LLD API contract.

### Phase 3: Profiles and Mappings

- Publish the Microsoft Foundry profile.
- Publish the Australia ACSC/ASD profile.
- Publish an informative ISO/IEC 42001 evidence mapping.
- Add a CIS-inspired implementation-group view.

### Phase 4: Reference Implementation

- Implement a small PDP/PEP reference service.
- Add signed decision evidence and decision replay.
- Add tool authorization and human approval examples.
- Build a public conformance test suite.

### Phase 5: Community Review

- Invite practitioners, assessors, researchers, and platform engineers to review the draft.
- Record public comments and disposition.
- Version the specification based on reviewed changes.
- Delay certification claims until governance, assessor independence, and appeals are defined.

## Immediate Next Deliverables

The next implementation batch should create:

```text
docs/AIZTA-Core-Standard-v0.1.md
docs/AIZTA-Control-Catalog-v0.1.yaml
docs/profiles/microsoft-foundry-v0.1.md
docs/profiles/australia-acsc-asd-v0.1.md
docs/mappings/iso-iec-42001-v0.1.md
docs/assessment/AIZTA-Assessment-Methodology-v0.1.md
```

The public website should then add three clear entry points:

```text
Read the Core Standard
Browse Controls
View Mappings
```

## Governance Guardrails

AIZTA should not claim official status or certification authority prematurely. The project should maintain a public change log, conflict-of-interest policy, public comment process, vulnerability disclosure process, versioned normative documents, clear separation between Core Controls and vendor profiles, and a statement that references are mappings rather than endorsements.
