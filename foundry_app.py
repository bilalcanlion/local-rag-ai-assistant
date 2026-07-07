from foundry_local_sdk import Configuration, FoundryLocalManager

from foundry_database import get_all_chunks
from foundry_embeddings import cosine_similarity


EMBEDDING_MODEL_NAME = "qwen3-embedding-0.6b"
CHAT_MODEL_NAME = "phi-4-mini"

def expand_query(query):
    expanded_query = query
    query_lower = query.lower()

    if "foundry" in query_lower:
        expanded_query += " Microsoft Foundry Local yerel yapay zeka modeli cevap üretecektir"

    if "sqlite" in query_lower:
        expanded_query += " SQLite veritabanı doküman parçalarını saklamak"

    if "pdf" in query_lower:
        expanded_query += " PDF desteği PDF destegi PDF belgelerini okuyabilmesi PDF dosyalarını bilgi kaynağı olarak kullanabilir"

    if "docx" in query_lower or "word" in query_lower:
        expanded_query += " DOCX desteği Word belgelerini okuyabilmesi DOCX belgelerini bilgi kaynağı olarak kullanabilir"

    if "rag" in query_lower:
        expanded_query += " Retrieval-Augmented Generation anlamına gelir doküman bilgi bağlam halüsinasyon azaltır"

    if "yapay zeka" in query_lower:
        expanded_query += " bilgisayar sistemleri insan benzeri görevler metin anlama soru cevaplama sınıflandırma tahmin"

    if "halüsinasyon" in query_lower or "halusinasyon" in query_lower:
        expanded_query += " kaynak bağlam doküman bilgi uydurma riskini azaltır"

    if "internet" in query_lower or "offline" in query_lower or "çevrimdışı" in query_lower:
        expanded_query += " internet bağlantısına ihtiyaç duymadan yerel cihaz üzerinde çalışır"

    if (
        "kayıtlı parça" in query_lower
        or "kayıtlı doküman" in query_lower
        or "veritabanında kayıtlı" in query_lower
        or "parça yoksa" in query_lower
        or "bulunamadı hatası" in query_lower
        or "ne yapmalıyım" in query_lower
    ):
        expanded_query += " Foundry veritabanında kayıtlı doküman parçası bulunamadı hatası python foundry_ingest_test.py komutu çalıştırılmalıdır troubleshooting faq"

    if "ne demek" in query_lower or "nedir" in query_lower:
        expanded_query += " anlam tanım açıklama"

    if "ne işe yarar" in query_lower or "ne için" in query_lower:
        expanded_query += " kullanım amacı görev"

    return expanded_query
    expanded_query = query
    query_lower = query.lower()

    if "foundry" in query_lower:
        expanded_query += " Microsoft Foundry Local yerel yapay zeka modeli cevap üretecektir"

    if "sqlite" in query_lower:
        expanded_query += " SQLite veritabanı doküman parçalarını saklamak"

    if "rag" in query_lower:
        expanded_query += " Retrieval-Augmented Generation anlamına gelir doküman bilgi bağlam halüsinasyon azaltır"

    if "yapay zeka" in query_lower:
        expanded_query += " bilgisayar sistemleri insan benzeri görevler metin anlama soru cevaplama sınıflandırma tahmin"

    if "halüsinasyon" in query_lower or "halusinasyon" in query_lower:
        expanded_query += " kaynak bağlam doküman bilgi uydurma riskini azaltır"

    if "internet" in query_lower or "offline" in query_lower or "çevrimdışı" in query_lower:
        expanded_query += " internet bağlantısına ihtiyaç duymadan yerel cihaz üzerinde çalışır"

    if (
        "kayıtlı parça" in query_lower
        or "kayıtlı doküman" in query_lower
        or "veritabanında kayıtlı" in query_lower
        or "parça yoksa" in query_lower
        or "bulunamadı hatası" in query_lower
        or "ne yapmalıyım" in query_lower
    ):
        expanded_query += " Foundry veritabanında kayıtlı doküman parçası bulunamadı hatası python foundry_ingest_test.py komutu çalıştırılmalıdır troubleshooting faq"

    if "ne demek" in query_lower or "nedir" in query_lower:
        expanded_query += " anlam tanım açıklama"

    if "ne işe yarar" in query_lower or "ne için" in query_lower:
        expanded_query += " kullanım amacı görev"

    return expanded_query
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


def keyword_bonus(question, content, source=""):
    question_lower = question.lower()
    content_lower = content.lower()
    source_lower = source.lower()

    bonus = 0

    important_words = [
        "foundry",
        "local",
        "microsoft",
        "sqlite",
        "rag",
        "retrieval",
        "generation",
        "embedding",
        "veritabanı",
        "doküman",
        "parça",
        "kayıtlı",
        "bulunamadı",
        "hata",
        "python",
        "foundry_ingest_test.py",
        "halüsinasyon",
        "yapay",
        "zeka",
        "internet",
        "yerel",
        "pdf",
        "destegi",
        "desteği",
        "docx",
        "word",
        "belge",
        "belgelerini",
        "dosyalarını",
    ]

    for word in important_words:
        if word in question_lower and word in content_lower:
            bonus += 0.05

    if (
        "kayıtlı parça" in question_lower
        or "veritabanında kayıtlı" in question_lower
        or "parça yoksa" in question_lower
        or "ne yapmalıyım" in question_lower
    ) and "foundry_ingest_test.py" in content_lower:
        bonus += 0.4

    if "halüsinasyon" in question_lower and "halüsinasyon" in content_lower:
        bonus += 0.2

    if "internet" in question_lower and "internet bağlantısına ihtiyaç duymadan" in content_lower:
        bonus += 0.2

    if "pdf" in question_lower and "pdf" in content_lower:
        bonus += 0.3

    if "pdf" in question_lower and source_lower.endswith(".pdf"):
        bonus += 0.6

    if ("docx" in question_lower or "word" in question_lower) and "docx" in content_lower:
        bonus += 0.3

    if ("docx" in question_lower or "word" in question_lower) and source_lower.endswith(".docx"):
        bonus += 0.4

    return bonus
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


def load_models():
    print("Foundry Local başlatılıyor...")

    config = Configuration(app_name="local_rag_ai_assistant")
    FoundryLocalManager.initialize(config)

    manager = FoundryLocalManager.instance

    print("Embedding modeli hazırlanıyor:", EMBEDDING_MODEL_NAME)
    embedding_model = manager.catalog.get_model(EMBEDDING_MODEL_NAME)
    embedding_model.download()
    embedding_model.load()
    embedding_client = embedding_model.get_embedding_client()

    print("Chat modeli hazırlanıyor:", CHAT_MODEL_NAME)
    chat_model = manager.catalog.get_model(CHAT_MODEL_NAME)
    chat_model.download()
    chat_model.load()
    chat_client = chat_model.get_chat_client()

    print("Modeller hazır.")

    return embedding_model, embedding_client, chat_model, chat_client


def create_question_embedding(question, embedding_client):
    expanded_question = expand_query(question)
    response = embedding_client.generate_embedding(expanded_question)
    return response.data[0].embedding


def find_top_chunks(question, embedding_client, top_k=3, min_final_score=0.35):
    chunks = get_all_chunks()

    if not chunks:
        return []

    question_embedding = create_question_embedding(question, embedding_client)

    results = []

    for chunk in chunks:
        similarity = cosine_similarity(
            question_embedding,
            chunk["embedding"]
        )

        final_score = similarity + keyword_bonus(
            question,
            chunk["content"],
            chunk["source"]
        )

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
    chunks = get_all_chunks()

    if not chunks:
        return []

    question_embedding = create_question_embedding(question, embedding_client)

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


def generate_answer(question, context, chat_client):
    messages = [
        {
            "role": "system",
            "content": (
                "Sen Türkçe cevap veren yardımcı bir yapay zeka asistanısın. "
                "Sadece verilen bağlamı kullanarak cevap ver. "
                "Bağlam dışı bilgi ekleme. "
                "Bağlamda bilgi yoksa 'Bu bilgi mevcut dokümanlarda bulunamadı.' de. "
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

    print("\n=== Cevap ===")

    output_piece_count = 0
    max_output_pieces = 120

    for chunk in chat_client.complete_streaming_chat(messages):
        if output_piece_count >= max_output_pieces:
            print("\n\nCevap çok uzadığı için burada durduruldu.")
            break

        if not chunk.choices:
            continue

        content = chunk.choices[0].delta.content

        if content:
            print(content, end="", flush=True)
            output_piece_count += 1

    print()


def print_sources(results):
    print("\n=== Kaynaklar ===")

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

    print("Hızlandırılmış Foundry RAG Assistant başlatılıyor...")
    print("Kayıtlı doküman parçası sayısı:", len(chunks))

    embedding_model = None
    chat_model = None

    try:
        embedding_model, embedding_client, chat_model, chat_client = load_models()

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

            results = find_top_chunks(question, embedding_client)

            if not results:
                print("\n=== Cevap ===")
                print("Bu bilgi mevcut dokümanlarda bulunamadı.")
                continue

            context = build_context(results)
            generate_answer(question, context, chat_client)
            print_sources(results)

    finally:
        if chat_model is not None:
            chat_model.unload()
            print("Chat modeli kapatıldı.")

        if embedding_model is not None:
            embedding_model.unload()
            print("Embedding modeli kapatıldı.")


if __name__ == "__main__":
    main()