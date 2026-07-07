# Local RAG AI Assistant

Bu proje, yerel dokümanlardan bilgi bulabilen ve bu bilgileri yerel bir yapay zeka modeliyle cevap haline getirebilen RAG tabanlı bir soru-cevap asistanıdır.

Proje önce eğitim amaçlı basit vektör benzerliği ile başlamış, daha sonra Microsoft Foundry Local kullanılarak gerçek embedding tabanlı yerel retrieval sistemine ve yerel LLM destekli cevap üretimine dönüştürülmüştür.

## Projenin Amacı

Bu projenin amacı, kullanıcının sorduğu soruya göre yerel dokümanlar içinden en alakalı bilgi parçalarını bulmak ve bu parçaları kullanarak kısa, kaynaklı ve anlaşılır cevaplar üretmektir.

Sistem internet bağlantısına ihtiyaç duymadan yerel dokümanlardan bilgi arayacak şekilde tasarlanmıştır. Microsoft Foundry Local ile cihaz üzerinde embedding üretilir, SQLite içinde saklanan embeddinglerle karşılaştırma yapılır ve bulunan kaynak parçalar yerel chat modeline bağlam olarak verilir.

## Şu Anki Özellikler

- Python proje yapısı oluşturuldu
- `data` klasöründeki birden fazla `.txt` dosyası okunabiliyor
- Dokümanlar paragraflara ayrılıyor
- Parçalar SQLite veritabanına kaydediliyor
- Eğitim amaçlı basit vektör benzerliği ile arama yapılabiliyor
- Query expansion ile bazı soru tipleri daha doğru eşleştiriliyor
- Microsoft Foundry Local SDK kurulumu test edildi
- Foundry Local ile gerçek embedding üretildi
- Doküman embeddingleri SQLite veritabanına kaydedildi
- Kullanıcı sorusu Foundry Local ile embedding vektörüne çevriliyor
- SQLite’taki kayıtlı embeddinglerle karşılaştırma yapılıyor
- En alakalı kaynak parçalar bulunuyor
- Bulunan kaynak parçalar yerel LLM modeline bağlam olarak veriliyor
- `phi-4-mini` modeli ile doğal cevap üretimi yapılıyor
- Cevapta kaynak dosya adı, parça ID, benzerlik ve final skor gösteriliyor
- Bilgi dokümanlarda yoksa sistem cevap uydurmuyor
- Embedding ve chat modelleri uygulama başında bir kez yükleniyor
- Program kapatılırken modeller güvenli şekilde kapatılıyor
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
├── foundry_app_fast_test.py
├── foundry_chat_test.py
├── foundry_database.py
├── foundry_embedding_test.py
├── foundry_embeddings.py
├── foundry_ingest_test.py
├── foundry_rag_answer_test.py
├── foundry_retrieval_test.py
├── foundry_search_test.py
├── ingest.py
├── list_foundry_models.py
├── main.py
├── rag.py
├── requirements.txt
├── test_queries.py
├── README.md
└── .gitignore
```

## Kullanılan Teknolojiler

- Python
- SQLite
- Microsoft Foundry Local
- Foundry Local SDK
- Yerel embedding modeli: `qwen3-embedding-0.6b`
- Yerel chat modeli: `phi-4-mini`
- Cosine similarity
- Query expansion
- Retrieval-Augmented Generation

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

## Foundry Chat Modeli Testi

Yerel chat modelinin cevap üretmesini test etmek için:

```bash
python foundry_chat_test.py
```

Bu testte en iyi sonucu `phi-4-mini` modeli vermiştir.

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

## Foundry Retrieval Testi

SQLite’a kaydedilmiş embeddinglerle arama testini çalıştırmak için:

```bash
python foundry_retrieval_test.py
```

Bu testte sistem, kullanıcının sorusunu embedding vektörüne çevirir ve SQLite içinde kayıtlı doküman embeddingleriyle karşılaştırır.

## RAG + LLM Cevap Üretimi Testi

Retrieval sonucunda bulunan kaynakları yerel LLM modeline verip cevap üretimini test etmek için:

```bash
python foundry_rag_answer_test.py
```

Bu test, final uygulamaya geçmeden önce kaynak bulma ve LLM cevap üretme adımının birlikte çalıştığını doğrulamak için kullanılmıştır.

## Hızlandırılmış Uygulama Testi

Modellerin her soru için yeniden yüklenmesini engelleyen hızlandırılmış sürüm test edilmiştir:

```bash
python foundry_app_fast_test.py
```

Bu test başarılı olduktan sonra aynı mantık ana uygulama dosyası olan `foundry_app.py` içine taşınmıştır.

## Final Foundry Tabanlı Etkileşimli Uygulama

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

## Final Uygulamanın Çalışma Mantığı

```text
Uygulama başlatılır
↓
Embedding modeli yüklenir
↓
Chat modeli yüklenir
↓
Kullanıcıdan soru alınır
↓
Soru query expansion ile güçlendirilir
↓
Soru Foundry Local embedding modeline gönderilir
↓
Soru embedding vektörüne çevrilir
↓
SQLite’taki kayıtlı doküman embeddingleri alınır
↓
Cosine similarity ile en alakalı parçalar bulunur
↓
Final skor ile sonuçlar sıralanır
↓
En iyi kaynak parçalar bağlam olarak hazırlanır
↓
Bağlam phi-4-mini yerel chat modeline verilir
↓
LLM kısa bir cevap üretir
↓
Kaynak dosya, parça ID, benzerlik ve final skor gösterilir
↓
Programdan çıkılırken modeller kapatılır
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

### Yerel LLM

Yerel LLM, cevap üretimini internet üzerinden değil, bilgisayarda çalışan yerel model üzerinden yapar.

Bu projede cevap üretimi için `phi-4-mini` modeli kullanılmıştır.

## Örnek Çıktı

```text
Hızlandırılmış Foundry RAG Assistant başlatılıyor...
Kayıtlı doküman parçası sayısı: 6
Foundry Local başlatılıyor...
Embedding modeli hazırlanıyor: qwen3-embedding-0.6b
Chat modeli hazırlanıyor: phi-4-mini
Modeller hazır.

Soru sormaya başlayabilirsiniz.
Çıkmak için q yazabilirsiniz.

Sorunuzu yazın: RAG ne demek?

=== Cevap ===
RAG, Retrieval-Augmented Generation anlamına gelir. Önce ilgili bilgi dokümanlardan bulunur, sonra bu bilgi yapay zeka modeline bağlam olarak verilir.

=== Kaynaklar ===
- Dosya: sample_doc.txt | Parça ID: 5 | Benzerlik: 0.852 | Final skor: 0.902
- Dosya: sample_doc.txt | Parça ID: 4 | Benzerlik: 0.541 | Final skor: 0.591
```

Başka bir örnek:

```text
Sorunuzu yazın: Foundry Local ne için kullanılacak?

=== Cevap ===
Foundry Local, yerel yapay zeka modeliyle cevap üretmek için Microsoft Foundry ile birleştirilecek.

=== Kaynaklar ===
- Dosya: project_faq.txt | Parça ID: 3 | Benzerlik: 0.815 | Final skor: 0.915
```

Bilgi dokümanlarda yoksa:

```text
Sorunuzu yazın: Türkiye'nin başkenti neresi?

=== Cevap ===
Bu bilgi mevcut dokümanlarda bulunamadı.
```

Program kapatılırken:

```text
Sorunuzu yazın: q
Program kapatıldı.
Chat modeli kapatıldı.
Embedding modeli kapatıldı.
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

RAG + LLM cevap üretimi testini çalıştırmak için:

```bash
python foundry_rag_answer_test.py
```

Final uygulamayı çalıştırmak için:

```bash
python foundry_app.py
```

## Dosyaların Görevleri

| Dosya                        | Görevi                                                                      |
| ---------------------------- | --------------------------------------------------------------------------- |
| `main.py`                    | Basit eğitim sürümünü çalıştırır                                            |
| `foundry_app.py`             | Final Foundry Local RAG + LLM uygulamasını çalıştırır                       |
| `foundry_app_fast_test.py`   | Modelleri başta bir kez yükleyen hızlandırılmış test sürümüdür              |
| `ingest.py`                  | Dokümanları okur ve parçalara böler                                         |
| `database.py`                | Basit SQLite işlemlerini yapar                                              |
| `rag.py`                     | Basit vektör benzerliği ile kaynak parça arar                               |
| `embeddings.py`              | Eğitim amaçlı basit vektör oluşturma ve cosine similarity işlemlerini yapar |
| `foundry_embeddings.py`      | Foundry Local embedding işlemleri için yardımcı sınıf içerir                |
| `foundry_database.py`        | Foundry embeddinglerini SQLite’a kaydeder ve okur                           |
| `foundry_ingest_test.py`     | Doküman embeddinglerini üretip SQLite’a kaydeder                            |
| `foundry_retrieval_test.py`  | SQLite’taki Foundry embeddingleriyle retrieval testi yapar                  |
| `foundry_embedding_test.py`  | Tek metin için Foundry embedding üretimini test eder                        |
| `foundry_chat_test.py`       | Yerel chat modelinin cevap üretimini test eder                              |
| `foundry_rag_answer_test.py` | Retrieval + LLM cevap üretimini test eder                                   |
| `foundry_search_test.py`     | Foundry embedding ile doğrudan arama testi yapar                            |
| `list_foundry_models.py`     | Foundry Local model kataloğundaki modelleri listeler                        |
| `test_queries.py`            | Basit retrieval testlerini çalıştırır                                       |
| `data/`                      | Sistemin cevap verirken kullanacağı dokümanları içerir                      |
| `docs/`                      | Proje notlarını ve test sonuçlarını içerir                                  |

## Tamamlanan Aşamalar

- Python proje yapısı oluşturuldu
- GitHub reposu oluşturuldu
- Yerel doküman okuma eklendi
- Doküman parçalama eklendi
- SQLite veritabanı eklendi
- Basit retrieval sistemi yazıldı
- Query expansion eklendi
- Basit test dosyası oluşturuldu
- Microsoft Foundry Local SDK kuruldu
- Foundry Local embedding modeli test edildi
- Doküman embeddingleri SQLite’a kaydedildi
- Stored embedding retrieval testi yapıldı
- Yerel chat modeli test edildi
- `phi-4-mini` modeli seçildi
- RAG + LLM cevap üretimi test edildi
- Final etkileşimli Foundry RAG uygulaması oluşturuldu
- Kaynak gösterme özelliği eklendi
- Dokümanda olmayan bilgi için uydurmama davranışı test edildi
- Foundry app hızlandırıldı
- Modellerin her soruda yeniden yüklenmesi yerine başlangıçta bir kez yüklenmesi sağlandı
- Program kapanırken modellerin güvenli şekilde kapatılması sağlandı

## Şu Anki Sınırlamalar

- Yerel LLM bazen Türkçe cümlelerde küçük anlatım bozuklukları yapabilir.
- Şu anda sadece `.txt` dosyaları destekleniyor.
- İlk açılışta modellerin yüklenmesi biraz zaman alabilir.
- Cevap kalitesi, bulunan kaynak parçaların kalitesine bağlıdır.
- Henüz web arayüzü yoktur.
- PDF ve DOCX desteği henüz eklenmemiştir.

## Sonraki Hedefler

- Cevap formatını daha temiz hale getirmek
- PDF dosyası desteği eklemek
- DOCX dosyası desteği eklemek
- Daha fazla test senaryosu eklemek
- Daha iyi değerlendirme metrikleri oluşturmak
- Basit bir web arayüzü eklemek
- README içine ekran görüntüsü veya demo çıktısı eklemek
- Final proje raporu hazırlamak

## Proje Özeti

Local RAG AI Assistant, yerel dokümanlardan bilgi bulup bu bilgileri yerel yapay zeka modeliyle cevap haline getiren bir RAG uygulamasıdır.

Proje eğitim amaçlı basit bir retrieval sistemiyle başlamış, daha sonra Microsoft Foundry Local ile embedding üretimi, SQLite tabanlı vektör saklama, kaynak bulma, yerel LLM ile cevap üretme ve hızlandırılmış model yükleme aşamalarına kadar geliştirilmiştir.
