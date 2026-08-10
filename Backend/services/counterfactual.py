from api.schemas import CounterfactualAnalysis

def compute_counterfactual_impact(
    total_weight_kg: float,
    baseline_revenue: float,
    baseline_waste_pct: float,
    optimal_revenue: float,
    optimal_waste_pct: float
) -> CounterfactualAnalysis:
    
    # Calculate physical waste deltas
    baseline_waste_kg = total_weight_kg * (baseline_waste_pct / 100.0)
    optimal_waste_kg = total_weight_kg * (optimal_waste_pct / 100.0)
    waste_prevented_kg = max(0.0, baseline_waste_kg - optimal_waste_kg)
    
    # Economic impact
    revenue_protected = max(0.0, optimal_revenue - baseline_revenue)
    
    # Social & Environmental Conversions (Industry standard fresh produce metrics)
    # 1 kg saved produce approx = 2.5 meals enabled (0.4kg / meal)
    # 1 kg food waste diverted approx = 2.2 kg CO2e avoided
    meals_enabled = int(waste_prevented_kg * 2.5)
    co2_avoided_kg = round(waste_prevented_kg * 2.2, 2)

    return CounterfactualAnalysis(
        do_nothing_revenue_inr=round(baseline_revenue, 2),
        do_nothing_waste_pct=round(baseline_waste_pct, 2),
        optimal_revenue_inr=round(optimal_revenue, 2),
        optimal_waste_pct=round(optimal_waste_pct, 2),
        revenue_protected_inr=round(revenue_protected, 2),
        waste_prevented_kg=round(waste_prevented_kg, 2),
        meals_enabled=meals_enabled,
        co2_avoided_kg=co2_avoided_kg
    )