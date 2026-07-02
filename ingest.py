from pathlib import Path


DATA_PATH = Path("data") / "sample_doc.txt"


def read_document(file_path):
    if not file_path.exists():
        print("Dosya bulunamadı:", file_path)
        return ""

    text = file_path.read_text(encoding="utf-8")
    return text


def main():
    document_text = read_document(DATA_PATH)

    print("=== Doküman İçeriği ===")
    print(document_text)

    print("\n=== Bilgi ===")
    print("Karakter sayısı:", len(document_text))


if __name__ == "__main__":
    main()