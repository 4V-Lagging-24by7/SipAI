import sqlite3
from datetime import datetime
from pathlib import Path

# Always point to project root
BASE_DIR = Path(__file__).resolve().parent.parent
DB_NAME = BASE_DIR / "water_tracker.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS water_intake (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            intake_ml INTEGER NOT NULL,
            date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def log_intake(user_id: str, intake_ml: int):
    conn = get_connection()
    cursor = conn.cursor()

    date_today = datetime.today().strftime("%Y-%m-%d")

    cursor.execute(
        "INSERT INTO water_intake (user_id, intake_ml, date) VALUES (?, ?, ?)",
        (user_id, intake_ml, date_today)
    )

    conn.commit()
    conn.close()


def get_intake_history(user_id: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT intake_ml, date FROM water_intake WHERE user_id = ? ORDER BY id ASC",
        (user_id,)
    )

    rows = cursor.fetchall()
    conn.close()
    return rows


create_tables()











# import sqlite3
# from datetime import datetime

# DB_NAME = "water_tracker.db"


# def create_tables():
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS water_intake (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id TEXT,
#             intake_ml INTEGER,
#             date TEXT
#         )
#     """)

#     conn.commit()
#     conn.close()


# def log_intake(user_id, intake_ml):
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()

#     date_today = datetime.today().strftime('%Y-%m-%d')

#     cursor.execute(
#         "INSERT INTO water_intake (user_id, intake_ml, date) VALUES (?, ?, ?)",
#         (user_id, intake_ml, date_today)
#     )

# def get_intake_history(user_id):
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()

#     cursor.execute(
#         "SELECT intake_ml, date FROM water_intake WHERE user_id = ?",
#         (user_id,)
#     )

#     records = cursor.fetchall()
#     conn.close()
#     return records


# create_tables()