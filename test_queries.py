from pathlib import Path

from database import create_tables, save_chunks
from ingest import load_all_chunks
from rag import find_top_chunks


DATA_DIR = Path("data")


TEST_CASES = [
    {
        "question": "RAG ne demek?",
        "expected_keyword": "Retrieval-Augmented Generation"
    },
    {
        "question": "SQLite ne işe yarar?",
        "expected_keyword": "veritabanı"
    },
    {
        "question": "Foundry Local ne için kullanılacak?",
        "expected_keyword": "Microsoft Foundry Local"
    },
    {
        "question": "Türkiye'nin başkenti neresi?",
        "expected_keyword": None
    }
]


def prepare_database():
    chunks = load_all_chunks(DATA_DIR)

    create_tables()
    save_chunks(chunks)

    return len(chunks)


def run_tests():
    print("=== Testler Başlıyor ===")

    chunk_count = prepare_database()
    print("Kaydedilen parça sayısı:", chunk_count)

    passed_count = 0

    for index, test_case in enumerate(TEST_CASES, start=1):
        question = test_case["question"]
        expected_keyword = test_case["expected_keyword"]

        results = find_top_chunks(question)

        print(f"\n--- Test {index} ---")
        print("Soru:", question)

        if expected_keyword is None:
            if not results:
                print("Sonuç: BAŞARILI")
                print("Beklenen: Bilgi bulunamadı.")
                passed_count += 1
            else:
                print("Sonuç: BAŞARISIZ")
                print("Beklenen: Bilgi bulunamamalıydı.")
                print("Bulunan cevap:", results[0]["content"])

        else:
            if results and expected_keyword.lower() in results[0]["content"].lower():
                print("Sonuç: BAŞARILI")
                print("Bulunan cevap:", results[0]["content"])
                passed_count += 1
            else:
                print("Sonuç: BAŞARISIZ")
                print("Beklenen kelime:", expected_keyword)

                if results:
                    print("Bulunan cevap:", results[0]["content"])
                else:
                    print("Hiç sonuç bulunamadı.")

    print("\n=== Test Özeti ===")
    print("Başarılı test sayısı:", passed_count)
    print("Toplam test sayısı:", len(TEST_CASES))


if __name__ == "__main__":
    run_tests()