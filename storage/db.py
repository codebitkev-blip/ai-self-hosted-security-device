import sqlite3
import os

DB_PATH = "storage/events.db"

os.makedirs("storage", exist_ok=True)
conn = sqlite3.connect(DB_PATH, check_same_thread=False)

conn.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    src TEXT,
    dst TEXT,
    size INTEGER
)
""")
conn.commit()

def log_event(packet):
    conn.execute(
        "INSERT INTO events (src, dst, size) VALUES (?, ?, ?)",
        (packet["src"], packet["dst"], packet["size"])
    )
    conn.commit()
