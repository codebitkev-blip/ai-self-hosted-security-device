from fastapi import FastAPI
import sqlite3
from api.schemas import Alert, AlertStats

# NOTE:
# This API is intentionally designed for local-only access.
# Do NOT expose publicly without authentication and TLS.

DB_PATH = "storage/events.db"

app = FastAPI(
    title="AI Self-Hosted Security Device API",
    description="Local-only API exposing detected network anomalies and security insights",
    version="1.0.0"
)


@app.get(
    "/",
    summary="Health check",
    description="Verify that the security device API is running"
)
def health():
    return {"status": "running"}


@app.get(
    "/alerts",
    response_model=list[Alert],
    summary="List detected anomalies",
    description="Returns all detected anomalous network events in reverse chronological order"
)
def get_alerts():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, src, dst, size FROM events ORDER BY id DESC"
    )
    rows = cursor.fetchall()
    conn.close()

    return [
        Alert(id=r[0], src=r[1], dst=r[2], size=r[3])
        for r in rows
    ]


@app.get(
    "/alerts/stats",
    response_model=AlertStats,
    summary="Get alert statistics",
    description="Provides a high-level summary of detected anomalies"
)
def alert_stats():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM events")
    total_alerts = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT src) FROM events")
    unique_sources = cursor.fetchone()[0]

    conn.close()

    return AlertStats(
        total_alerts=total_alerts,
        unique_sources=unique_sources
    )


@app.get(
    "/alerts/by-source/{ip}",
    response_model=list[Alert],
    summary="Filter alerts by source IP",
    description="Returns anomalies originating from a specific source IP"
)
def alerts_by_source(ip: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, src, dst, size FROM events WHERE src = ? ORDER BY id DESC",
        (ip,)
    )
    rows = cursor.fetchall()
    conn.close()

    return [
        Alert(id=r[0], src=r[1], dst=r[2], size=r[3])
        for r in rows
    ]

