from database import get_all_chunks
from embeddings import build_vocabulary, text_to_vector, cosine_similarity


def expand_query(query):
    expanded_query = query
    query_lower = query.lower()

    if "ne demek" in query_lower or "nedir" in query_lower:
        expanded_query += " anlam anlamına gelir tanım açıklama"

    if "ne işe yarar" in query_lower:
        expanded_query += " kullanılan kullanılır görev amaç"

    if "ne için" in query_lower:
        expanded_query += " kullanılacak amacı hedef"

    if "foundry" in query_lower:
        expanded_query += " foundry local microsoft yerel yapay zeka model cevap üretecektir"

    if "sqlite" in query_lower:
        expanded_query += " sqlite veritabanı saklamak yerel database"

    if "rag" in query_lower:
        expanded_query += " retrieval augmented generation anlamına gelir doküman bilgi bağlam"

    return expanded_query
    expanded_query = query
    query_lower = query.lower()

    if "ne demek" in query_lower or "nedir" in query_lower:
        expanded_query += " anlam anlamına gelir tanım açıklama"

    if "ne işe yarar" in query_lower or "ne için" in query_lower:
        expanded_query += " kullanılan kullanılır amacı görev"

    return expanded_query
    expanded_query = query
    query_lower = query.lower()

    if "ne demek" in query_lower or "nedir" in query_lower:
        expanded_query += " anlam anlamına gelir tanım açıklama"

    if "ne işe yarar" in query_lower or "ne için" in query_lower:
        expanded_query += " kullanılan kullanılır amacı görev"

    return expanded_query


def find_top_chunks(query, top_k=3, min_similarity=0.1):
    chunks = get_all_chunks()

    if not chunks:
        return []

    expanded_query = expand_query(query)

    texts = [content for _, _, content in chunks]
    vocabulary = build_vocabulary(texts + [expanded_query])

    query_vector = text_to_vector(expanded_query, vocabulary)

    results = []

    for chunk_id, source, content in chunks:
        chunk_vector = text_to_vector(content, vocabulary)
        similarity = cosine_similarity(query_vector, chunk_vector)

        if similarity >= min_similarity:
            results.append({
                "id": chunk_id,
                "source": source,
                "content": content,
                "similarity": similarity
            })

    results.sort(key=lambda item: item["similarity"], reverse=True)

    return results[:top_k]


def find_best_chunk(query):
    top_chunks = find_top_chunks(query, top_k=1)

    if top_chunks:
        return top_chunks[0]

    return None


if __name__ == "__main__":
    question = input("Sorunuzu yazın: ")

    results = find_top_chunks(question)

    if results:
        print("\n=== En Benzer Parçalar ===")

        for result in results:
            print(f"\n--- Parça ID: {result['id']} ---")
            print("Kaynak dosya:", result["source"])
            print("Benzerlik:", round(result["similarity"], 3))
            print(result["content"])
    else:
        print("Bu bilgi mevcut dokümanlarda bulunamadı.")