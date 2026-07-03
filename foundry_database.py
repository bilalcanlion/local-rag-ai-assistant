import json
import sqlite3
from pathlib import Path


DB_PATH = Path("db") / "foundry_rag.db"


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    return connection


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS foundry_chunks")

    cursor.execute("""
        CREATE TABLE foundry_chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT NOT NULL,
            content TEXT NOT NULL,
            embedding TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_chunk(source, content, embedding):
    connection = get_connection()
    cursor = connection.cursor()

    embedding_json = json.dumps(embedding)

    cursor.execute(
        """
        INSERT INTO foundry_chunks (source, content, embedding)
        VALUES (?, ?, ?)
        """,
        (source, content, embedding_json)
    )

    connection.commit()
    connection.close()


def get_all_chunks():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, source, content, embedding FROM foundry_chunks")
    rows = cursor.fetchall()

    connection.close()

    chunks = []

    for chunk_id, source, content, embedding_json in rows:
        chunks.append({
            "id": chunk_id,
            "source": source,
            "content": content,
            "embedding": json.loads(embedding_json)
        })

    return chunks


if __name__ == "__main__":
    create_tables()
    print("Foundry veritabanı hazır:", DB_PATH)