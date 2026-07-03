# Foundry Local Test Results

Bu dosya, Local RAG AI Assistant projesinde yapılan Microsoft Foundry Local embedding testini içerir.

## Testin Amacı

Bu testin amacı, Microsoft Foundry Local kullanarak gerçek embedding üretilebildiğini ve bu embeddingler ile doküman parçaları arasında benzerlik araması yapılabildiğini göstermektir.

Önceki sistemde eğitim amaçlı basit kelime sayımı vektörleri kullanılıyordu. Bu testte ise Foundry Local üzerinden gerçek embedding modeli çalıştırılmıştır.

## Kullanılan Dosyalar

| Dosya                       | Görevi                                                         |
| --------------------------- | -------------------------------------------------------------- |
| `foundry_embedding_test.py` | Tek bir metinden Foundry Local embedding üretimini test eder   |
| `foundry_embeddings.py`     | Foundry Local embedding işlemleri için yardımcı sınıf içerir   |
| `foundry_search_test.py`    | Doküman parçaları üzerinde Foundry Local ile arama testi yapar |
| `data/project_faq.txt`      | Testte kullanılan örnek dokümanlardan biri                     |
| `data/sample_doc.txt`       | Testte kullanılan örnek dokümanlardan biri                     |

## Kullanılan Model

```text
qwen3-embedding-0.6b
```

Bu model, metinleri embedding vektörlerine çevirmek için kullanılmıştır.

## Embedding Üretim Testi

Çalıştırılan komut:

```bash
python foundry_embedding_test.py
```

Test çıktısı özeti:

```text
Foundry Local başlatılıyor...
Embedding modeli seçiliyor...
Model indiriliyor veya önbellekten hazırlanıyor...
Model yükleniyor...
Embedding client hazırlanıyor...
Test embedding üretiliyor...
Embedding başarıyla üretildi.
Vektör boyutu: 1024
Model kapatıldı.
```

## Arama Testi

Çalıştırılan komut:

```bash
python foundry_search_test.py
```

Test sorusu:

```text
Foundry Local ne için kullanılacak?
```

## Test Sonucu

Sistem, Foundry Local embedding modelini kullanarak doküman parçalarını karşılaştırmış ve en alakalı parçayı doğru şekilde ilk sıraya getirmiştir.

Örnek çıktı:

```text
Soru: Foundry Local ne için kullanılacak?

=== Foundry Local ile En Benzer Parçalar ===

Kaynak: project_faq.txt
Benzerlik: 0.795
Final skor: 0.895
Bu proje ileride Microsoft Foundry Local ile birleştirilerek yerel yapay zeka modeliyle cevap üretecektir.
```

## Benzerlik ve Final Skor Açıklaması

### Benzerlik

Benzerlik değeri, soru embedding vektörü ile doküman parçası embedding vektörü arasındaki cosine similarity sonucudur.

Bu değer, soru ile doküman parçasının anlamsal olarak ne kadar yakın olduğunu gösterir.

### Final Skor

Final skor, embedding benzerliğine küçük bir anahtar kelime bonusu eklenmiş halidir.

```text
Final skor = Benzerlik + Anahtar kelime bonusu
```

Bu yöntem, özellikle önemli kelimeler soru ve doküman parçasında birlikte geçiyorsa doğru parçanın daha üst sıraya çıkmasına yardımcı olur.

## Değerlendirme

Test sonucuna göre:

- Foundry Local SDK başarıyla çalışmıştır.
- Embedding modeli başarıyla yüklenmiştir.
- Metinlerden 1024 boyutlu embedding vektörleri üretilebilmiştir.
- Doküman parçaları embedding ile karşılaştırılmıştır.
- Foundry Local ile ilgili doğru doküman parçası ilk sırada bulunmuştur.

Bu sonuç, projenin gerçek embedding tabanlı retrieval aşamasına geçmeye hazır olduğunu göstermektedir.

## Sonraki Hedefler

- Foundry Local embeddinglerini SQLite veritabanına kaydetmek
- Her çalıştırmada embeddingleri yeniden üretmek yerine veritabanından okumak
- `rag.py` dosyasını gerçek Foundry Local embedding sistemiyle entegre etmek
- Bulunan kaynak parçaları yerel LLM modeline bağlam olarak vermek
- Foundry Local ile doğal dilde cevap üretmek
