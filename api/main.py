from fastapi import FastAPI
import sqlite3

app = FastAPI(title="AI Self-Hosted Security Device")

DB_PATH = "storage/events.db"

@app.get("/")
def health():
    return {"status": "running"}

@app.get("/alerts")
def get_alerts():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, src, dst, size FROM events ORDER BY id DESC")
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
