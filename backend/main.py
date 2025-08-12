from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Literal, Dict, Tuple

app = FastAPI(title="Medical Terminology Analyzer")

# temp vocab, just for structure
VOCAB: Dict[str, Dict[str, str]] = {
    "hypo": {
        "type": "prefix",
        "meaning": "low/below/insufficient",
        "image_url": "/images/hypo.png",
    },
    "hyper": {
        "type": "prefix",
        "meaning": "high/excessive",
        "image_url": "/images/hyper.png",
    },
    "glyc": {
        "type": "root",
        "meaning": "sugar/glucose",
        "image_url": "/images/glucose.png",
    },
    "cardi": {"type": "root", "meaning": "heart", "image_url": "/images/heart.png"},
    "hem": {"type": "root", "meaning": "blood", "image_url": "/images/blood.png"},
    "itis": {
        "type": "suffix",
        "meaning": "inflammation",
        "image_url": "/images/inflammation.png",
    },
    "emia": {
        "type": "suffix",
        "meaning": "blood condition",
        "image_url": "/images/blood_cond.png",
    },
}

# token schema
class Token(BaseModel):
    part: str
    status: Literal["ok", "unknown"]
    type: Literal["prefix", "root", "suffix"] | None = None
    meaning: str | None = None
    image_url: str | None = None
    
# analyze reponse schema
class AnalyzeResponse(BaseModel):
    term: str
    normalized: str
    tokens: List[Token]
    valid_structure: bool
    
