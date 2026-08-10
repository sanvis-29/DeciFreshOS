import json
from pathlib import Path


class HistoricalRAG:
    """
    Retrieves historically similar produce batches.
    """

    def __init__(self):
        data_path = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "historical_batches.json"
        )

        with open(data_path, "r", encoding="utf-8") as file:
            self.history = json.load(file)

    def retrieve_similar(self, batch: dict, top_k: int = 3):
        scored_batches = []

        for past_batch in self.history:
            distance = self._calculate_distance(
                current=batch,
                past=past_batch,
            )

            scored_batches.append({
                "distance": distance,
                "record": past_batch,
            })

        scored_batches.sort(
            key=lambda item: item["distance"]
        )

        return [
            item["record"]
            for item in scored_batches[:top_k]
        ]

    def _calculate_distance(self, current: dict, past: dict):
        fields = [
            "freshness",
            "market_price",
            "demand",
            "logistics",
            "waste_risk",
        ]

        distance = sum(
            abs(current[field] - past[field])
            for field in fields
        )

        # Prefer matches of the same produce type
        if current.get("produce_type") != past.get("produce_type"):
            distance += 20

        return distance