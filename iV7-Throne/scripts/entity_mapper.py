#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path
ENTITY_RE = re.compile(r"\b([A-Z][a-z]+(?:\s+(?:Corp|Inc|LLC|Ltd|Company|Group|Holdings|Corporation|Partners))?)\b")

def extract_entities(text):
    seen, out = set(), []
    for m in ENTITY_RE.finditer(text):
        ent = m.group(1).strip()
        if ent not in seen and len(ent) > 3:
            seen.add(ent); out.append(ent)
    return out

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", default="reports/entities.json")
    args = p.parse_args()
    text = Path(args.input).read_text(encoding="utf-8")
    Path(args.output).write_text(json.dumps({"entities": extract_entities(text)}, indent=2), encoding="utf-8")
