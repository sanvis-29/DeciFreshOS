from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class BatchCreateRequest(BaseModel):
    batch_id: str = Field(..., example="MX-201")
    crop_type: str = Field(..., example="Mangoes")
    weight_kg: float = Field(..., example=1000.0)
    origin: str = Field(..., example="Farm A, Azadpur")
    harvest_date: str = Field(..., example="2026-08-05")
    current_location: str = Field(..., example="Delhi Warehouse")
    vision_freshness: Optional[float] = None

class AgentInsight(BaseModel):
    agent_name: str
    finding: str

class DecisionScenario(BaseModel):
    scenario_id: str
    destination: str
    allocation_kg: float
    expected_revenue_inr: float
    waste_percentage: float
    preservation_score: float

class CounterfactualAnalysis(BaseModel):
    do_nothing_revenue_inr: float
    do_nothing_waste_pct: float
    optimal_revenue_inr: float
    optimal_waste_pct: float
    revenue_protected_inr: float
    waste_prevented_kg: float
    meals_enabled: int
    co2_avoided_kg: float

class DecisionResponse(BaseModel):
    batch_id: str
    crop_type: str
    weight_kg: float
    value_preservation_score: float
    confidence_score: float
    recommended_action: str
    explanation: List[str]
    scenarios_evaluated: List[DecisionScenario]
    counterfactual: CounterfactualAnalysis
    agent_insights: List[AgentInsight]
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class ProducePassport(BaseModel):
    passport_id: str
    batch_id: str
    crop_type: str
    weight_kg: float
    origin: str
    harvest_date: str
    current_value_preservation_score: float
    quality_grade: str
    route_history: List[str]
    qr_code_url: str