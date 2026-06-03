#!/usr/bin/env python3
import json
from pathlib import Path
from earnings_model_stub import score_event

def build_signals(timeline_path):
    data = json.loads(Path(timeline_path).read_text())
    signals = []
    for day in data.get("timeline", []):
        for item in day["items"]:
            signals.append(score_event(item))
    return signals

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--timeline", required=True)
    p.add_argument("--output", default="reports/signals.json")
    args = p.parse_args()
    signals = build_signals(args.timeline)
    Path(args.output).write_text(json.dumps(signals, indent=2))
    print(f"Wrote {args.output}")
