import sqlite3
from pathlib import Path

DB_NAME = "users.db"


def get_conn():
    return sqlite3.connect(DB_NAME)


def init_db():
    # Maak DB file aan als die niet bestaat
    Path(DB_NAME).touch(exist_ok=True)

    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                firstname TEXT,
                lastname TEXT,
                created_at TEXT NOT NULL
            );
        """)
        
        # Migraties voor bestaande databases (voeg kolommen toe als ze missen)
        try:
            cur.execute("ALTER TABLE users ADD COLUMN firstname TEXT")
        except sqlite3.OperationalError:
            pass  # Kolom bestaat al

        try:
            cur.execute("ALTER TABLE users ADD COLUMN lastname TEXT")
        except sqlite3.OperationalError:
            pass  # Kolom bestaat al

        conn.commit()
