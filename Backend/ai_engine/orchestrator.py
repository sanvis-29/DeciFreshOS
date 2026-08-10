import Crew, Process

from Backend.models.decision import DecisionEngine
from Backend.ai_engine.counterfactual import CounterfactualSimulator
from Backend.ai_engine.historical_rag import HistoricalRAG

from Backend.ai_engine.workers.quality_worker import quality_worker
from Backend.ai_engine.workers.market_worker import market_worker
from Backend.ai_engine.workers.logistics_worker import logistics_worker
from Backend.ai_engine.workers.sustainability_worker import sustainability_worker
from Backend.ai_engine.workers.chief_worker import chief_worker
from Backend.ai_engine.workers.validator import validator_agent

from Backend.ai_engine.working.quality_task import create_quality_task
from Backend.ai_engine.working.market_task import create_market_task
from Backend.ai_engine.working.logistics_task import create_logistics_task
from Backend.ai_engine.working.sustainability_task import create_sustainability_task
from Backend.ai_engine.working.chief_task import create_chief_task
from Backend.ai_engine.working.validator_task import create_validator_task
def run_decifresh(batch: dict):
    """
    Runs the complete DeciFresh decision pipeline.

    Input:
        batch: dictionary containing produce metrics

    Output:
        dictionary containing:
        - deterministic decision engine result
        - counterfactual analysis
        - final validated AI decision
    """

    # ==========================================
    # 1. DETERMINISTIC DECISION ENGINE
    # ==========================================

    engine = DecisionEngine()

    score = engine.score_batch(batch)
    engine_action = engine.choose_action(score)

    # Normalize action name for cleaner output
    normalized_engine_action = engine_action.replace("Sell to ", "")

    # ==========================================
    # 2. COUNTERFACTUAL SIMULATION
    # ==========================================

    simulator = CounterfactualSimulator()

    counterfactuals = simulator.simulate(batch)

    # ==========================================
    # 3. HISTORICAL RAG
    # ==========================================

    historical_rag = HistoricalRAG()

    historical_matches = historical_rag.retrieve_similar(
    batch=batch,
    top_k=3,
)

    # ==========================================
    # 4. CREATE SPECIALIST TASKS
    # ==========================================

    quality_task = create_quality_task(
        agent=quality_worker,
        freshness=batch["freshness"],
    )

    market_task = create_market_task(
        agent=market_worker,
        market_price=batch["market_price"],
        demand=batch["demand"],
    )

    logistics_task = create_logistics_task(
        agent=logistics_worker,
        logistics_score=batch["logistics"],
    )

    sustainability_task = create_sustainability_task(
        agent=sustainability_worker,
        waste_risk=batch["waste_risk"],
    )

    # ==========================================
    # 5. CHIEF DECISION TASK
    # ==========================================

    chief_task = create_chief_task(
    agent=chief_worker,
    quality_task=quality_task,
    market_task=market_task,
    logistics_task=logistics_task,
    sustainability_task=sustainability_task,
    historical_matches=historical_matches,
    counterfactual_analysis=counterfactuals,

    )

    # ==========================================
    # 5. VALIDATOR TASK
    # ==========================================

    validator_task = create_validator_task(
        agent=validator_agent,
        score=score,
        engine_action=normalized_engine_action,
        chief_task=chief_task,
    )

    # ==========================================
    # 6. CREATE CREW
    # ==========================================

    crew = Crew(
        agents=[
            quality_worker,
            market_worker,
            logistics_worker,
            sustainability_worker,
            chief_worker,
            validator_agent,
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

    # ==========================================
    # 7. RUN CREW
    # ==========================================

    result = crew.kickoff()

    # Convert CrewAI output to string
    raw_output = str(result)

    # ==========================================
    # 8. PARSE FINAL VALIDATOR JSON
    # ==========================================

    try:
        final_decision = json.loads(raw_output)

    except json.JSONDecodeError:
        final_decision = {
            "validation_status": "PARSE_ERROR",
            "final_recommendation": normalized_engine_action,
            "confidence": 0,
            "engine_agreement": "UNKNOWN",
            "reasoning": raw_output,
        }

    # ==========================================
    # 9. FINAL DECIFRESH RESPONSE
    # ==========================================

    return {
        "batch_id": batch.get("batch_id"),
        "produce_type": batch.get("produce_type"),
        "quantity_kg": batch.get("quantity_kg"),

        "decision_engine": {
            "score": score,
            "recommendation": normalized_engine_action,
        },

        "counterfactual_analysis": counterfactuals,
        "historical_matches": historical_matches,

        "ai_decision": final_decision,
    }