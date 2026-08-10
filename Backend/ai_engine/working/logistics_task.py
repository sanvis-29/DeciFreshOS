from crewai import Task


def create_logistics_task(agent, logistics_score):
    """
    Creates the Logistics Analysis task.
    """

    return Task(
        description=f"""
You are the Supply Chain & Logistics Expert.

Analyze ONLY the logistics conditions.

Logistics Score:
{logistics_score}

Use this scale exactly:

- 0 to 30 = Poor
- 31 to 60 = Moderate
- 61 to 80 = Good
- 81 to 100 = Excellent

Your responsibilities:

1. Classify transportation feasibility.

2. Classify distribution efficiency.

3. Assess logistics risk.

4. Explain your reasoning briefly.

IMPORTANT:
- Logistics Score is a 0-100 score.
- Do NOT invent routes, distances, vehicles, warehouses, cold-chain availability, or delivery times.
- ONLY analyze logistics.
- Ignore freshness.
- Ignore market price.
- Ignore demand.
- Ignore waste risk.
- Do NOT recommend the final business action.
- Return ONLY valid JSON.
- Confidence MUST be an integer from 0 to 100.
- Base confidence on how clearly the Logistics Score fits the provided scale.
- Do NOT return 0 confidence unless the supplied data is unusable.
- You MUST follow the provided logistics scale exactly.
- A Logistics Score of 81-100 MUST be classified as Excellent.
- Apply the scale mechanically.
- For score 85, transportation_feasibility MUST be "Excellent".
- For score 85, distribution_efficiency MUST be "Excellent".
- Do not substitute "Good" for "Excellent".
""",
        expected_output="""
{
  "transport_feasibility": "Poor | Moderate | Good | Excellent",
  "distribution_efficiency": "Poor | Moderate | Good | Excellent",
  "logistics_risk": "Low | Moderate | High",
  "confidence": 0,
  "reasoning": "string"
}
""",
        agent=agent,
    )