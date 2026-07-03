from pathlib import Path

from foundry_embeddings import FoundryEmbedder, cosine_similarity
from ingest import load_all_chunks


DATA_DIR = Path("data")


def expand_query(query):
    expanded_query = query
    query_lower = query.lower()

    if "foundry" in query_lower:
        expanded_query += " Microsoft Foundry Local yerel yapay zeka modeli cevap üretecektir"

    if "sqlite" in query_lower:
        expanded_query += " SQLite veritabanı doküman parçalarını saklamak"

    if "rag" in query_lower:
        expanded_query += " Retrieval-Augmented Generation anlamına gelir doküman bilgi bağlam"

    return expanded_query


def keyword_bonus(question, content):
    question_lower = question.lower()
    content_lower = content.lower()

    bonus = 0

    important_words = ["foundry", "local", "sqlite", "rag", "microsoft"]

    for word in important_words:
        if word in question_lower and word in content_lower:
            bonus += 0.05

    return bonus


def find_top_chunks_with_foundry(question, chunks, embedder, top_k=3):
    expanded_question = expand_query(question)

    print("Soru embedding vektörüne çevriliyor...")
    question_embedding = embedder.embed_text(expanded_question)

    results = []

    for chunk in chunks:
        print("Doküman parçası embedding vektörüne çevriliyor:", chunk["source"])

        chunk_embedding = embedder.embed_text(chunk["content"])
        similarity = cosine_similarity(question_embedding, chunk_embedding)

        final_score = similarity + keyword_bonus(question, chunk["content"])

        results.append({
            "source": chunk["source"],
            "content": chunk["content"],
            "similarity": similarity,
            "final_score": final_score
        })

    results.sort(key=lambda item: item["final_score"], reverse=True)

    return results[:top_k]


def main():
    chunks = load_all_chunks(DATA_DIR)

    print("Toplam doküman parçası:", len(chunks))

    question = "Foundry Local ne için kullanılacak?"

    embedder = FoundryEmbedder()

    try:
        embedder.start()

        results = find_top_chunks_with_foundry(
            question=question,
            chunks=chunks,
            embedder=embedder,
            top_k=3
        )

        print("\nSoru:", question)
        print("\n=== Foundry Local ile En Benzer Parçalar ===")

        for result in results:
            print("\nKaynak:", result["source"])
            print("Benzerlik:", round(result["similarity"], 3))
            print("Final skor:", round(result["final_score"], 3))
            print(result["content"])

    finally:
        embedder.stop()


if __name__ == "__main__":
    main()