# AIZTA Normative Language

**Status**: Public draft v0.1

## 1. Requirement Keywords

The following uppercase terms define requirement strength in AIZTA normative documents:

| Keyword | Meaning |
|---|---|
| **MUST** / **REQUIRED** | An absolute requirement for conformance |
| **MUST NOT** | An absolute prohibition |
| **SHOULD** / **RECOMMENDED** | A strong recommendation; an alternative requires a documented reason and equivalent risk treatment |
| **SHOULD NOT** | A strong warning; an alternative requires a documented reason |
| **MAY** / **OPTIONAL** | A permitted but non-required capability |
|
The special meaning applies only when the keyword is written in uppercase. Lowercase words retain their ordinary English meaning.

## 2. Writing Rules

Normative text MUST:

- State one testable behavior or condition.
- Identify the responsible subject or component.
- Define the scope, trigger, or risk level where relevant.
- Define evidence or an observable result.
- Avoid requirements that depend on a named vendor or product.

Normative text SHOULD:

- Prefer a stable control identifier over a changing product name.
- Separate the requirement from implementation guidance.
- Describe failure behavior explicitly.
- Use precise terms such as `subject`, `action`, `resource`, `context`, `risk`, and `evidence`.

## 3. Control Requirement Template

```text
[ID] [Component or responsible party] MUST [observable behavior]
when [condition or scope].

Evidence: [one or more verifiable evidence items]
Test: [positive test and negative test]
```

Example:

```text
AZT-TOOL-001 The Tool Enforcement Point MUST validate the requested tool,
resource scope, parameters, and decision expiry before execution.

Evidence: decision event, validated request, execution result
Test: replay an expired decision and an out-of-scope resource request
```

## 4. Exceptions to Normative Requirements

An exception MUST be explicit, approved, time-bound, and recorded. A document MUST NOT weaken a `MUST` requirement by using an undocumented local interpretation.

## 5. Versioning of Normative Text

Changing a `MUST` or `MUST NOT` requirement is a normative change. The change MUST be described in release notes and assigned the appropriate specification version.
