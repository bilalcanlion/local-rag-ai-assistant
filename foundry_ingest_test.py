from pathlib import Path

from foundry_database import create_tables, save_chunk, get_all_chunks
from foundry_embeddings import FoundryEmbedder
from ingest import load_all_chunks


DATA_DIR = Path("data")


def main():
    chunks = load_all_chunks(DATA_DIR)

    print("Toplam doküman parçası:", len(chunks))

    create_tables()
    print("Foundry SQLite tablosu oluşturuldu.")

    embedder = FoundryEmbedder()

    try:
        embedder.start()

        for index, chunk in enumerate(chunks, start=1):
            print(f"\nEmbedding üretiliyor: {index}/{len(chunks)}")
            print("Kaynak:", chunk["source"])
            print("İçerik:", chunk["content"][:80], "...")

            embedding = embedder.embed_text(chunk["content"])

            save_chunk(
                source=chunk["source"],
                content=chunk["content"],
                embedding=embedding
            )

            print("Kaydedildi. Vektör boyutu:", len(embedding))

    finally:
        embedder.stop()

    saved_chunks = get_all_chunks()

    print("\n=== Kayıt Kontrolü ===")
    print("SQLite'a kaydedilen parça sayısı:", len(saved_chunks))

    if saved_chunks:
        first_chunk = saved_chunks[0]
        print("İlk kayıt kaynak dosyası:", first_chunk["source"])
        print("İlk kayıt vektör boyutu:", len(first_chunk["embedding"]))


if __name__ == "__main__":
    main()