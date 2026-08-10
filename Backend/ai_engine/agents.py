from crewai import Agent
from ai_engine.config import llm


market_agent = Agent(
    role="Market Intelligence Agent",
    goal="Predict demand, pricing trends and identify the best market for each produce batch.",
    backstory=(
        "You are an agricultural market analyst who understands "
        "regional demand, seasonal trends, price fluctuations and buyer behavior."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)


logistics_agent = Agent(
    role="Logistics Intelligence Agent",
    goal="Recommend the fastest and most cost-effective routing for produce.",
    backstory=(
        "You specialize in transportation, cold-chain logistics, delivery timing "
        "and warehouse optimization."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)


vision_agent = Agent(
    role="Vision Intelligence Agent",
    goal="Estimate produce quality and remaining shelf life.",
    backstory=(
        "You analyze computer vision results such as freshness score, defects "
        "and visible spoilage."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)


decision_agent = Agent(
    role="Produce Decision Agent",
    goal="Choose the highest-value future for every produce batch.",
    backstory=(
        "You combine predictions from every AI system and recommend "
        "the single best action."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)


counterfactual_agent = Agent(
    role="Counterfactual AI Agent",
    goal="Estimate what would happen if no action were taken.",
    backstory=(
        "You compare the recommended decision with doing nothing "
        "and calculate value saved."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)


explainability_agent = Agent(
    role="Explainability Agent",
    goal="Explain every recommendation in simple business language.",
    backstory=(
        "You convert AI outputs into clear explanations that supply-chain "
        "managers can understand."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)
