from crewai import Task


def create_quality_task(agent, freshness):
    """
    Creates the Produce Quality task.
    """

    return Task(
        description=f"""
You are the Produce Quality Expert.

Analyze ONLY the produce quality.

Freshness Score:
{freshness}

Your responsibilities:

1. Determine the quality grade
   (Premium / Good / Average / Poor)

2. State whether this produce is suitable for:
   - Premium Retail
   - Standard Retail
   - Processing

3. Explain your reasoning in 3-4 sentences.

IMPORTANT:
- ONLY evaluate quality.
- Ignore market price.
- Ignore demand.
- Ignore logistics.
- Ignore sustainability.
- Do NOT recommend a final business action.
- Return ONLY valid JSON.
- Confidence MUST be an integer from 0 to 100.
- Base confidence on how clearly the Freshness Score fits the quality assessment.
- Do NOT return 0 confidence unless the input is missing, invalid, or contradictory.
""",
        expected_output="""
{
  "quality_grade": "Premium | Good | Average | Poor",
  "premium_suitable": true,
  "standard_suitable": true,
  "processing_suitable": false,
  "confidence": 0,
  "reasoning": "string"
}
""",
        agent=agent,
    )