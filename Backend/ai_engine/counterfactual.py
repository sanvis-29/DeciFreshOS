class CounterfactualSimulator:
    """
    Simulates possible future actions for a produce batch
    and compares them against a 'do nothing' baseline.
    """

    ACTIONS = [
        "Premium Retail",
        "Standard Retail",
        "Discount Sale",
        "Cold Storage",
        "Food Processing",
        "Food Donation",
        "Animal Feed",
        "Compost",
    ]

    def simulate(self, batch: dict):
        scenarios = []

        baseline = self.calculate_baseline(batch)

        for action in self.ACTIONS:
            value = self._estimate_future_value(
                batch,
                action
            )

            scenarios.append({
                "action": action,
                "future_value": round(value, 2),
                "gain_vs_baseline": round(
                    value - baseline,
                    2
                ),
            })

        scenarios.sort(
            key=lambda x: x["future_value"],
            reverse=True
        )

        return {
            "baseline_future_value": baseline,
            "best_action": scenarios[0]["action"],
            "best_future_value": scenarios[0]["future_value"],
            "value_saved_vs_baseline":
                scenarios[0]["gain_vs_baseline"],
            "scenarios": scenarios,
        }

    def calculate_baseline(self, batch: dict):
        """
        Represents the future value if no intervention
        is made for the produce batch.
        """

        freshness = batch["freshness"]
        market_price = batch["market_price"]
        demand = batch["demand"]
        logistics = batch["logistics"]
        waste_risk = batch["waste_risk"]

        baseline = (
            freshness * 0.20
            + market_price * 0.20
            + demand * 0.15
            + logistics * 0.10
            + (100 - waste_risk) * 0.05
        )

        return round(baseline, 2)

    def _estimate_future_value(
        self,
        batch: dict,
        action: str
    ):
        freshness = batch["freshness"]
        market_price = batch["market_price"]
        demand = batch["demand"]
        logistics = batch["logistics"]
        waste_risk = batch["waste_risk"]

        base_value = (
            freshness * 0.30
            + market_price * 0.25
            + demand * 0.20
            + logistics * 0.15
            + (100 - waste_risk) * 0.10
        )

        modifiers = {
            "Premium Retail":
                1.10
                if freshness >= 80 and demand >= 60
                else 0.65,

            "Standard Retail":
                1.00
                if freshness >= 50
                else 0.70,

            "Discount Sale":
                0.90
                if freshness >= 35
                else 0.65,

            "Cold Storage":
                0.95
                if waste_risk <= 60
                else 0.60,

            "Food Processing":
                0.85
                if freshness >= 25
                else 0.65,

            "Food Donation":
                0.70
                if freshness >= 30
                else 0.50,

            "Animal Feed": 0.45,

            "Compost": 0.20,
        }

        return base_value * modifiers[action]