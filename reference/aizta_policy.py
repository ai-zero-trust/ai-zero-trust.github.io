"""Minimal deterministic AIZTA policy decision point reference."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Effect(str, Enum):
    ALLOW = "allow"
    CONSTRAIN = "constrain"
    DENY = "deny"
    QUARANTINE = "quarantine"


@dataclass(frozen=True)
class Request:
    request_id: str
    subject_id: str
    subject_type: str
    delegated_by: str | None
    purpose: str
    action: str
    resource_id: str
    tenant_id: str
    risk_level: int
    model_id: str
    tool_id: str | None = None
    tool_registered: bool = False
    context_trusted: bool = False
    approval_id: str | None = None
    requested_fields: tuple[str, ...] = ()


@dataclass(frozen=True)
class Decision:
    request_id: str
    effect: Effect
    reason_codes: tuple[str, ...]
    constraints: dict[str, Any] = field(default_factory=dict)
    policy_version: str = "core-0.1.0"
    evidence_refs: tuple[str, ...] = ()


class PolicyDecisionPoint:
    """Small reference evaluator for the AIZTA Core decision model."""

    def __init__(self, allowed_fields: tuple[str, ...] = ("status", "public_comment")) -> None:
        self.allowed_fields = frozenset(allowed_fields)

    def evaluate(self, request: Request) -> Decision:
        reasons: list[str] = []
        evidence = (f"request:{request.request_id}",)

        if not request.subject_id or request.subject_type not in {"user", "service", "agent"}:
            return self._deny(request, "IDENTITY_INVALID", evidence)
        if request.subject_type == "agent" and not request.delegated_by:
            return self._deny(request, "DELEGATION_MISSING", evidence)
        if not request.purpose:
            return self._deny(request, "PURPOSE_MISSING", evidence)
        if not request.resource_id or not request.tenant_id:
            return self._deny(request, "RESOURCE_SCOPE_MISSING", evidence)
        if request.risk_level < 0 or request.risk_level > 4:
            return self._deny(request, "RISK_INVALID", evidence)
        if not request.context_trusted:
            return self._quarantine(request, "CONTEXT_UNTRUSTED", evidence)
        if request.tool_id and not request.tool_registered:
            return self._deny(request, "TOOL_UNREGISTERED", evidence)

        reasons.append(f"RISK_R{request.risk_level}")
        if request.risk_level >= 3 and not request.approval_id:
            return Decision(
                request.request_id,
                Effect.CONSTRAIN,
                tuple(reasons + ["APPROVAL_REQUIRED"]),
                {"requires_approval": True, "max_scope": request.resource_id},
                evidence_refs=evidence,
            )
        if request.requested_fields and not set(request.requested_fields).issubset(self.allowed_fields):
            return Decision(
                request.request_id,
                Effect.CONSTRAIN,
                tuple(reasons + ["FIELD_SCOPE_REDUCED"]),
                {"allowed_fields": sorted(self.allowed_fields)},
                evidence_refs=evidence,
            )
        return Decision(request.request_id, Effect.ALLOW, tuple(reasons + ["POLICY_MATCH"]), evidence_refs=evidence)

    @staticmethod
    def _deny(request: Request, reason: str, evidence: tuple[str, ...]) -> Decision:
        return Decision(request.request_id, Effect.DENY, (reason,), evidence_refs=evidence)

    @staticmethod
    def _quarantine(request: Request, reason: str, evidence: tuple[str, ...]) -> Decision:
        return Decision(request.request_id, Effect.QUARANTINE, (reason,), evidence_refs=evidence)
