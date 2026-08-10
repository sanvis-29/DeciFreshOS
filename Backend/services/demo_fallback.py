def get_standard_apple_demo(batch_data: dict):

    return {
        "batch_id": batch_data.get("batch_id", "MX-201"),
        "produce_type": batch_data.get("crop_type", "Apple"),
        "quantity_kg": batch_data.get("weight_kg", 1000),

        "demo_mode": True,

        "decision_engine": {
            "score": 66.5,
            "recommendation": "Standard Retail"
        },

        "counterfactual_analysis": {
            "baseline_future_value": 48.25,
            "best_action": "Standard Retail",
            "best_future_value": 68.5,
            "value_saved_vs_baseline": 20.25,

            "scenarios": [
                {
                    "action": "Standard Retail",
                    "future_value": 68.5,
                    "gain_vs_baseline": 20.25
                },
                {
                    "action": "Cold Storage",
                    "future_value": 65.4,
                    "gain_vs_baseline": 17.15
                },
                {
                    "action": "Discount Sale",
                    "future_value": 62.8,
                    "gain_vs_baseline": 14.55
                },
                {
                    "action": "Food Processing",
                    "future_value": 59.7,
                    "gain_vs_baseline": 11.45
                },
                {
                    "action": "Food Donation",
                    "future_value": 49.1,
                    "gain_vs_baseline": 0.85
                },
                {
                    "action": "Premium Retail",
                    "future_value": 44.9,
                    "gain_vs_baseline": -3.35
                },
                {
                    "action": "Animal Feed",
                    "future_value": 31.5,
                    "gain_vs_baseline": -16.75
                },
                {
                    "action": "Compost",
                    "future_value": 14.2,
                    "gain_vs_baseline": -34.05
                }
            ]
        },

        "historical_matches": [
            {
                "batch_id": "H-002",
                "produce_type": "Apple",
                "freshness": 72,
                "market_price": 66,
                "demand": 70,
                "logistics": 74,
                "waste_risk": 32,
                "decision": "Standard Retail",
                "outcome": "Most produce sold through standard retail",
                "waste_percent": 7
            },
            {
                "batch_id": "H-006",
                "produce_type": "Apple",
                "freshness": 68,
                "market_price": 64,
                "demand": 67,
                "logistics": 71,
                "waste_risk": 38,
                "decision": "Standard Retail",
                "outcome": "Batch sold successfully",
                "waste_percent": 9
            },
            {
                "batch_id": "H-004",
                "produce_type": "Apple",
                "freshness": 79,
                "market_price": 72,
                "demand": 75,
                "logistics": 76,
                "waste_risk": 24,
                "decision": "Standard Retail",
                "outcome": "High sell-through with limited waste",
                "waste_percent": 5
            }
        ],

        "ai_decision": {
            "validation_status": "APPROVED",
            "final_recommendation": "Standard Retail",
            "confidence": 90,
            "engine_agreement": "AGREE",
            "reasoning": (
                "The batch shows commercially viable standard-retail quality. "
                "Its visual condition, market suitability, logistics feasibility, "
                "historical outcomes and counterfactual analysis support Standard "
                "Retail as the strongest value-preserving destination."
            )
        }
    }
