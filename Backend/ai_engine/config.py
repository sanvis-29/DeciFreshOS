import os
from pathlib import Path

from dotenv import load_dotenv
from crewai import LLM

ROOT_DIR = Path(__file__).resolve().parents[2]

load_dotenv(
    ROOT_DIR / ".env",
    override=True,
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not found")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "groq/llama-3.3-70b-versatile",
)

temperature = 0.2
max_tokens = 2048

llm = LLM(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY,
    temperature=temperature,
)

VERBOSE = True
ALLOW_DELEGATION = False

VALUE_SCORE_MAX = 100
MIN_CONFIDENCE = 0.70

WEIGHTS = {
    "freshness": 0.30,
    "market_price": 0.25,
    "demand": 0.20,
    "logistics": 0.15,
    "waste_risk": 0.10,
}
