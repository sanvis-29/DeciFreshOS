from crewai import Task


def create_market_task(agent, market_price, demand):
    """
    Creates the Market Intelligence task.
    """

    return Task(
        description=f"""
You are the Market Intelligence Analyst.

Analyze ONLY the market conditions.

Market Price Score:
{market_price}

Demand Score:
{demand}

Use these scales exactly:

Market Price:
- 0 to 30 = Low
- 31 to 60 = Moderate
- 61 to 80 = High
- 81 to 100 = Very High

Demand:
- 0 to 30 = Low
- 31 to 60 = Moderate
- 61 to 80 = High
- 81 to 100 = Very High

Your responsibilities:

1. Determine overall market attractiveness.

2. Determine the revenue opportunity.

3. Determine whether current market conditions support selling now.

4. Explain your reasoning briefly.

IMPORTANT:
- Market Price and Demand are SCORES from 0-100.
- Do NOT multiply Market Price by Demand.
- Do NOT treat Demand as number of units.
- Do NOT invent actual currency, revenue, customers, or quantities.
- ONLY analyze market conditions.
- Ignore freshness.
- Ignore logistics.
- Ignore waste risk.
- Do NOT recommend the final business action.
- Return ONLY valid JSON.
- Confidence MUST be an integer from 0 to 100.
- Base confidence on how clearly the supplied scores fit the defined scales.
- Do NOT return 0 confidence unless the supplied data is unusable or contradictory.
""",
        expected_output="""
{
  "market_attractiveness": "Low | Moderate | High | Very High",
  "revenue_opportunity": "Low | Moderate | High | Very High",
  "sell_now": true,
  "confidence": 0,
  "reasoning": "string"
}
""",
        agent=agent,
    )