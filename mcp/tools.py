import sqlite3

DB_PATH = "storage/events.db"

def get_alerts(limit: int = 10):
    """
    Return recent security anomalies.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, src, dst, size FROM events ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": r[0],
            "src": r[1],
            "dst": r[2],
            "size": r[3]
        }
        for r in rows
    ]


def get_alert_stats():
    """
    Return high-level anomaly statistics.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM events")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT src) FROM events")
    unique_sources = cursor.fetchone()[0]

    conn.close()

    return {
        "total_alerts": total,
        "unique_sources": unique_sources
    }
