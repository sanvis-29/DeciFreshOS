from crewai.tools import tool
import random


# ==========================================================
# Market Price Tool
# ==========================================================

@tool("Get Current Market Prices")
def get_market_prices(produce_type: str):
    """
    Returns market prices for different cities.
    Replace with a real API later.
    """

    return {
        "Delhi": 42,
        "Gurgaon": 48,
        "Noida": 44
    }


# ==========================================================
# Demand Forecast Tool
# ==========================================================

@tool("Demand Forecast")
def get_demand_forecast(city: str):
    """
    Mock demand prediction.
    """

    forecasts = {
        "Delhi": "Stable",
        "Gurgaon": "Increasing",
        "Noida": "Moderate"
    }

    return forecasts.get(city, "Unknown")


# ==========================================================
# Weather Tool
# ==========================================================

@tool("Weather Information")
def get_weather(city: str):
    """
    Mock weather data.
    """

    return {
        "temperature": 36,
        "condition": "Sunny",
        "risk": "Low"
    }


# ==========================================================
# Logistics Tool
# ==========================================================

@tool("Estimate Logistics")
def estimate_logistics(source: str, destination: str):
    """
    Mock logistics estimation.
    """

    return {
        "distance_km": random.randint(20, 120),
        "travel_time_hours": round(random.uniform(1, 4), 1),
        "transport_cost": random.randint(3000, 9000)
    }


# ==========================================================
# Institutional Buyers Tool
# ==========================================================

@tool("Institution Finder")
def get_institutions(city: str):
    """
    Mock institutional demand.
    """

    return [
        {
            "name": "ABC University Hostel",
            "required_quantity": 300
        },
        {
            "name": "Fresh Juice Processor",
            "required_quantity": 200
        }
    ]


# ==========================================================
# Value Preservation Score
# ==========================================================

@tool("Calculate Value Preservation Score")
def calculate_value_score(
    freshness: float,
    demand: float,
    logistics: float,
    waste_risk: float
):
    """
    Simple weighted score.
    """

    score = (
        freshness * 0.35
        + demand * 0.30
        + logistics * 0.20
        + (100 - waste_risk) * 0.15
    )

    return round(score, 2)
