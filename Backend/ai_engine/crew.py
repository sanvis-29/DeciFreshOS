from crewai import Crew, Process

from backend.crewai.agents import (
    vision_agent,
    market_agent,
    logistics_agent,
    institution_agent,
    decision_orchestrator,
)

from backend.crewai.tasks import (
    vision_task,
    market_task,
    logistics_task,
    institution_task,
    decision_task,
)


decifresh_crew = Crew(
    agents=[
        vision_agent,
        market_agent,
        logistics_agent,
        institution_agent,
        decision_orchestrator,
    ],

   tasks=[
    quality_task,
    market_task,
    logistics_task,
    sustainability_task,
    chief_task,
    validator_task,
],

    process=Process.sequential,

    verbose=True,
)


def run_decifresh(batch_data: dict):
    """
    Runs the complete DeciFresh AI workflow.

    Args:
        batch_data (dict): Information about the produce batch.

    Returns:
        Crew Output
    """

    result = decifresh_crew.kickoff(
        inputs=batch_data
    )

    return result
