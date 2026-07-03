import math

from foundry_local_sdk import Configuration, FoundryLocalManager


MODEL_NAME = "qwen3-embedding-0.6b"


class FoundryEmbedder:
    def __init__(self):
        self.model = None
        self.client = None

    def start(self):
        print("Foundry Local başlatılıyor...")

        config = Configuration(app_name="local_rag_ai_assistant")
        FoundryLocalManager.initialize(config)

        manager = FoundryLocalManager.instance

        print("Embedding modeli seçiliyor:", MODEL_NAME)
        self.model = manager.catalog.get_model(MODEL_NAME)

        print("Model indiriliyor veya önbellekten hazırlanıyor...")
        self.model.download(
            lambda progress: print(
                f"\rİndirme ilerlemesi: {progress:.2f}%",
                end="",
                flush=True,
            )
        )

        print("\nModel yükleniyor...")
        self.model.load()

        print("Embedding client hazırlanıyor...")
        self.client = self.model.get_embedding_client()

    def embed_text(self, text):
        if self.client is None:
            raise RuntimeError("Embedding client hazır değil. Önce start() çağırılmalı.")

        response = self.client.generate_embedding(text)
        embedding = response.data[0].embedding

        return embedding

    def stop(self):
        if self.model is not None:
            self.model.unload()
            print("Model kapatıldı.")


def cosine_similarity(vector_a, vector_b):
    dot_product = 0

    for a, b in zip(vector_a, vector_b):
        dot_product += a * b

    length_a = math.sqrt(sum(a * a for a in vector_a))
    length_b = math.sqrt(sum(b * b for b in vector_b))

    if length_a == 0 or length_b == 0:
        return 0

    return dot_product / (length_a * length_b)