# Demo Çıktısı: Local RAG AI Assistant

Bu dosya, Local RAG AI Assistant projesinin final sürümünde alınan örnek terminal çıktılarını içerir.

Final sürümde sistem `.txt`, `.pdf` ve `.docx` dosyalarını okuyabilir, bu dokümanlardan embedding üretebilir, SQLite veritabanına kaydedebilir ve Foundry Local üzerinde çalışan yerel LLM ile kaynaklı cevap üretebilir.

## 1. Örnek PDF ve DOCX Dosyalarının Oluşturulması

PDF ve DOCX desteğini test etmek için örnek dosyalar oluşturulmuştur.

Çalıştırılan komut:

```bash
python create_sample_documents.py
```

Örnek çıktı:

```text
DOCX dosyası oluşturuldu: data\docx_support_note.docx
PDF dosyası oluşturuldu: data\pdf_support_note.pdf
Örnek PDF ve DOCX dosyaları hazır.
```

Bu komut sonucunda `data/` klasörüne iki örnek dosya eklenmiştir:

```text
data/docx_support_note.docx
data/pdf_support_note.pdf
```

## 2. Dokümanların Okunması ve Parçalara Ayrılması

Desteklenen doküman türlerini okumak için `ingest.py` çalıştırılmıştır.

Çalıştırılan komut:

```bash
python ingest.py
```

Örnek çıktı:

```text
=== Bilgi ===
Desteklenen dosya türleri: .txt, .pdf, .docx
Kaydedilen parça sayısı: 22
```

Bu çıktı, sistemin `.txt`, `.pdf` ve `.docx` dosyalarını okuyabildiğini ve toplam 22 doküman parçası oluşturduğunu göstermektedir.

## 3. Foundry Embeddinglerinin SQLite’a Kaydedilmesi

Doküman parçaları için Foundry Local embeddingleri üretilmiş ve SQLite veritabanına kaydedilmiştir.

Çalıştırılan komut:

```bash
python foundry_ingest_test.py
```

Örnek çıktı:

```text
Toplam doküman parçası: 22
Foundry SQLite tablosu oluşturuldu.
Foundry Local başlatılıyor...
Embedding modeli seçiliyor: qwen3-embedding-0.6b
Model indiriliyor veya önbellekten hazırlanıyor...

Model yükleniyor...
Embedding client hazırlanıyor...

Embedding üretiliyor: 1/22
Kaynak: ai_notes.txt
Kaydedildi. Vektör boyutu: 1024

Embedding üretiliyor: 6/22
Kaynak: docx_support_note.docx
Kaydedildi. Vektör boyutu: 1024

Embedding üretiliyor: 12/22
Kaynak: pdf_support_note.pdf
Kaydedildi. Vektör boyutu: 1024

Embedding üretiliyor: 22/22
Kaynak: troubleshooting_faq.txt
Kaydedildi. Vektör boyutu: 1024

Model kapatıldı.

=== Kayıt Kontrolü ===
SQLite'a kaydedilen parça sayısı: 22
İlk kayıt kaynak dosyası: ai_notes.txt
İlk kayıt vektör boyutu: 1024
```

Bu çıktı, tüm doküman parçalarının embedding vektörlerinin başarıyla oluşturulduğunu ve SQLite veritabanına kaydedildiğini göstermektedir.

## 4. Final Foundry RAG Uygulamasının Başlatılması

Final uygulama şu komutla çalıştırılmıştır:

```bash
python foundry_app.py
```

Başlangıç çıktısı:

```text
Hızlandırılmış Foundry RAG Assistant başlatılıyor...
Kayıtlı doküman parçası sayısı: 22
Foundry Local başlatılıyor...
Embedding modeli hazırlanıyor: qwen3-embedding-0.6b
Chat modeli hazırlanıyor: phi-4-mini
Modeller hazır.

Soru sormaya başlayabilirsiniz.
Çıkmak için q yazabilirsiniz.
```

Bu çıktı, embedding modelinin ve chat modelinin uygulama başlangıcında bir kez yüklendiğini göstermektedir.

## 5. DOCX Desteği Demo Sorusu

Sorulan soru:

```text
DOCX desteği ne için eklendi?
```

Alınan cevap:

```text
=== Cevap ===
DOCX desteği, Local RAG AI Assistant projesinin Word belgelerini okuyabilmesi için eklendi.

=== Kaynaklar ===
- Dosya: docx_support_note.docx | Parça ID: 6 | Benzerlik: 0.606 | Final skor: 0.606
- Dosya: docx_support_note.docx | Parça ID: 5 | Benzerlik: 0.575 | Final skor: 0.575
- Dosya: docx_support_note.docx | Parça ID: 7 | Benzerlik: 0.541 | Final skor: 0.541
```

Bu örnek, sistemin DOCX dosyasını okuyabildiğini ve soruya doğru Word belgesini kaynak göstererek cevap verdiğini göstermektedir.

## 6. PDF Desteği Demo Sorusu

Sorulan soru:

```text
PDF desteği ne için eklendi?
```

Alınan cevap:

```text
=== Cevap ===
PDF desteği, Local RAG AI Assistant projesinin PDF belgelerini okuyabilmesi için eklenmiştir.

=== Kaynaklar ===
- Dosya: pdf_support_note.pdf | Parça ID: 12 | Benzerlik: 0.636 | Final skor: 1.586
- Dosya: docx_support_note.docx | Parça ID: 6 | Benzerlik: 0.505 | Final skor: 0.555
- Dosya: docx_support_note.docx | Parça ID: 5 | Benzerlik: 0.535 | Final skor: 0.535
```

Bu örnek, sistemin PDF dosyasını okuyabildiğini ve doğru PDF dosyasını en alakalı kaynak olarak bulduğunu göstermektedir.

## 7. RAG Sorusu Demo Çıktısı

Sorulan soru:

```text
RAG ne demek?
```

Örnek cevap:

```text
=== Cevap ===
RAG, Retrieval-Augmented Generation anlamına gelir. Önce ilgili bilgi dokümanlardan bulunur, sonra bu bilgi yapay zeka modeline bağlam olarak verilir.

=== Kaynaklar ===
- Dosya: sample_doc.txt | Parça ID: 17 | Benzerlik: 0.852 | Final skor: 0.902
```

Bu örnek, sistemin RAG ile ilgili bilgiyi yerel dokümanlardan bulup kaynaklı cevap üretebildiğini göstermektedir.

## 8. Dokümanda Olmayan Bilgi Demo Çıktısı

Sorulan soru:

```text
Türkiye'nin başkenti neresi?
```

Alınan cevap:

```text
=== Cevap ===
Bu bilgi mevcut dokümanlarda bulunamadı.
```

Bu çıktı, sistemin dokümanlarda bulunmayan bilgi için cevap uydurmadığını göstermektedir.

## 9. Programdan Çıkış

Çıkmak için kullanıcı `q` yazmıştır.

Örnek çıktı:

```text
Sorunuzu yazın: q
Program kapatıldı.
Chat modeli kapatıldı.
Embedding modeli kapatıldı.
```

Bu çıktı, program kapanırken chat modelinin ve embedding modelinin güvenli şekilde kapatıldığını göstermektedir.

## 10. Demo Sonucu

Demo sonucunda sistemin şu özellikleri başarıyla gösterilmiştir:

- `.txt` dosyalarını okuma
- `.pdf` dosyalarını okuma
- `.docx` dosyalarını okuma
- Dokümanları parçalara ayırma
- Foundry Local ile embedding üretme
- Embeddingleri SQLite veritabanına kaydetme
- Kullanıcı sorusuna göre kaynak bulma
- Yerel LLM ile cevap üretme
- Cevapla birlikte kaynak gösterme
- Dokümanda olmayan bilgi için cevap uydurmama
- Modelleri başlangıçta bir kez yükleyip program kapanırken güvenli şekilde kapatma

Bu demo, Local RAG AI Assistant projesinin final sürümünün çalışır durumda olduğunu göstermektedir.
