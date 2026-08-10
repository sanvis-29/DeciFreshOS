from datetime import datetime

from Backend.ai_engine.orchestrator import run_decifresh


def build_ai_batch(batch_data: dict) -> dict:
    """
    Convert frontend/API batch metadata into the numeric inputs
    required by the DeciFresh AI engine.

    NOTE:
    These are temporary MVP scoring rules.
    Replace later with real sensor/market/logistics data if available.
    """

    # -----------------------------
    # Freshness score
    # -----------------------------

    vision_freshness = batch_data.get("vision_freshness")

    if vision_freshness is not None:
        freshness = max(0, min(100, float(vision_freshness)))
    else:
        harvest_date = datetime.strptime(
            batch_data["harvest_date"],
            "%Y-%m-%d"
        ).date()

        today = datetime.now().date()

        days_since_harvest = (today - harvest_date).days

        freshness = max(
            0,
            min(
                100,
                100 - (days_since_harvest * 8)
            )
        )

    # -----------------------------
    # MVP default scores
    # -----------------------------

    market_price = 70
    demand = 75
    logistics = 80

    # Higher freshness = lower waste risk
    waste_risk = max(
        0,
        min(
            100,
            100 - freshness
        )
    )

    # -----------------------------
    # AI-compatible batch
    # -----------------------------

    return {
        "batch_id": batch_data["batch_id"],
        "produce_type": batch_data["crop_type"],
        "quantity_kg": batch_data["weight_kg"],

        "freshness": freshness,
        "market_price": market_price,
        "demand": demand,
        "logistics": logistics,
        "waste_risk": waste_risk,
    }


def process_decision(batch_data: dict):
    ai_batch = build_ai_batch(batch_data)

    return run_decifresh(ai_batch)