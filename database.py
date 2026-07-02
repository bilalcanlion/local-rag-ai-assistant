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

    cursor.execute("DROP TABLE IF EXISTS chunks")

    cursor.execute("""
        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_chunks(chunks):
    connection = get_connection()
    cursor = connection.cursor()

    for chunk in chunks:
        cursor.execute(
            "INSERT INTO chunks (source, content) VALUES (?, ?)",
            (chunk["source"], chunk["content"])
        )

    connection.commit()
    connection.close()


def get_all_chunks():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, source, content FROM chunks")
    rows = cursor.fetchall()

    connection.close()
    return rows


if __name__ == "__main__":
    create_tables()
    print("Veritabanı hazır:", DB_PATH)