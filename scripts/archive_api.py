#!/usr/bin/env python3
"""Wayback lookup helpers for public archival research."""
import argparse, json, requests
WAYBACK_AVAILABLE = "https://archive.org/wayback/available"
WAYBACK_CDX = "https://web.archive.org/cdx/search/cdx"

def get_available_snapshot(url, timeout=30):
    r = requests.get(WAYBACK_AVAILABLE, params={"url": url}, timeout=timeout)
    r.raise_for_status()
    return r.json().get("archived_snapshots", {}).get("closest")

def get_cdx(url, limit=50, timeout=30):
    params = {"url": url, "output": "json", "limit": limit, "filter": "statuscode:200"}
    r = requests.get(WAYBACK_CDX, params=params, timeout=timeout)
    r.raise_for_status()
    rows = r.json()
    return [dict(zip(rows[0], row)) for row in rows[1:]] if rows else []

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--url", required=True)
    p.add_argument("--cdx", action="store_true")
    args = p.parse_args()
    out = {"url": args.url, "snapshot": get_available_snapshot(args.url)}
    if args.cdx: out["cdx"] = get_cdx(args.url)
    print(json.dumps(out, indent=2))
