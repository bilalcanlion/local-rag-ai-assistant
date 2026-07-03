from foundry_local_sdk import Configuration, FoundryLocalManager


def main():
    print("Foundry Local başlatılıyor...")

    config = Configuration(app_name="local_rag_ai_assistant")
    FoundryLocalManager.initialize(config)

    manager = FoundryLocalManager.instance

    print("Embedding modeli seçiliyor...")
    model = manager.catalog.get_model("qwen3-embedding-0.6b")

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

    print("Embedding client hazırlanıyor...")
    client = model.get_embedding_client()

    text = "SQLite, yerel doküman parçalarını saklamak için kullanılan hafif bir veritabanıdır."

    print("Test embedding üretiliyor...")
    response = client.generate_embedding(text)

    embedding = response.data[0].embedding

    print("Embedding başarıyla üretildi.")
    print("Vektör boyutu:", len(embedding))
    print("İlk 5 değer:", embedding[:5])

    model.unload()
    print("Model kapatıldı.")


if __name__ == "__main__":
    main()