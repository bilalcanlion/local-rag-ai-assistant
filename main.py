from pathlib import Path

from database import create_tables, save_chunks
from ingest import load_all_chunks
from rag import find_top_chunks


DATA_DIR = Path("data")


def prepare_database():
    chunks = load_all_chunks(DATA_DIR)

    if not chunks:
        print("Hiç doküman parçası bulunamadı.")
        return False

    create_tables()
    save_chunks(chunks)

    print("Veritabanı hazırlandı.")
    print("Kaydedilen parça sayısı:", len(chunks))

    return True


def create_basic_answer(results):
    if not results:
        return "Bu soruyla ilgili bir bilgi bulunamadı."

    best_result = results[0]

    answer = (
        "Dokümanlara göre: "
        + best_result["content"]
    )

    return answer


def print_sources(results):
    print("\nKaynaklar:")

    for result in results:
        print(
            f"- Dosya: {result['source']} | "
            f"Parça ID: {result['id']} | "
            f"Skor: {result['score']}"
        )


def ask_questions():
    print("\nLocal RAG AI Assistant çalışıyor.")
    print("Çıkmak için q yazabilirsiniz.")

    while True:
        question = input("\nSorunuzu yazın: ")

        if question.lower().strip() in ["q", "quit", "exit", "çıkış"]:
            print("Program kapatıldı.")
            break

        if not question.strip():
            print("Lütfen boş olmayan bir soru yazın.")
            continue

        results = find_top_chunks(question)

        print("\n=== Cevap ===")
        answer = create_basic_answer(results)
        print(answer)

        if results:
            print_sources(results)


def main():
    is_ready = prepare_database()

    if is_ready:
        ask_questions()


if __name__ == "__main__":
    main()