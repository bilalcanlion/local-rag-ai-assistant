from foundry_local_sdk import Configuration, FoundryLocalManager


MODEL_NAME = "phi-3.5-mini"

def main():
    print("Foundry Local chat testi başlatılıyor...")

    config = Configuration(app_name="local_rag_ai_assistant")
    FoundryLocalManager.initialize(config)

    manager = FoundryLocalManager.instance

    print("Chat modeli seçiliyor:", MODEL_NAME)
    model = manager.catalog.get_model(MODEL_NAME)

    print("Model indiriliyor veya önbellekten hazırlanıyor...")
    model.download(
        lambda progress: print(
            f"\rİndirme ilerlemesi: {progress:.2f}%",
            end="",
            flush=True,
        )
    )

    print("\nModel yükleniyor...")
    model.load()
    print("Model yüklendi.")

    print("Chat client hazırlanıyor...")
    client = model.get_chat_client()

    context = (
        "RAG, Retrieval-Augmented Generation anlamına gelir. "
        "Bu yöntemde sistem önce ilgili bilgiyi dokümanlardan bulur, "
        "sonra bu bilgiyi yapay zeka modeline bağlam olarak verir."
    )

    messages = [
        {
            "role": "system",
            "content": (
                "Sen Türkçe cevap veren yardımcı bir asistansın. "
                "Sadece verilen bağlama göre cevap ver. "
                "Bağlamda bilgi yoksa 'Bu bilgi bağlamda yok.' de. "
                "Cevabın en fazla 2 cümle olsun."
            )
        },
        {
            "role": "user",
            "content": (
                f"Bağlam:\n{context}\n\n"
                "Soru: RAG nedir?"
            )
        }
    ]

    print("\nSoru:")
    print("RAG nedir?")

    print("\nAsistan cevabı:")

    try:
        token_count = 0
        max_tokens_to_print = 80

        for chunk in client.complete_streaming_chat(messages):
            if token_count >= max_tokens_to_print:
                print("\n\nCevap uzun olduğu için test burada durduruldu.")
                break

            if not chunk.choices:
                continue

            content = chunk.choices[0].delta.content

            if content:
                print(content, end="", flush=True)
                token_count += 1

        print()

    finally:
        model.unload()
        print("\nModel kapatıldı.")


if __name__ == "__main__":
    main()