import os
import json
import base64
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

ROOT_DIR = Path(__file__).resolve().parents[2]

load_dotenv(
    ROOT_DIR / ".env",
    override=True,
)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_produce_image(
    image_bytes: bytes,
    mime_type: str
) -> dict:
    """
    Analyze visible produce quality from an uploaded image.

    This performs visual estimation only.
    It does NOT claim to measure internal spoilage or exact shelf life.
    """

    encoded_image = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    image_url = (
        f"data:{mime_type};base64,{encoded_image}"
    )

    prompt = """
You are the computer-vision quality inspection layer for DeciFresh.

Analyze the produce visible in this image.

You may evaluate ONLY visually observable characteristics.

Return:
- produce type
- estimated visual freshness score from 0 to 100
- quality grade
- visible issues
- confidence score

Freshness interpretation:
81-100 = Excellent visible freshness
61-80 = Good visible freshness
41-60 = Average visible freshness
0-40 = Poor visible freshness

Quality grade must be one of:
Premium
Good
Average
Poor

Possible visible issues include:
bruising
discoloration
wrinkling
mold
surface damage
decay
over-ripeness
under-ripeness

IMPORTANT:
- Do not invent weight.
- Do not infer market price.
- Do not infer demand.
- Do not infer logistics.
- Do not infer origin.
- Do not infer harvest date.
- Do not claim to detect internal spoilage.
- If the image is unclear, lower confidence.
- If no produce is clearly visible, say so.

Return ONLY valid JSON in exactly this structure:

{
  "produce_type": "string",
  "freshness_score": 0,
  "quality_grade": "Premium | Good | Average | Poor",
  "visible_issues": ["string"],
  "confidence": 0,
  "visual_summary": "string"
}
"""

    response = client.chat.completions.create(
        model="qwen/qwen3.6-27b",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        },
                    },
                ],
            }
        ],
        temperature=0.1,
    )

    raw = response.choices[0].message.content.strip()

    # Remove markdown fences if the model adds them
    if raw.startswith("```json"):
        raw = raw[7:]

    if raw.startswith("```"):
        raw = raw[3:]

    if raw.endswith("```"):
        raw = raw[:-3]

    raw = raw.strip()

    # Extract the JSON object if extra text appears
    start = raw.find("{")
    end = raw.rfind("}")

    if start == -1 or end == -1:
        raise ValueError(
            f"Vision model did not return valid JSON: {raw}"
        )

    raw_json = raw[start:end + 1]

    result = json.loads(raw_json)

    # Normalize confidence to 0–100
    confidence = result.get("confidence", 0)

    if isinstance(confidence, (int, float)) and 0 <= confidence <= 1:
        result["confidence"] = round(confidence * 100)

    return result

