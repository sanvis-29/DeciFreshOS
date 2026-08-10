from crewai import Task


def create_chief_task(
    agent,
    quality_task,
    market_task,
    logistics_task,
    sustainability_task,
    historical_matches,
    counterfactual_analysis,
):
    """
    Creates the Chief Produce Decision Officer task.

    The Chief combines:
    - specialist reports
    - historical similar cases
    - counterfactual scenario analysis

    and selects one final business action.
    """

    return Task(
        description=f"""
You are the Chief Produce Decision Officer.

Your job is to make ONE final business recommendation for the current produce batch.

You have access to structured reports from:

1. Produce Quality Expert
2. Market Intelligence Analyst
3. Supply Chain & Logistics Expert
4. Sustainability & Food Waste Expert

You also have access to similar historical batches:

{historical_matches}

HISTORICAL RAG RULES:

- Historical cases are supporting evidence only.
- Do NOT blindly copy a historical decision.
- The current batch and current specialist reports are more important.
- Use historical outcomes to strengthen or weaken your confidence.
- Prefer historical cases that are genuinely similar.
- Do NOT invent historical batches.
- Do NOT invent historical outcomes.
- Do NOT claim historical evidence exists unless it is included above.

You also have access to counterfactual scenario analysis:

{counterfactual_analysis}

COUNTERFACTUAL RULES:

- Counterfactual results are supporting evidence only.
- Do NOT automatically choose the action with the highest future value.
- Use the scenarios to compare trade-offs between possible actions.
- Consider the best_action, best_future_value, baseline_future_value,
  value_saved_vs_baseline, and scenario rankings.
- If the highest-ranked counterfactual conflicts with specialist reports
  or historical evidence, explain why you do or do not follow it.
- Do NOT invent counterfactual scores.
- Do NOT modify the provided counterfactual values.
- Only use scenario information explicitly provided above.

Using all available evidence, choose exactly ONE final business action.

Possible actions:

- Premium Retail
- Standard Retail
- Discount Sale
- Cold Storage
- Food Processing
- Food Donation
- Animal Feed
- Compost

Decision principles:

- Premium Retail requires strong produce quality AND strong market conditions.

- Standard Retail is preferred when quality is commercially viable but
  premium conditions are not clearly justified.

- Discount Sale is suitable when produce can still be sold but value
  is weakening or faster clearance is desirable.

- Cold Storage is appropriate when delaying the sale may preserve value
  and waste risk remains manageable.

- Food Processing is appropriate when retail quality is insufficient
  but the produce still has usable commercial value.

- Food Donation is appropriate when commercial value is weak but the
  produce is still suitable for human use.

- Animal Feed is appropriate when the produce is not suitable for normal
  human consumption but may still have feed value.

- Compost is a last-resort option when other edible or commercial uses
  are no longer reasonable.

Your responsibilities:

1. Select exactly ONE final recommendation.

2. Give a confidence score from 0 to 100.

3. State the primary factor that most influenced the decision.

4. Explain how the specialist reports support the recommendation.

5. Explain whether the historical cases strengthen, weaken, or do not
   materially affect the recommendation.

6. Explain how the counterfactual analysis affects the recommendation.

IMPORTANT:

- Do NOT invent new scores or facts.
- Do NOT invent prices, revenue, routes, storage capacity, shelf life,
  customers, or quantities.
- Do NOT choose Premium Retail based on freshness alone.
- Consider ALL FOUR specialist reports.
- Historical evidence must remain secondary to current-batch evidence.
- Counterfactual evidence must remain advisory, not authoritative.
- Do NOT blindly choose the counterfactual best_action.
- Do NOT provide multiple final recommendations.
- Return ONLY valid JSON.
""",
        expected_output="""
{
  "final_recommendation": "Premium Retail | Standard Retail | Discount Sale | Cold Storage | Food Processing | Food Donation | Animal Feed | Compost",
  "confidence": 0,
  "primary_factor": "string",
  "historical_evidence": "string",
  "counterfactual_evidence": "string",
  "reasoning": "string"
}
""",
        agent=agent,
        context=[
            quality_task,
            market_task,
            logistics_task,
            sustainability_task,
        ],
    )