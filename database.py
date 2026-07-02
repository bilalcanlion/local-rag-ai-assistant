import sqlite3
from pathlib import Path


DB_PATH = Path("db") / "rag.db"


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    return connection


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def clear_chunks():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM chunks")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='chunks'")

    connection.commit()
    connection.close()

def save_chunks(chunks):
    connection = get_connection()
    cursor = connection.cursor()

    for chunk in chunks:
        cursor.execute(
            "INSERT INTO chunks (content) VALUES (?)",
            (chunk,)
        )

    connection.commit()
    connection.close()


def get_all_chunks():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, content FROM chunks")
    rows = cursor.fetchall()

    connection.close()
    return rows


if __name__ == "__main__":
    create_tables()
    print("Veritabanı hazır:", DB_PATH)