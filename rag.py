import re

from database import get_all_chunks


def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())


def simple_score(query, text):
    query_words = set(tokenize(query))
    text_words = set(tokenize(text))

    score = 0

    for word in query_words:
        if word in text_words:
            score += 2
        elif any(word in text_word or text_word in word for text_word in text_words):
            score += 1

    return score


def find_top_chunks(query, top_k=3, min_score=2):
    chunks = get_all_chunks()
    scored_chunks = []

    for chunk_id, source, content in chunks:
        score = simple_score(query, content)

        if score >= min_score:
            scored_chunks.append({
                "id": chunk_id,
                "source": source,
                "content": content,
                "score": score
            })

    scored_chunks.sort(key=lambda item: item["score"], reverse=True)

    return scored_chunks[:top_k]
    chunks = get_all_chunks()
    scored_chunks = []

    for chunk_id, source, content in chunks:
        score = simple_score(query, content)

        if score > 0:
            scored_chunks.append({
                "id": chunk_id,
                "source": source,
                "content": content,
                "score": score
            })

    scored_chunks.sort(key=lambda item: item["score"], reverse=True)

    return scored_chunks[:top_k]


def find_best_chunk(query):
    top_chunks = find_top_chunks(query, top_k=1)

    if top_chunks:
        return top_chunks[0]

    return None


if __name__ == "__main__":
    question = input("Sorunuzu yazın: ")

    results = find_top_chunks(question)

    if results:
        print("\n=== En Alakalı Parçalar ===")

        for result in results:
            print(f"\n--- Parça ID: {result['id']} ---")
            print("Kaynak dosya:", result["source"])
            print("Skor:", result["score"])
            print(result["content"])
    else:
        print("Bu soruyla ilgili bir bilgi bulunamadı.")