import sqlite3

def init_db(path="passwords.db"):
    conn = sqlite3.connect(path)
    conn.execute("""CREATE TABLE IF NOT EXISTS password_history(
        id INTEGER PRIMARY KEY,
        hash TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
    conn.close()
