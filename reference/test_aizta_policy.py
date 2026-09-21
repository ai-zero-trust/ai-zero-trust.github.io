import unittest

from aizta_policy import Effect, PolicyDecisionPoint, Request


class PolicyDecisionPointTests(unittest.TestCase):
    def setUp(self):
        self.pdp = PolicyDecisionPoint()

    def request(self, **overrides):
        values = {
            "request_id": "req-001",
            "subject_id": "agent-support",
            "subject_type": "agent",
            "delegated_by": "user-123",
            "purpose": "customer-support",
            "action": "ticket.update",
            "resource_id": "ticket-456",
            "tenant_id": "tenant-a",
            "risk_level": 2,
            "model_id": "model-a@1",
            "tool_id": "ticket-api",
            "tool_registered": True,
            "context_trusted": True,
        }
        values.update(overrides)
        return Request(**values)

    def test_allows_scoped_registered_action(self):
        decision = self.pdp.evaluate(self.request())
        self.assertEqual(decision.effect, Effect.ALLOW)
        self.assertIn("POLICY_MATCH", decision.reason_codes)

    def test_denies_missing_delegation(self):
        decision = self.pdp.evaluate(self.request(delegated_by=None))
        self.assertEqual(decision.effect, Effect.DENY)
        self.assertIn("DELEGATION_MISSING", decision.reason_codes)

    def test_quarantines_untrusted_context(self):
        decision = self.pdp.evaluate(self.request(context_trusted=False))
        self.assertEqual(decision.effect, Effect.QUARANTINE)

    def test_denies_unregistered_tool(self):
        decision = self.pdp.evaluate(self.request(tool_registered=False))
        self.assertEqual(decision.effect, Effect.DENY)
        self.assertIn("TOOL_UNREGISTERED", decision.reason_codes)

    def test_constrains_high_impact_action_without_approval(self):
        decision = self.pdp.evaluate(self.request(risk_level=3))
        self.assertEqual(decision.effect, Effect.CONSTRAIN)
        self.assertTrue(decision.constraints["requires_approval"])

    def test_constrains_unknown_fields(self):
        decision = self.pdp.evaluate(self.request(requested_fields=("status", "private_note")))
        self.assertEqual(decision.effect, Effect.CONSTRAIN)
        self.assertEqual(decision.constraints["allowed_fields"], ["public_comment", "status"])


if __name__ == "__main__":
    unittest.main()
