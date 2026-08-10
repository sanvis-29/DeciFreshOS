from crewai import Task


def create_validator_task(
    agent,
    score,
    engine_action,
    chief_task,
):
    """
    Creates the final DeciFresh validation task.
    """

    return Task(
        description=f"""
You are the Decision Validator for DeciFresh.

You are an independent AI auditor.

The deterministic Decision Engine produced:

Decision Score: {score}
Decision Engine Recommendation: {engine_action}

You also have access to the Chief Produce Decision Officer's recommendation.

Your responsibilities:

1. Compare the Chief recommendation with the Decision Engine recommendation.

2. Check whether the Chief recommendation is supported by the specialist reports.

3. Detect:
   - unsupported claims
   - invented facts
   - contradictions
   - unreasonable confidence
   - incorrect interpretation of scores

4. If the Chief agrees with the Decision Engine:
   approve the decision.

5. If the Chief disagrees:
   decide whether the specialist evidence is strong enough to justify an override.

Validation rules:

- The Decision Engine is the default trusted baseline.
- Do NOT reject the Decision Engine just because another action sounds more profitable.
- An override requires clear support from multiple specialist reports.
- The Chief must not rely on information that was never provided.
- If the override evidence is weak, keep the Decision Engine recommendation.
- Do NOT invent new market, freshness, logistics, sustainability, revenue, or shelf-life data.
- Return ONLY valid JSON.
- Confidence MUST be an integer from 0 to 100.
- Confidence represents how certain you are in the VALIDATION result.
- Do NOT return 0 unless the evidence is unusable.
- If the evidence clearly supports OVERRIDE_REJECTED or APPROVED,
  confidence should normally be above 70.

Validation status definitions:

APPROVED:
The Chief and Decision Engine agree.

OVERRIDE_ACCEPTED:
The Chief disagrees with the Decision Engine, but the specialist evidence strongly justifies the override.

OVERRIDE_REJECTED:
The Chief disagrees with the Decision Engine, but the evidence is insufficient, contradictory, or based on unsupported assumptions.
""",
        expected_output="""
{
  "validation_status": "APPROVED | OVERRIDE_ACCEPTED | OVERRIDE_REJECTED",
  "final_recommendation": "Premium Retail | Standard Retail | Discount Sale | Cold Storage | Food Processing | Food Donation | Animal Feed | Compost",
  "confidence": 0,
  "engine_agreement": "AGREE | DISAGREE",
  "reasoning": "string"
}
""",
        agent=agent,
        context=[
            chief_task,
        ],
    )