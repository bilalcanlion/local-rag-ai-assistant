from pathlib import Path

from database import create_tables, save_chunks, get_all_chunks


DATA_DIR = Path("data")


def read_document(file_path):
    if not file_path.exists():
        print("Dosya bulunamadı:", file_path)
        return ""

    text = file_path.read_text(encoding="utf-8")
    return text


def split_into_chunks(text, source_name):
    chunks = []

    paragraphs = text.split("\n\n")

    for paragraph in paragraphs:
        clean_paragraph = paragraph.strip()

        if clean_paragraph:
            chunks.append({
                "source": source_name,
                "content": clean_paragraph
            })

    return chunks


def load_all_chunks(data_dir):
    all_chunks = []

    text_files = sorted(data_dir.glob("*.txt"))

    for file_path in text_files:
        document_text = read_document(file_path)
        chunks = split_into_chunks(document_text, file_path.name)
        all_chunks.extend(chunks)

    return all_chunks


def main():
    chunks = load_all_chunks(DATA_DIR)

    create_tables()
    save_chunks(chunks)

    saved_chunks = get_all_chunks()

    print("=== Veritabanına Kaydedilen Parçalar ===")

    for chunk_id, source, content in saved_chunks:
        print(f"\n--- Parça ID: {chunk_id} ---")
        print("Kaynak dosya:", source)
        print(content)

    print("\n=== Bilgi ===")
    print("Kaydedilen parça sayısı:", len(saved_chunks))


if __name__ == "__main__":
    main()