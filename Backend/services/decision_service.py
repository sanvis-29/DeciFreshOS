from datetime import datetime

from Backend.ai_engine.orchestrator import run_decifresh


def build_ai_batch(batch_data: dict) -> dict:
    """Convert batch metadata into the numeric inputs expected by the AI engine."""

    freshness = batch_data.get("vision_freshness")

    if freshness is None:
        harvest_date = batch_data.get("harvest_date")
        if harvest_date:
            try:
                harvest_date = datetime.strptime(harvest_date, "%Y-%m-%d").date()
                today = datetime.now().date()
                freshness = max(0, min(100, 100 - ((today - harvest_date).days * 8)))
            except ValueError:
                freshness = 70
        else:
            freshness = 70
    else:
        freshness = max(0, min(100, float(freshness)))

    market_price = batch_data.get("market_price", 65)
    demand = batch_data.get("demand", 68)
    logistics = batch_data.get("logistics", 72)
    waste_risk = max(0, min(100, 100 - freshness))

    return {
        "batch_id": batch_data.get("batch_id"),
        "produce_type": batch_data.get("crop_type"),
        "quantity_kg": batch_data.get("weight_kg"),
        "freshness": freshness,
        "market_price": market_price,
        "demand": demand,
        "logistics": logistics,
        "waste_risk": waste_risk,
    }


def process_decision(batch_data: dict):
    intelligence_input = build_ai_batch(batch_data)
    return run_decifresh(intelligence_input)
