from database import get_all_chunks


def simple_score(query, text):
    query_words = query.lower().split()
    text_lower = text.lower()

    score = 0

    for word in query_words:
        if word in text_lower:
            score += 1

    return score


def find_best_chunk(query):
    chunks = get_all_chunks()

    best_chunk = None
    best_score = 0

    for chunk_id, content in chunks:
        score = simple_score(query, content)

        if score > best_score:
            best_score = score
            best_chunk = {
                "id": chunk_id,
                "content": content,
                "score": score
            }

    return best_chunk


if __name__ == "__main__":
    question = input("Sorunuzu yazın: ")

    result = find_best_chunk(question)

    if result:
        print("\n=== En Alakalı Parça ===")
        print("Parça ID:", result["id"])
        print("Skor:", result["score"])
        print(result["content"])
    else:
        print("Bu soruyla ilgili bir bilgi bulunamadı.")