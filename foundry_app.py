from foundry_database import get_all_chunks
from foundry_embeddings import FoundryEmbedder, cosine_similarity


def expand_query(query):
    expanded_query = query
    query_lower = query.lower()

    if "foundry" in query_lower:
        expanded_query += " Microsoft Foundry Local yerel yapay zeka modeli cevap üretecektir"

    if "sqlite" in query_lower:
        expanded_query += " SQLite veritabanı doküman parçalarını saklamak"

    if "rag" in query_lower:
        expanded_query += " Retrieval-Augmented Generation anlamına gelir doküman bilgi bağlam"

    if "ne demek" in query_lower or "nedir" in query_lower:
        expanded_query += " anlam tanım açıklama"

    if "ne işe yarar" in query_lower or "ne için" in query_lower:
        expanded_query += " kullanım amacı görev"

    return expanded_query


def keyword_bonus(question, content):
    question_lower = question.lower()
    content_lower = content.lower()

    bonus = 0

    important_words = [
        "foundry",
        "local",
        "microsoft",
        "sqlite",
        "rag",
        "retrieval",
        "generation",
    ]

    for word in important_words:
        if word in question_lower and word in content_lower:
            bonus += 0.05

    return bonus


def find_top_chunks(question, embedder, top_k=3, min_final_score=0.35):
    chunks = get_all_chunks()

    if not chunks:
        return []

    expanded_question = expand_query(question)
    question_embedding = embedder.embed_text(expanded_question)

    results = []

    for chunk in chunks:
        similarity = cosine_similarity(
            question_embedding,
            chunk["embedding"]
        )

        final_score = similarity + keyword_bonus(question, chunk["content"])

        if final_score >= min_final_score:
            results.append({
                "id": chunk["id"],
                "source": chunk["source"],
                "content": chunk["content"],
                "similarity": similarity,
                "final_score": final_score
            })

    results.sort(key=lambda item: item["final_score"], reverse=True)

    return results[:top_k]


def print_answer(results):
    if not results:
        print("\n=== Cevap ===")
        print("Bu bilgi mevcut dokümanlarda bulunamadı.")
        return

    best_result = results[0]

    print("\n=== Cevap ===")
    print("Dokümanlara göre:", best_result["content"])

    print("\nKaynaklar:")

    for result in results:
        print(
            f"- Dosya: {result['source']} | "
            f"Parça ID: {result['id']} | "
            f"Benzerlik: {round(result['similarity'], 3)} | "
            f"Final skor: {round(result['final_score'], 3)}"
        )


def main():
    chunks = get_all_chunks()

    if not chunks:
        print("Foundry veritabanında kayıtlı doküman parçası bulunamadı.")
        print("Önce şu komutu çalıştırın:")
        print("python foundry_ingest_test.py")
        return

    print("Foundry tabanlı Local RAG Assistant başlatılıyor...")
    print("Kayıtlı doküman parçası sayısı:", len(chunks))

    embedder = FoundryEmbedder()

    try:
        embedder.start()

        print("\nSoru sormaya başlayabilirsiniz.")
        print("Çıkmak için q yazabilirsiniz.")

        while True:
            question = input("\nSorunuzu yazın: ")

            if question.lower().strip() in ["q", "quit", "exit", "çıkış"]:
                print("Program kapatıldı.")
                break

            if not question.strip():
                print("Lütfen boş olmayan bir soru yazın.")
                continue

            results = find_top_chunks(question, embedder)
            print_answer(results)

    finally:
        embedder.stop()


if __name__ == "__main__":
    main()