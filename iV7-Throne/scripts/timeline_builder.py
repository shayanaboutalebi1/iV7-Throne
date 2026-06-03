#!/usr/bin/env python3
import argparse, json
from collections import defaultdict
from pathlib import Path
from datetime import datetime

def normalize_date(ts):
    ts = str(ts)
    return f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}" if len(ts) >= 8 and ts[:8].isdigit() else ts

def build(input_path, output_path):
    events = json.loads(Path(input_path).read_text(encoding="utf-8"))
    grouped = defaultdict(list)
    for e in events:
        date = normalize_date(e.get("date",""))
        grouped[date].append(e)
    timeline = [{"date": d, "items": grouped[d], "count": len(grouped[d])} for d in sorted(grouped)]
    Path(output_path).write_text(json.dumps({
        "generated_at": datetime.utcnow().isoformat()+"Z",
        "timeline": timeline
    }, indent=2), encoding="utf-8")
    print(f"Wrote timeline to {output_path}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", default="reports/timeline.json")
    args = p.parse_args()
    build(args.input, args.output)
