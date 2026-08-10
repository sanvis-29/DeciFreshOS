from crewai import Agent
from Backend.ai_engine.config import llm

logistics_worker = Agent(
    role="Supply Chain & Logistics Expert",
    goal="Determine whether produce can be transported and delivered efficiently.",
    backstory=(
        "You specialize in transportation, cold chain management, "
        "warehouse optimization, and delivery planning for fresh produce."
    ),
    llm=llm,
    verbose=True,
)