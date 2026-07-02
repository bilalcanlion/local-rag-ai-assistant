from pathlib import Path

from database import create_tables, clear_chunks, save_chunks
from ingest import read_document, split_into_chunks
from rag import find_top_chunks


DATA_PATH = Path("data") / "sample_doc.txt"


def prepare_database():
    document_text = read_document(DATA_PATH)

    if not document_text:
        print("Doküman okunamadı.")
        return False

    chunks = split_into_chunks(document_text)

    create_tables()
    clear_chunks()
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
        print(f"- Parça ID: {result['id']} | Skor: {result['score']}")


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