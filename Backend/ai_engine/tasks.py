from crewai import Task  # type: ignore[import]
from ai_engine.agents import (
    vision_agent,
    market_agent,
    logistics_agent,
    decision_agent,
    counterfactual_agent,
    explainability_agent,
)


def create_tasks(batch_data: dict):
    """
    Creates all CrewAI tasks for one produce batch.
    """

    vision_task = Task(
        description=f"""
        Analyze the following produce batch.

        Batch Data:
        {batch_data}

        Estimate:
        - Freshness
        - Visible defects
        - Shelf life
        """,
        expected_output="Quality assessment of the produce batch.",
        agent=vision_agent,
    )

    market_task = Task(
        description=f"""
        Using the batch details below:

        {batch_data}

        Predict:
        - Best market
        - Selling price
        - Demand
        """,
        expected_output="Market recommendation.",
        agent=market_agent,
    )

    logistics_task = Task(
        description=f"""
        Given this produce batch:

        {batch_data}

        Recommend:
        - Best transport route
        - Delivery urgency
        - Logistics strategy
        """,
        expected_output="Logistics recommendation.",
        agent=logistics_agent,
    )

    decision_task = Task(
        description="""
        Combine all previous analyses.

        Recommend ONE action:
        - Sell
        - Store
        - Process
        - Donate
        """,
        expected_output="Final business decision.",
        agent=decision_agent,
    )

    counterfactual_task = Task(
        description="""
        Estimate what happens if no action is taken.
        """,
        expected_output="Estimated losses and waste.",
        agent=counterfactual_agent,
    )

    explainability_task = Task(
        description="""
        Explain the final recommendation in plain English.
        """,
        expected_output="Human-friendly explanation.",
        agent=explainability_agent,
    )

    return [
        vision_task,
        market_task,
        logistics_task,
        decision_task,
        counterfactual_task,
        explainability_task,
    ]
