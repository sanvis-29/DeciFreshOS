from crewai import Task


def create_sustainability_task(agent, waste_risk):
    """
    Creates the Sustainability & Food Waste task.
    """

    return Task(
        description=f"""
You are the Sustainability & Food Waste Expert.

Analyze ONLY the sustainability and food-waste conditions.

Waste Risk Score:
{waste_risk}

Use this scale EXACTLY:

- 0 to 30 = Low Waste Risk
- 31 to 60 = Moderate Waste Risk
- 61 to 80 = High Waste Risk
- 81 to 100 = Critical Waste Risk

Your responsibilities:

1. Classify the waste risk.

2. Assess the likelihood of food waste.

3. Identify the primary environmental concern.

4. Select ONE appropriate sustainability strategy.

Possible sustainability strategies:

- Immediate Sale
- Cold Storage
- Food Processing
- Food Donation
- Animal Feed
- Compost

IMPORTANT:
- Waste Risk is a score from 0-100.
- A LOWER Waste Risk score means LOWER likelihood of waste.
- A HIGHER Waste Risk score means HIGHER likelihood of waste.
- Do NOT reinterpret the scale.
- Do NOT assume produce is close to spoilage when Waste Risk is low.
- Do NOT invent environmental or supply-chain data.
- Ignore freshness.
- Ignore market price.
- Ignore demand.
- Ignore logistics.
- Do NOT make the final business decision.
- Return ONLY valid JSON.
- When Waste Risk is Low, do NOT automatically recommend Food Donation,
  Animal Feed, or Compost.
- Food Donation should only be selected when there is evidence that
  commercial sale is unsuitable or waste is becoming likely.
- For Low Waste Risk, prefer "Immediate Sale" unless the supplied
  sustainability data clearly supports another strategy.
- Your reasoning MUST use ONLY Waste Risk.
- Do NOT mention freshness, quality, market conditions, demand, or logistics.
""",
        expected_output="""
{
  "waste_risk_level": "Low | Moderate | High | Critical",
  "waste_likelihood": "Low | Moderate | High | Critical",
  "environmental_concern": "string",
  "strategy": "Immediate Sale | Cold Storage | Food Processing | Food Donation | Animal Feed | Compost",
  "confidence": 0,
  "reasoning": "string"
}
""",
        agent=agent,
    )