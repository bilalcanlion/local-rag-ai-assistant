from foundry_local_sdk import FoundryLocalManager

from foundry_database import get_all_chunks
from foundry_embeddings import FoundryEmbedder, cosine_similarity

CHAT_MODEL_NAME = "phi-4-mini"


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


def find_top_chunks(question, embedder, top_k=2, min_final_score=0.35):
    chunks = get_all_chunks()

    if not chunks:
        print("Foundry veritabanında kayıtlı parça bulunamadı.")
        print("Önce şu komutu çalıştırın: python foundry_ingest_test.py")
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
                "final_score": final_score,
            })

    results.sort(key=lambda item: item["final_score"], reverse=True)

    return results[:top_k]


def build_context(results):
    context_parts = []

    for result in results:
        context_parts.append(
            f"[Kaynak: {result['source']} | Parça ID: {result['id']}]\n"
            f"{result['content']}"
        )

    return "\n\n".join(context_parts)


def generate_answer_with_chat_model(question, context):
    print("\nChat modeli başlatılıyor:", CHAT_MODEL_NAME)

    manager = FoundryLocalManager.instance
    model = manager.catalog.get_model(CHAT_MODEL_NAME)

    print("Chat modeli indiriliyor veya önbellekten hazırlanıyor...")
    model.download(
        lambda progress: print(
            f"\rİndirme ilerlemesi: {progress:.2f}%",
            end="",
            flush=True,
        )
    )

    print("\nChat modeli yükleniyor...")
    model.load()

    client = model.get_chat_client()

    messages = [
        {
            "role": "system",
            "content": (
                "Sen Türkçe cevap veren yardımcı bir yapay zeka asistanısın. "
                "Sadece verilen bağlamı kullanarak cevap ver. "
                "Bağlam dışı bilgi ekleme. "
                "Cevabın kısa, açık ve en fazla 2 cümle olsun."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Bağlam:\n{context}\n\n"
                f"Soru: {question}\n\n"
                "Cevap:"
            ),
        },
    ]

    print("\n=== LLM Cevabı ===")

    try:
        for chunk in client.complete_streaming_chat(messages):
            if not chunk.choices:
                continue

            content = chunk.choices[0].delta.content

            if content:
                print(content, end="", flush=True)

        print()

    finally:
        model.unload()
        print("\nChat modeli kapatıldı.")


def main():
    question = "RAG ne demek?"

    print("Soru:", question)

    embedder = FoundryEmbedder()

    try:
        embedder.start()
        results = find_top_chunks(question, embedder)
    finally:
        embedder.stop()

    if not results:
        print("\n=== Cevap ===")
        print("Bu bilgi mevcut dokümanlarda bulunamadı.")
        return

    print("\n=== Bulunan Kaynaklar ===")

    for result in results:
        print(
            f"- Dosya: {result['source']} | "
            f"Parça ID: {result['id']} | "
            f"Benzerlik: {round(result['similarity'], 3)} | "
            f"Final skor: {round(result['final_score'], 3)}"
        )

    context = build_context(results)
    generate_answer_with_chat_model(question, context)


if __name__ == "__main__":
    main()