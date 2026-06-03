# iV7-Throne

Public-records archival research scaffold.

**Purpose**: Reconstruct timelines from Wayback Machine, SEC EDGAR, and other public archives. Citation-first. No targeting of private individuals.

### Guardrails
1. **Public records only**: SEC filings, archived pages, press releases, news.
2. **Citation required**: Every timeline item must include a `source` URL.
3. **No attribution without primary sources**: Human review required before any claims.
4. **Organizations only**: Entity extraction limited to orgs, not people.

### Quick Start
```bash
bash bootstrap_local.sh
python scripts/archive_api.py --url https://berkshirehathaway.com --cdx > data/snapshots/example.json
python scripts/timeline_builder.py --input data/sample_events.json --output reports/timeline.json
python scripts/report_generator.py --timeline reports/timeline.json
```

### Data Format
`data/sample_events.json` expects:
```json
[
  {
    "date": "20240115",
    "title": "Q4 Earnings Release",
    "type": "10-K",
    "url": "https://sec.gov/...",
    "source": "https://web.archive.org/web/..."
  }
]
```

### License
MIT - see LICENSE
