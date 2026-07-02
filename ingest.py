from pathlib import Path


DATA_PATH = Path("data") / "sample_doc.txt"


def read_document(file_path):
    if not file_path.exists():
        print("Dosya bulunamadı:", file_path)
        return ""

    text = file_path.read_text(encoding="utf-8")
    return text


def split_into_chunks(text):
    chunks = []

    paragraphs = text.split("\n\n")

    for paragraph in paragraphs:
        clean_paragraph = paragraph.strip()

        if clean_paragraph:
            chunks.append(clean_paragraph)

    return chunks


def main():
    document_text = read_document(DATA_PATH)

    chunks = split_into_chunks(document_text)

    print("=== Doküman Parçaları ===")

    for index, chunk in enumerate(chunks, start=1):
        print(f"\n--- Parça {index} ---")
        print(chunk)

    print("\n=== Bilgi ===")
    print("Toplam parça sayısı:", len(chunks))


if __name__ == "__main__":
    main()