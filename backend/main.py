from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Literal, Dict, Tuple
import re

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


# helper functions
def normalize(term: str) -> str:
    term = term.lower()
    term = re.sub(r"[^a-z ]", "", term)
    return term


def tokenize(term: str) -> List[Token]:
    s = normalize(term)
    tokens = []
    i = 0
    max_len = max(len(k) for k in VOCAB.keys())

    while i < len(s):
        best = None
        for j in range(min(len(s), i + max_len), i, -1):
            piece = s[i:j]
            if piece in VOCAB:
                best = piece
                break
        if best:
            meta = VOCAB[best]
            tokens.append(
                Token(
                    part=best,
                    status="ok",
                    type=meta["type"],
                    meaning=meta["meaning"],
                    image_url=meta["image_url"],
                )
            )
            i += len(best)
        else:
            # could possible implement a gemini fallback
            tokens.append(Token(part=s[i], status="unknown"))
            i += 1
    return tokens


@app.get("/analyze", response_model=AnalyzeReponse)
def analyze(term: str):
    if not term.strip():
        raise HTTPException(status_code=400, detail="empty term")
    tokens = tokenize(term)
    return AnalyzeResponse(
        term=term, normalized=normalize(term), tokens=tokens, valid_structure=True
    )
