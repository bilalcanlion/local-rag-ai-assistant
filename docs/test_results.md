# Test Results

Bu dosya, Local RAG AI Assistant projesinde yapılan temel retrieval testlerini içerir.

## Test Ortamı

- Uygulama: Local RAG AI Assistant
- Test komutu: `python test_queries.py`
- Veri klasörü: `data/`
- Toplam doküman parçası: 6
- Test edilen özellik: Soruya göre doğru kaynak parçayı bulma

## Test Senaryoları

| No  | Soru                                | Beklenen Sonuç                     | Durum    |
| --- | ----------------------------------- | ---------------------------------- | -------- |
| 1   | RAG ne demek?                       | RAG açıklamasını bulmalı           | Başarılı |
| 2   | SQLite ne işe yarar?                | SQLite açıklamasını bulmalı        | Başarılı |
| 3   | Foundry Local ne için kullanılacak? | Foundry Local açıklamasını bulmalı | Başarılı |
| 4   | Türkiye'nin başkenti neresi?        | Bilgi bulunamadı demeli            | Başarılı |

## Test Çıktısı

```text
=== Testler Başlıyor ===
Kaydedilen parça sayısı: 6

--- Test 1 ---
Soru: RAG ne demek?
Sonuç: BAŞARILI
Bulunan cevap: RAG, Retrieval-Augmented Generation anlamına gelir. Önce ilgili bilgi dokümanlardan bulunur, sonra bu bilgi yapay zeka modeline bağlam olarak verilir.

--- Test 2 ---
Soru: SQLite ne işe yarar?
Sonuç: BAŞARILI
Bulunan cevap: SQLite, doküman parçalarını saklamak için kullanılan hafif bir yerel veritabanıdır.

--- Test 3 ---
Soru: Foundry Local ne için kullanılacak?
Sonuç: BAŞARILI
Bulunan cevap: Bu proje ileride Microsoft Foundry Local ile birleştirilerek yerel yapay zeka modeliyle cevap üretecektir.

--- Test 4 ---
Soru: Türkiye'nin başkenti neresi?
Sonuç: BAŞARILI
Beklenen: Bilgi bulunamadı.

=== Test Özeti ===
Başarılı test sayısı: 4
Toplam test sayısı: 4
```

## Değerlendirme

Test sonuçlarına göre sistem, dokümanlarda bulunan bilgiler için doğru kaynak parçalarını bulabilmektedir.

Sistem şu sorularda doğru sonuç vermiştir:

- RAG ne demek?
- SQLite ne işe yarar?
- Foundry Local ne için kullanılacak?

Ayrıca dokümanlarda bulunmayan bir soru sorulduğunda sistem cevap uydurmamış ve bilgi bulunamadığını belirtmiştir.

Bu sonuçlar, temel retrieval mantığının çalıştığını göstermektedir.

## Sonraki Test Hedefleri

- Daha fazla örnek soru eklemek
- Daha uzun dokümanlarla test yapmak
- Farklı konu başlıklarında dokümanlar eklemek
- Retrieval kalitesini daha fazla soru ile ölçmek
- Microsoft Foundry Local entegrasyonundan sonra cevap kalitesini tekrar test etmek
