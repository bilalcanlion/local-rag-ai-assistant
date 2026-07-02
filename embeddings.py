import math
import re
from pathlib import Path

from ingest import load_all_chunks


DATA_DIR = Path("data")


def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())


def build_vocabulary(texts):
    vocabulary = []

    for text in texts:
        words = tokenize(text)

        for word in words:
            if word not in vocabulary:
                vocabulary.append(word)

    return vocabulary


def text_to_vector(text, vocabulary):
    words = tokenize(text)
    vector = []

    for vocab_word in vocabulary:
        count = words.count(vocab_word)
        vector.append(count)

    return vector


def cosine_similarity(vector_a, vector_b):
    dot_product = 0

    for a, b in zip(vector_a, vector_b):
        dot_product += a * b

    length_a = math.sqrt(sum(a * a for a in vector_a))
    length_b = math.sqrt(sum(b * b for b in vector_b))

    if length_a == 0 or length_b == 0:
        return 0

    return dot_product / (length_a * length_b)


def main():
    chunks = load_all_chunks(DATA_DIR)

    texts = [chunk["content"] for chunk in chunks]
    vocabulary = build_vocabulary(texts)

    question = "SQLite ne işe yarar?"
    question_vector = text_to_vector(question, vocabulary)

    results = []

    for chunk in chunks:
        chunk_vector = text_to_vector(chunk["content"], vocabulary)
        similarity = cosine_similarity(question_vector, chunk_vector)

        results.append({
            "source": chunk["source"],
            "content": chunk["content"],
            "similarity": similarity
        })

    results.sort(key=lambda item: item["similarity"], reverse=True)

    print("Soru:", question)
    print("\n=== En Benzer Parçalar ===")

    for result in results:
        print("\nKaynak:", result["source"])
        print("Benzerlik:", round(result["similarity"], 3))
        print(result["content"])


if __name__ == "__main__":
    main()