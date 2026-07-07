from pathlib import Path

from docx import Document
from pypdf import PdfReader

from database import create_tables, save_chunks, get_all_chunks


DATA_DIR = Path("data")
SUPPORTED_EXTENSIONS = [".txt", ".pdf", ".docx"]


def read_txt_file(file_path):
    return file_path.read_text(encoding="utf-8")


def read_pdf_file(file_path):
    reader = PdfReader(file_path)

    pages_text = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            pages_text.append(page_text)

    return "\n\n".join(pages_text)


def read_docx_file(file_path):
    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:
        clean_text = paragraph.text.strip()

        if clean_text:
            paragraphs.append(clean_text)

    return "\n\n".join(paragraphs)


def read_document(file_path):
    if not file_path.exists():
        print("Dosya bulunamadı:", file_path)
        return ""

    file_extension = file_path.suffix.lower()

    try:
        if file_extension == ".txt":
            return read_txt_file(file_path)

        if file_extension == ".pdf":
            return read_pdf_file(file_path)

        if file_extension == ".docx":
            return read_docx_file(file_path)

        print("Desteklenmeyen dosya türü:", file_path)
        return ""

    except Exception as error:
        print("Dosya okunurken hata oluştu:", file_path)
        print("Hata:", error)
        return ""


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

    files = sorted(data_dir.iterdir())

    for file_path in files:
        if not file_path.is_file():
            continue

        if file_path.name.startswith("~$"):
            continue

        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        document_text = read_document(file_path)

        if not document_text.strip():
            print("Boş veya okunamayan dosya atlandı:", file_path.name)
            continue

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
    print("Desteklenen dosya türleri:", ", ".join(SUPPORTED_EXTENSIONS))
    print("Kaydedilen parça sayısı:", len(saved_chunks))


if __name__ == "__main__":
    main()