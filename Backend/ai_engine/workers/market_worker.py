from crewai import Agent
from Backend.ai_engine.config import llm

market_worker = Agent(
    role="Market Intelligence Analyst",
    goal="Analyze demand, pricing trends, and market opportunities.",
    backstory=(
        "You are a market analyst specializing in fresh produce economics. "
        "You understand customer demand, seasonal pricing, competition, "
        "and profit optimization."
    ),
    llm=llm,
    verbose=True,
)