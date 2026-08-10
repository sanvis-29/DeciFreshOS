from typing import List, Dict


def generate_explanation(
    recommendation: str,
    destination: str,
    confidence: float,
    reasons: List[str],
):
    """
    Converts the AI recommendation into an easy-to-understand explanation.
    """

    explanation = {
        "title": f"Recommended Action: {recommendation}",

        "destination": destination,

        "confidence": f"{confidence:.0f}%",

        "summary": (
            f"DeciFresh recommends '{recommendation}' "
            f"because it provides the highest overall value "
            f"while minimizing waste."
        ),

        "reasoning": reasons
    }

    return explanation
