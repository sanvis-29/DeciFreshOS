class DecisionEngine:
    def __init__(self):
        self.weights = {
            "freshness": 0.30,
            "market_price": 0.25,
            "demand": 0.20,
            "logistics": 0.15,
            "waste_risk": 0.10,
        }

    def score_batch(self, batch):
        score = (
            batch["freshness"] * self.weights["freshness"]
            + batch["market_price"] * self.weights["market_price"]
            + batch["demand"] * self.weights["demand"]
            + batch["logistics"] * self.weights["logistics"]
            + batch["waste_risk"] * self.weights["waste_risk"]
        )

        return round(score, 2)

    def choose_action(self, score):
        if score >= 80:
            return "Sell to Premium Retail"

        elif score >= 60:
            return "Sell to Standard Retail"

        elif score >= 40:
            return "Redirect to Food Processing"

        else:
            return "Donate / Relief Network"