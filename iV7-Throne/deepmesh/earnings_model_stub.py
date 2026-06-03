#!/usr/bin/env python3
"""Stub for scoring public events. Replace with real model later."""

EVENT_WEIGHTS = {
    "10-K": 1.0,
    "10-Q": 0.8,
    "8-K": 0.9,
    "13F": 0.7,
    "press_release": 0.5,
    "news": 0.3
}

def score_event(event):
    """Score based on public event type only. No private data."""
    event_type = event.get("type", "unknown")
    base_score = EVENT_WEIGHTS.get(event_type, 0.1)
    return {
        "url": event.get("url"),
        "type": event_type,
        "score": base_score,
        "requires_human_review": True
    }
