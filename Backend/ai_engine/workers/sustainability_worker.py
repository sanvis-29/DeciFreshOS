from crewai import Agent
from Backend.ai_engine.config import llm

sustainability_worker = Agent(
    role="Sustainability & Food Waste Expert",
    goal="Reduce waste while maximizing environmental and social impact.",
    backstory=(
        "You are an expert in food waste reduction, circular economy, "
        "food donation strategies, composting, and sustainable supply chains."
    ),
    llm=llm,
    verbose=True,
)