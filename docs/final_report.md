# Final Proje Raporu: Local RAG AI Assistant

## 1. Proje Özeti

Local RAG AI Assistant, yerel dokümanlardan bilgi bulabilen ve bu bilgileri yerel bir yapay zeka modeliyle cevap haline getirebilen RAG tabanlı bir soru-cevap asistanıdır.

Proje ilk olarak eğitim amaçlı basit bir retrieval sistemi olarak başlamıştır. Daha sonra Microsoft Foundry Local kullanılarak gerçek embedding üretimi, SQLite tabanlı vektör saklama, kaynak bulma ve yerel LLM ile cevap üretme aşamalarına kadar geliştirilmiştir.

Final sürümde sistem `.txt`, `.pdf` ve `.docx` dosyalarını okuyabilir. Kullanıcının sorduğu soruya göre yerel dokümanlar içinden ilgili parçaları bulur, bu parçaları yerel chat modeline bağlam olarak verir ve kısa bir cevap üretir.

## 2. Projenin Amacı

Bu projenin amacı, internet bağlantısına ihtiyaç duymadan yerel dokümanlar üzerinden çalışan bir soru-cevap asistanı geliştirmektir.

Sistem şu hedeflere göre tasarlanmıştır:

- Yerel `.txt`, `.pdf` ve `.docx` dosyalarını okuyabilmek
- Dokümanları küçük parçalara ayırmak
- Doküman parçalarını SQLite veritabanında saklamak
- Microsoft Foundry Local ile embedding üretmek
- Embeddingleri yerel veritabanında saklamak
- Kullanıcı sorusuna göre en alakalı doküman parçalarını bulmak
- Bulunan kaynak parçaları yerel LLM modeline bağlam olarak vermek
- Kısa ve anlaşılır cevap üretmek
- Cevapla birlikte kaynak bilgilerini göstermek
- Dokümanda olmayan bilgi için cevap uydurmamak

Bu sayede proje, yerel dokümanlara dayalı güvenli ve kaynaklı bir yapay zeka asistanı örneği sunmaktadır.

## 3. Kullanılan Teknolojiler

| Teknoloji               | Kullanım Amacı                                             |
| ----------------------- | ---------------------------------------------------------- |
| Python                  | Ana programlama dili                                       |
| SQLite                  | Doküman parçalarını ve embeddingleri yerel olarak saklamak |
| Microsoft Foundry Local | Yerel model çalıştırmak                                    |
| Foundry Local SDK       | Python üzerinden Foundry Local modellerini kullanmak       |
| qwen3-embedding-0.6b    | Yerel embedding modeli                                     |
| phi-4-mini              | Yerel chat modeli                                          |
| Cosine similarity       | Soru ve doküman embeddingleri arasındaki benzerliği ölçmek |
| Query expansion         | Soruları ek anahtar kelimelerle güçlendirmek               |
| pypdf                   | PDF dosyalarından metin çıkarmak                           |
| python-docx             | DOCX dosyalarından metin çıkarmak                          |
| GitHub                  | Versiyon kontrolü ve proje paylaşımı                       |

## 4. Sistem Mimarisi

Final sistemin genel mimarisi şu şekildedir:

```text
Yerel dokümanlar (.txt / .pdf / .docx)
↓
Doküman okuma
↓
Metin parçalama
↓
Foundry Local ile embedding üretimi
↓
Embeddingleri SQLite’a kaydetme
↓
Kullanıcı sorusu
↓
Soru embedding üretimi
↓
Benzerlik araması
↓
İlgili kaynak parçaları bulma
↓
Kaynakları yerel LLM modeline bağlam olarak verme
↓
Cevap üretimi
↓
Cevap + kaynak gösterimi
```

Bu yapı sayesinde sistem hem bilgi arama hem de cevap üretme adımlarını tamamen yerel ortamda gerçekleştirebilir.

## 5. Veri Hazırlama

Projedeki dokümanlar `data/` klasörü içinde tutulmaktadır.

Kullanılan örnek veri dosyaları:

```text
data/sample_doc.txt
data/project_faq.txt
data/ai_notes.txt
data/foundry_manual.txt
data/troubleshooting_faq.txt
data/docx_support_note.docx
data/pdf_support_note.pdf
```

`ingest.py` dosyası bu dokümanları okur ve paragraflara göre küçük parçalara ayırır.

Dokümanları küçük parçalara ayırmak önemlidir. Çünkü sistem tüm dokümanı tek seferde aramak yerine daha küçük ve anlamlı parçalar üzerinde arama yapar. Böylece kullanıcının sorusuna daha alakalı kaynaklar bulunabilir.

## 6. Desteklenen Dosya Türleri

Final sürümde sistem şu dosya türlerini desteklemektedir:

```text
.txt
.pdf
.docx
```

TXT dosyaları doğrudan okunur.

PDF dosyaları için `pypdf` kütüphanesi kullanılır.

DOCX dosyaları için `python-docx` kütüphanesi kullanılır.

Bu destek sayesinde sistem yalnızca düz metin dosyalarıyla değil, PDF ve Word belgeleriyle de çalışabilir.

## 7. Basit RAG Sürümü

Projenin ilk aşamasında eğitim amaçlı basit bir RAG sistemi oluşturulmuştur.

Bu sürümde kullanılan ana dosyalar:

```text
main.py
rag.py
embeddings.py
database.py
ingest.py
```

Bu sürümde metinler basit kelime sayımı mantığıyla vektöre çevrilmiştir. Daha sonra kullanıcı sorusu ile doküman parçaları arasında cosine similarity hesaplanmıştır.

Basit sürümün çalışma mantığı:

```text
Kullanıcı sorusu
↓
Soru vektöre çevrilir
↓
Doküman parçalarıyla karşılaştırılır
↓
En alakalı parça bulunur
↓
Cevap olarak gösterilir
```

Bu sürüm, RAG mantığını öğrenmek için faydalı olmuştur. Ancak kelime sayımı tabanlı olduğu için anlam benzerliğini sınırlı şekilde yakalayabilmiştir.

## 8. Microsoft Foundry Local Entegrasyonu

Daha sonra projeye Microsoft Foundry Local entegrasyonu eklenmiştir.

İlk olarak tek bir metin için embedding üretimi test edilmiştir.

Bu test için kullanılan dosya:

```text
foundry_embedding_test.py
```

Kullanılan embedding modeli:

```text
qwen3-embedding-0.6b
```

Test sonucunda 1024 boyutlu embedding vektörü başarıyla üretilmiştir.

Bu aşama, Foundry Local SDK’nın doğru kurulduğunu ve yerel embedding modelinin çalıştığını göstermiştir.

## 9. Embeddingleri SQLite’a Kaydetme

Embedding üretimi çalıştıktan sonra doküman parçalarının embeddingleri SQLite veritabanına kaydedilmiştir.

Bu aşamada kullanılan ana dosyalar:

```text
foundry_database.py
foundry_ingest_test.py
```

Çalışma akışı:

```text
data klasöründeki dokümanları oku
↓
Dokümanları küçük parçalara böl
↓
Her parça için Foundry Local embedding üret
↓
Kaynak dosya adı, içerik ve embedding bilgisini SQLite’a kaydet
```

Bu yapı sayesinde doküman embeddingleri her soru için yeniden üretilmek zorunda kalmaz. Embeddingler bir kez oluşturulur ve veritabanından tekrar kullanılabilir.

PDF ve DOCX desteği eklendikten sonra sistem 22 doküman parçasını başarıyla işlemiş ve embedding veritabanına kaydetmiştir.

## 10. Stored Embedding Retrieval

Daha sonra SQLite içinde kayıtlı embeddinglerle arama yapılmıştır.

Bu test için kullanılan dosya:

```text
foundry_retrieval_test.py
```

Bu aşamada sistem şu adımları uygulamıştır:

1. Kullanıcı sorusunu alır
2. Soruyu query expansion ile güçlendirir
3. Soruyu embedding vektörüne çevirir
4. SQLite’taki kayıtlı doküman embeddinglerini okur
5. Cosine similarity hesaplar
6. Anahtar kelime bonusu ekler
7. Final skora göre sonuçları sıralar
8. En alakalı kaynak parçaları döndürür

Test edilen örnek sorular:

```text
RAG ne demek?
SQLite ne işe yarar?
Foundry Local ne için kullanılacak?
Türkiye'nin başkenti neresi?
DOCX desteği ne için eklendi?
PDF desteği ne için eklendi?
```

Sistem dokümanlarda bulunan sorular için doğru kaynakları bulmuş, dokümanda olmayan soru için ise cevap uydurmamıştır.

## 11. Yerel Chat Modeli Testi

Retrieval sistemi çalıştıktan sonra yerel LLM ile cevap üretimi test edilmiştir.

Bu test için kullanılan dosya:

```text
foundry_chat_test.py
```

Test edilen modeller:

```text
qwen2.5-0.5b
qwen2.5-1.5b
phi-3.5-mini
phi-4-mini
```

Küçük Qwen modelleri bazı durumlarda zayıf, tekrar eden veya bağlamdan kopan cevaplar üretmiştir.

`phi-3.5-mini` daha iyi sonuç vermiştir. Daha sonra `phi-4-mini` denenmiş ve cevap kalitesi daha iyi bulunduğu için final uygulamada bu model seçilmiştir.

Final chat modeli:

```text
phi-4-mini
```

## 12. RAG + LLM Cevap Üretimi

Bir sonraki aşamada retrieval ve LLM cevap üretimi birleştirilmiştir.

Bu test için kullanılan dosya:

```text
foundry_rag_answer_test.py
```

Çalışma mantığı:

```text
Kullanıcı sorusu
↓
İlgili doküman parçalarını bul
↓
Bu parçaları bağlam olarak hazırla
↓
Bağlamı ve soruyu phi-4-mini modeline gönder
↓
Kısa cevap üret
```

Bu aşamada modelin sadece verilen bağlama göre cevap vermesi istenmiştir. Böylece sistemin doküman dışı bilgi uydurma riski azaltılmıştır.

## 13. Final Etkileşimli Uygulama

Final uygulama dosyası:

```text
foundry_app.py
```

Uygulama şu komutla çalıştırılır:

```bash
python foundry_app.py
```

Kullanıcı uygulama açıldıktan sonra sorularını terminal üzerinden sorabilir.

Örnek sorular:

```text
RAG ne demek?
SQLite ne işe yarar?
Foundry Local ne için kullanılacak?
Yapay zeka nedir?
RAG halüsinasyonu nasıl azaltır?
Foundry veritabanında kayıtlı parça yoksa ne yapmalıyım?
DOCX desteği ne için eklendi?
PDF desteği ne için eklendi?
Türkiye'nin başkenti neresi?
```

Çıkmak için:

```text
q
```

yazılır.

Final uygulama cevapla birlikte kaynakları da gösterir:

```text
=== Kaynaklar ===
- Dosya: sample_doc.txt | Parça ID: 17 | Benzerlik: 0.852 | Final skor: 0.902
```

Bu sayede kullanıcı cevabın hangi doküman parçasına dayandığını görebilir.

## 14. Hızlandırma Çalışması

İlk LLM entegrasyonunda embedding modeli ve chat modeli her soru için yeniden yükleniyordu. Bu durum uygulamayı yavaşlatıyordu.

Bu sorunu çözmek için önce ayrı bir test dosyası oluşturuldu:

```text
foundry_app_fast_test.py
```

Bu dosyada modeller uygulama başında bir kez yüklendi ve kullanıcı çıkana kadar açık tutuldu.

Başarılı testten sonra aynı mantık `foundry_app.py` dosyasına taşındı.

Final uygulamada artık süreç şöyledir:

```text
Uygulama başlar
↓
Embedding modeli bir kez yüklenir
↓
Chat modeli bir kez yüklenir
↓
Kullanıcı birden fazla soru sorar
↓
Programdan çıkarken modeller kapatılır
```

Çıkışta modeller güvenli şekilde kapatılır:

```text
Chat modeli kapatıldı.
Embedding modeli kapatıldı.
```

Bu değişiklik uygulamanın kullanımını daha verimli hale getirmiştir.

## 15. PDF ve DOCX Desteği

Projede başlangıçta yalnızca `.txt` dosyaları destekleniyordu.

Daha sonra `ingest.py` dosyası güncellenerek `.pdf` ve `.docx` dosyaları da desteklenmiştir.

PDF desteği için:

```text
pypdf
```

DOCX desteği için:

```text
python-docx
```

kullanılmıştır.

Örnek PDF ve DOCX dosyaları oluşturmak için şu dosya eklenmiştir:

```text
create_sample_documents.py
```

Bu dosya şu örnek belgeleri üretir:

```text
data/docx_support_note.docx
data/pdf_support_note.pdf
```

DOCX desteği şu soru ile test edilmiştir:

```text
DOCX desteği ne için eklendi?
```

Sistem doğru şekilde `docx_support_note.docx` dosyasını kaynak olarak bulmuştur.

PDF desteği şu soru ile test edilmiştir:

```text
PDF desteği ne için eklendi?
```

Sistem doğru şekilde `pdf_support_note.pdf` dosyasını kaynak olarak bulmuştur.

## 16. Örnek Çıktılar

### 16.1 RAG Sorusu

Örnek soru:

```text
RAG ne demek?
```

Örnek cevap:

```text
RAG, Retrieval-Augmented Generation anlamına gelir. Önce ilgili bilgi dokümanlardan bulunur, sonra bu bilgi yapay zeka modeline bağlam olarak verilir.
```

Kaynaklar:

```text
=== Kaynaklar ===
- Dosya: sample_doc.txt | Parça ID: 17 | Benzerlik: 0.852 | Final skor: 0.902
```

### 16.2 DOCX Sorusu

Örnek soru:

```text
DOCX desteği ne için eklendi?
```

Örnek cevap:

```text
DOCX desteği, Local RAG AI Assistant projesinin Word belgelerini okuyabilmesi için eklendi.
```

Kaynaklar:

```text
=== Kaynaklar ===
- Dosya: docx_support_note.docx | Parça ID: 6 | Benzerlik: 0.606 | Final skor: 0.606
- Dosya: docx_support_note.docx | Parça ID: 5 | Benzerlik: 0.575 | Final skor: 0.575
- Dosya: docx_support_note.docx | Parça ID: 7 | Benzerlik: 0.541 | Final skor: 0.541
```

### 16.3 PDF Sorusu

Örnek soru:

```text
PDF desteği ne için eklendi?
```

Örnek cevap:

```text
PDF desteği, Local RAG AI Assistant projesinin PDF belgelerini okuyabilmesi için eklenmiştir.
```

Kaynak:

```text
=== Kaynaklar ===
- Dosya: pdf_support_note.pdf | Parça ID: 12 | Benzerlik: 0.636 | Final skor: 1.586
```

### 16.4 Dokümanda Olmayan Bilgi

Dokümanda olmayan bilgi örneği:

```text
Türkiye'nin başkenti neresi?
```

Cevap:

```text
Bu bilgi mevcut dokümanlarda bulunamadı.
```

Bu örnek, sistemin dokümanda olmayan bilgiyi uydurmadığını göstermektedir.

## 17. Karşılaşılan Sorunlar

### 17.1 Basit vektör sisteminin sınırlı kalması

İlk sürümde kullanılan kelime sayımı tabanlı vektör sistemi, yalnızca benzer kelimeler geçtiğinde iyi çalışıyordu. Farklı kelimelerle sorulan ama anlam olarak benzer sorularda yetersiz kalabiliyordu.

### 17.2 Model kalitesi sorunu

Bazı küçük chat modelleri doğru veya akıcı cevap veremedi. Özellikle küçük Qwen modelleri bazı testlerde tekrar eden ve bağlamdan kopan cevaplar üretti.

Bu nedenle farklı modeller test edildi ve finalde `phi-4-mini` seçildi.

### 17.3 Singleton hatası

Geliştirme sırasında şu hata ile karşılaşıldı:

```text
FoundryLocalManager is a singleton and has already been initialized.
```

Bu hata, FoundryLocalManager’ın aynı program içinde birden fazla kez başlatılmaya çalışılmasından kaynaklandı.

Çözüm olarak Foundry Local bir kez başlatıldı ve daha sonra aynı manager instance’ı tekrar kullanıldı.

### 17.4 Yavaş model yükleme

İlk denemelerde modeller her soru için tekrar yükleniyordu. Bu durum özellikle yerel LLM kullanımında uygulamayı yavaşlatıyordu.

Çözüm olarak modeller uygulama başında bir kez yüklendi ve program kapanırken kapatıldı.

### 17.5 PDF retrieval sorunu

PDF dosyası okunup embedding veritabanına kaydedildiği halde, ilk testte “PDF desteği ne için eklendi?” sorusunda PDF kaynağı üst sıraya çıkmadı.

Bu sorun `expand_query` ve `keyword_bonus` fonksiyonlarına PDF/DOCX odaklı kurallar eklenerek çözüldü.

## 18. Çözümler

Projede karşılaşılan sorunlara şu çözümler uygulanmıştır:

| Sorun                                            | Çözüm                                                                 |
| ------------------------------------------------ | --------------------------------------------------------------------- |
| Basit kelime benzerliği yetersiz kaldı           | Foundry Local embedding modeline geçildi                              |
| Bazı sorularda doğru parça üst sıraya çıkmadı    | Query expansion ve final skor mantığı eklendi                         |
| Doküman embeddingleri tekrar tekrar üretiliyordu | Embeddingler SQLite’a kaydedildi                                      |
| Küçük chat modelleri kötü cevap verdi            | Farklı modeller test edildi ve `phi-4-mini` seçildi                   |
| FoundryLocalManager singleton hatası alındı      | Manager bir kez başlatılıp tekrar kullanıldı                          |
| Modeller her soruda yeniden yükleniyordu         | Modeller başlangıçta bir kez yüklenir hale getirildi                  |
| Sadece `.txt` dosyaları destekleniyordu          | `.pdf` ve `.docx` okuma desteği eklendi                               |
| PDF kaynağı ilk testte üst sıraya çıkmadı        | PDF/DOCX için özel query expansion ve keyword bonus kuralları eklendi |

## 19. Mevcut Sınırlamalar

Projenin şu anki sınırlamaları şunlardır:

- Yerel LLM bazen Türkçe cümlelerde küçük anlatım bozuklukları yapabilir.
- İlk açılışta modellerin yüklenmesi biraz zaman alabilir.
- Cevap kalitesi, dokümanların içeriğine ve bulunan kaynak parçaların kalitesine bağlıdır.
- PDF desteği metin içeren PDF dosyaları için uygundur.
- Taranmış görsel PDF dosyaları için OCR desteği yoktur.
- Henüz web arayüzü bulunmamaktadır.
- Daha kapsamlı test senaryoları eklenebilir.

## 20. Gelecek Geliştirmeler

Projeye ileride şu özellikler eklenebilir:

- Taranmış PDF dosyaları için OCR desteği
- Daha temiz cevap formatı
- Daha gelişmiş prompt tasarımı
- Daha fazla test senaryosu
- Basit bir web arayüzü
- Ekran görüntüsü veya demo çıktıları
- Daha iyi retrieval metrikleri
- Final sunum dosyası
- Kullanıcı dostu kurulum yönergeleri

## 21. Sonuç

Local RAG AI Assistant projesi, basit bir eğitim prototipinden çalışan bir yerel RAG uygulamasına dönüştürülmüştür.

Final sistem şu özelliklere sahiptir:

- Yerel dokümanları okuyabilir
- `.txt`, `.pdf` ve `.docx` dosyalarını destekler
- Dokümanları parçalara ayırabilir
- Microsoft Foundry Local ile embedding üretebilir
- Embeddingleri SQLite veritabanında saklayabilir
- Kullanıcı sorusuna göre ilgili kaynakları bulabilir
- Yerel LLM ile cevap üretebilir
- Cevapla birlikte kaynak gösterebilir
- Dokümanda olmayan bilgi için cevap uydurmaz
- Modelleri uygulama başında bir kez yükleyerek daha hızlı çalışabilir

Bu proje, Python, SQLite ve Microsoft Foundry Local kullanılarak yerel ortamda Retrieval-Augmented Generation mantığının nasıl kurulabileceğini göstermektedir.
