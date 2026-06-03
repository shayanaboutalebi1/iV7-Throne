#!/usr/bin/env python3
import argparse, json
from pathlib import Path

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--timeline", required=True)
    p.add_argument("--output", default="reports/report.md")
    args = p.parse_args()
    data = json.loads(Path(args.timeline).read_text(encoding="utf-8"))
    lines = ["# iV7-Throne Report", "", f"_Generated: {data.get('generated_at', 'N/A')}_", "", "## Timeline", ""]
    for day in data.get("timeline", []):
        lines.append(f"### {day['date']} ({day['count']} item(s))")
        for item in day["items"]:
            title = item.get("title") or item.get("url") or "Untitled"
            source = item.get("source") or item.get("url") or ""
            event_type = item.get("type", "unknown")
            lines.append(f"- **{title}** [{event_type}]")
            if source: lines.append(f" - Source: {source}")
        lines.append("")
    Path(args.output).write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {args.output}")
