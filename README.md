# Local RAG AI Assistant

Bu proje, yerel dokümanlardan bilgi bulabilen basit bir RAG tabanlı soru-cevap asistanıdır.

Proje, önce eğitim amaçlı basit vektör benzerliği ile başlamış; daha sonra Microsoft Foundry Local embedding modeli kullanılarak gerçek embedding tabanlı yerel retrieval sistemine dönüştürülmüştür.

## Projenin Amacı

Bu projenin amacı, kullanıcının sorduğu soruya göre yerel dokümanlar içinden en alakalı bilgi parçalarını bulabilen bir sistem geliştirmektir.

Sistem, internet bağlantısına ihtiyaç duymadan yerel dokümanlardan bilgi aramaya hazırlanmıştır. Microsoft Foundry Local ile cihaz üzerinde embedding üretilerek daha gerçekçi bir RAG altyapısı kurulmuştur.

## Şu Anki Özellikler

- Python proje yapısı oluşturuldu
- `data` klasöründeki birden fazla `.txt` dosyası okunabiliyor
- Dokümanlar paragraflara ayrılıyor
- Parçalar SQLite veritabanına kaydediliyor
- Basit vektör benzerliği ile arama yapılabiliyor
- Query expansion ile bazı soru tipleri daha doğru eşleştiriliyor
- Microsoft Foundry Local SDK kurulumu test edildi
- Foundry Local ile gerçek embedding üretildi
- Doküman embeddingleri SQLite veritabanına kaydedildi
- Kullanıcı sorusu Foundry Local ile embedding vektörüne çevriliyor
- SQLite’taki kayıtlı embeddinglerle karşılaştırma yapılıyor
- En alakalı kaynak parçalar bulunuyor
- Cevapta kaynak dosya adı, parça ID, benzerlik ve final skor gösteriliyor
- Bilgi dokümanlarda yoksa sistem cevap uydurmuyor
- Etkileşimli Foundry tabanlı uygulama `python foundry_app.py` komutu ile çalışıyor

## Proje Yapısı

```text
local-rag-ai-assistant/
├── data/
│   ├── sample_doc.txt
│   └── project_faq.txt
├── docs/
│   ├── project_notes.md
│   ├── test_results.md
│   ├── foundry_notes.md
│   └── foundry_test_results.md
├── database.py
├── embeddings.py
├── foundry_app.py
├── foundry_database.py
├── foundry_embedding_test.py
├── foundry_embeddings.py
├── foundry_ingest_test.py
├── foundry_retrieval_test.py
├── foundry_search_test.py
├── ingest.py
├── main.py
├── rag.py
├── requirements.txt
├── test_queries.py
├── README.md
└── .gitignore
```

## Kurulum

Gerekli paketleri kurmak için:

```bash
pip install -r requirements.txt
```

Windows için Foundry Local SDK paketi:

```text
foundry-local-sdk-winml
```

## Basit Sürümü Çalıştırma

Bu sürüm eğitim amaçlı basit vektör benzerliği kullanır:

```bash
python main.py
```

## Foundry Local Embedding Testi

Tek bir metin için Foundry Local embedding üretimini test etmek için:

```bash
python foundry_embedding_test.py
```

Beklenen çıktı örneği:

```text
Embedding başarıyla üretildi.
Vektör boyutu: 1024
```

## Foundry Embeddingleri SQLite’a Kaydetme

Doküman parçalarını Foundry Local embedding modelinden geçirip SQLite’a kaydetmek için:

```bash
python foundry_ingest_test.py
```

Bu komut şunları yapar:

```text
data klasöründeki dokümanları okur
↓
Dokümanları parçalara böler
↓
Her parça için Foundry Local embedding üretir
↓
Embeddingleri SQLite veritabanına kaydeder
```

## Foundry Tabanlı Etkileşimli Uygulama

Asıl Foundry tabanlı uygulamayı çalıştırmak için:

```bash
python foundry_app.py
```

Program açıldıktan sonra soru sorabilirsiniz.

Örnek sorular:

```text
RAG ne demek?
SQLite ne işe yarar?
Foundry Local ne için kullanılacak?
Türkiye'nin başkenti neresi?
```

Çıkmak için:

```text
q
```

yazabilirsiniz.

## Çalışma Mantığı

```text
data klasöründeki dokümanları oku
↓
Dokümanları küçük parçalara böl
↓
Foundry Local ile her parçanın embedding vektörünü üret
↓
Embeddingleri SQLite veritabanına kaydet
↓
Kullanıcıdan soru al
↓
Soruyu query expansion ile güçlendir
↓
Soruyu Foundry Local ile embedding vektörüne çevir
↓
SQLite’taki kayıtlı doküman embeddingleriyle karşılaştır
↓
Cosine similarity ile en alakalı parçaları bul
↓
Final skor ile sonuçları sırala
↓
En iyi parçaya göre cevap göster
↓
Kaynak dosya, parça ID, benzerlik ve final skor bilgisini yazdır
```

## Kullanılan Temel Kavramlar

### RAG

RAG, Retrieval-Augmented Generation anlamına gelir. Bu yöntemde sistem önce ilgili bilgiyi dokümanlardan bulur, sonra cevabı bu bilgiye göre üretir.

### Embedding

Embedding, metni bilgisayarın karşılaştırabileceği sayısal bir vektöre dönüştürme işlemidir.

Örneğin bir cümle şu şekilde temsil edilebilir:

```text
[0.12, -0.04, 0.88, ...]
```

Bu projede Foundry Local ile üretilen embedding vektörleri 1024 boyutludur.

### SQLite

SQLite, doküman parçalarını ve embedding vektörlerini yerel olarak saklamak için kullanılan hafif bir veritabanıdır.

### Cosine Similarity

Cosine similarity, soru embedding vektörü ile doküman embedding vektörlerinin birbirine ne kadar benzediğini ölçmek için kullanılır.

### Query Expansion

Kullanıcının sorusu bazı ek kelimelerle genişletilir. Örneğin “ne demek?” sorusu için “anlam”, “tanım”, “açıklama” gibi kelimeler eklenir. Böylece sistem daha doğru parçaları bulabilir.

### Final Skor

Final skor, embedding benzerliğine küçük bir anahtar kelime bonusu eklenmiş halidir.

```text
Final skor = Benzerlik + Anahtar kelime bonusu
```

Bu yöntem, önemli kelimeler soru ve doküman parçasında birlikte geçiyorsa doğru parçanın daha üst sıraya çıkmasına yardımcı olur.

## Örnek Çıktı

```text
Sorunuzu yazın: RAG ne demek?

=== Cevap ===
Dokümanlara göre: RAG, Retrieval-Augmented Generation anlamına gelir. Önce ilgili bilgi dokümanlardan bulunur, sonra bu bilgi yapay zeka modeline bağlam olarak verilir.

Kaynaklar:
- Dosya: sample_doc.txt | Parça ID: 5 | Benzerlik: 0.852 | Final skor: 0.902
```

Başka bir örnek:

```text
Sorunuzu yazın: Foundry Local ne için kullanılacak?

=== Cevap ===
Dokümanlara göre: Bu proje ileride Microsoft Foundry Local ile birleştirilerek yerel yapay zeka modeliyle cevap üretecektir.

Kaynaklar:
- Dosya: project_faq.txt | Parça ID: 3 | Benzerlik: 0.815 | Final skor: 0.915
```

Bilgi dokümanlarda yoksa:

```text
Sorunuzu yazın: Türkiye'nin başkenti neresi?

=== Cevap ===
Bu bilgi mevcut dokümanlarda bulunamadı.
```

## Testler

Basit retrieval testlerini çalıştırmak için:

```bash
python test_queries.py
```

Foundry Local embedding tabanlı retrieval testini çalıştırmak için:

```bash
python foundry_retrieval_test.py
```

## Dosyaların Görevleri

| Dosya                       | Görevi                                                                      |
| --------------------------- | --------------------------------------------------------------------------- |
| `main.py`                   | Basit eğitim sürümünü çalıştırır                                            |
| `foundry_app.py`            | Foundry Local embedding tabanlı etkileşimli uygulamayı çalıştırır           |
| `ingest.py`                 | Dokümanları okur ve parçalara böler                                         |
| `database.py`               | Basit SQLite işlemlerini yapar                                              |
| `rag.py`                    | Basit vektör benzerliği ile kaynak parça arar                               |
| `embeddings.py`             | Eğitim amaçlı basit vektör oluşturma ve cosine similarity işlemlerini yapar |
| `foundry_embeddings.py`     | Foundry Local embedding işlemleri için yardımcı sınıf içerir                |
| `foundry_database.py`       | Foundry embeddinglerini SQLite’a kaydeder ve okur                           |
| `foundry_ingest_test.py`    | Doküman embeddinglerini üretip SQLite’a kaydeder                            |
| `foundry_retrieval_test.py` | SQLite’taki Foundry embeddingleriyle retrieval testi yapar                  |
| `foundry_embedding_test.py` | Tek metin için Foundry embedding üretimini test eder                        |
| `foundry_search_test.py`    | Foundry embedding ile doğrudan arama testi yapar                            |
| `test_queries.py`           | Basit retrieval testlerini çalıştırır                                       |
| `data/`                     | Sistemin cevap verirken kullanacağı dokümanları içerir                      |
| `docs/`                     | Proje notlarını ve test sonuçlarını içerir                                  |

## Sonraki Hedefler

- Foundry Local ile yerel LLM bağlantısı kurmak
- Bulunan kaynak parçaları yerel LLM modeline bağlam olarak vermek
- Daha doğal cevap üretimi sağlamak
- Kaynaklı cevap formatını geliştirmek
- Embedding üretimini daha optimize hale getirmek
- Basit bir web arayüzü eklemek
- Daha fazla doküman türü desteklemek
