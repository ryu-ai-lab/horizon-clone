"""Shared time helpers for Horizon."""

from datetime import datetime, timedelta, timezone


KST = timezone(timedelta(hours=9), "KST")


def current_digest_date() -> str:
    """Return the digest publication date in Korea Standard Time."""
    return datetime.now(KST).strftime("%Y-%m-%d")
