# Demo Output: Local RAG AI Assistant

Bu dosya, Local RAG AI Assistant projesinin örnek çalışma çıktısını göstermektedir.

Demo, final Foundry tabanlı uygulama olan `foundry_app.py` üzerinden alınmıştır.

## Çalıştırma Komutu

```bash
python foundry_app.py
```

## Program Başlangıcı

```text
Hızlandırılmış Foundry RAG Assistant başlatılıyor...
Kayıtlı doküman parçası sayısı: 6
Foundry Local başlatılıyor...
Embedding modeli hazırlanıyor: qwen3-embedding-0.6b
Chat modeli hazırlanıyor: phi-4-mini
Modeller hazır.

Soru sormaya başlayabilirsiniz.
Çıkmak için q yazabilirsiniz.
```

Bu başlangıç çıktısı, sistemin iki modeli uygulama başında bir kez yüklediğini gösterir:

```text
qwen3-embedding-0.6b
phi-4-mini
```

Embedding modeli kullanıcı sorusunu vektöre çevirmek için kullanılır.  
Chat modeli ise bulunan kaynak parçalarına göre doğal cevap üretir.

---

## Demo 1: RAG Sorusu

### Kullanıcı Sorusu

```text
RAG ne demek?
```

### Sistem Cevabı

```text
=== Cevap ===
RAG, Retrieval-Augmented Generation anlamına gelir. Önce ilgili bilgi dokümanlardan bulunur, sonra bu bilgi yapay zeka modeline bağlam olarak verilir.
```

### Kaynaklar

```text
=== Kaynaklar ===
- Dosya: sample_doc.txt | Parça ID: 5 | Benzerlik: 0.852 | Final skor: 0.902
- Dosya: sample_doc.txt | Parça ID: 4 | Benzerlik: 0.541 | Final skor: 0.591
```

### Yorum

Bu örnekte sistem, RAG ile ilgili bilgiyi `sample_doc.txt` dosyasındaki ilgili parçalardan bulmuştur.

Cevap, doğrudan dokümanda bulunan bilgiye dayanmaktadır.

---

## Demo 2: SQLite Sorusu

### Kullanıcı Sorusu

```text
SQLite ne işe yarar?
```

### Sistem Cevabı

```text
=== Cevap ===
SQLite, soruların cevaplandığı yerel dokümanlardan yapılan soru-cevap sistemlerinde saklanması için kullanılan hafif bir yerel veritabanıdır.
```

### Kaynaklar

```text
=== Kaynaklar ===
- Dosya: project_faq.txt | Parça ID: 2 | Benzerlik: 0.772 | Final skor: 0.822
- Dosya: sample_doc.txt | Parça ID: 4 | Benzerlik: 0.457 | Final skor: 0.457
- Dosya: sample_doc.txt | Parça ID: 6 | Benzerlik: 0.395 | Final skor: 0.395
```

### Yorum

Bu örnekte sistem, SQLite ile ilgili en alakalı bilgiyi `project_faq.txt` dosyasından bulmuştur.

Kaynaklar kısmında en yüksek final skora sahip parçanın en alakalı kaynak olduğu görülmektedir.

---

## Demo 3: Foundry Local Sorusu

### Kullanıcı Sorusu

```text
Foundry Local ne için kullanılacak?
```

### Sistem Cevabı

```text
=== Cevap ===
Foundry Local, yerel yapay zeka modeliyle cevap üretmek için Microsoft Foundry ile birleştirilecek.
```

### Kaynaklar

```text
=== Kaynaklar ===
- Dosya: project_faq.txt | Parça ID: 3 | Benzerlik: 0.815 | Final skor: 0.915
- Dosya: sample_doc.txt | Parça ID: 4 | Benzerlik: 0.495 | Final skor: 0.545
- Dosya: project_faq.txt | Parça ID: 2 | Benzerlik: 0.438 | Final skor: 0.438
```

### Yorum

Bu örnekte sistem, Foundry Local ile ilgili bilgiyi `project_faq.txt` dosyasındaki üçüncü parçadan bulmuştur.

Final skorun yüksek olması, bu parçanın soruyla güçlü şekilde ilişkili olduğunu göstermektedir.

---

## Demo 4: Dokümanda Olmayan Bilgi

### Kullanıcı Sorusu

```text
Türkiye'nin başkenti neresi?
```

### Sistem Cevabı

```text
=== Cevap ===
Bu bilgi mevcut dokümanlarda bulunamadı.
```

### Yorum

Bu örnek, projenin en önemli davranışlarından birini göstermektedir.

Sistemin yerel dokümanlarında Türkiye'nin başkenti ile ilgili bilgi yoktur. Bu yüzden sistem cevap uydurmamış ve bilginin mevcut dokümanlarda bulunmadığını söylemiştir.

Bu davranış, RAG sistemlerinde güvenilirlik açısından önemlidir.

---

## Programdan Çıkış

### Kullanıcı Girişi

```text
q
```

### Program Çıkışı

```text
Program kapatıldı.
Chat modeli kapatıldı.
Embedding modeli kapatıldı.
```

### Yorum

Bu çıktı, uygulamanın çıkış sırasında modelleri güvenli şekilde kapattığını gösterir.

Final sürümde modeller her soru için tekrar yüklenmez. Bunun yerine uygulama başında bir kez yüklenir ve program kapanırken kapatılır.

---

## Demo Özeti

Bu demo çıktısı, final uygulamanın şu özellikleri başarıyla yaptığını göstermektedir:

- Kullanıcıdan soru alır
- Soruyu embedding vektörüne çevirir
- SQLite içindeki kayıtlı embeddinglerle karşılaştırır
- En alakalı kaynak parçaları bulur
- Bulunan kaynakları `phi-4-mini` modeline bağlam olarak verir
- Kısa ve anlaşılır cevap üretir
- Cevapla birlikte kaynak dosya, parça ID, benzerlik ve final skor gösterir
- Dokümanda olmayan bilgi için cevap uydurmaz
- Program kapanırken modelleri güvenli şekilde kapatır

## Kullanılan Modeller

| Model                  | Görev                                 |
| ---------------------- | ------------------------------------- |
| `qwen3-embedding-0.6b` | Soru ve doküman embeddingleri üretmek |
| `phi-4-mini`           | Bulunan kaynaklara göre cevap üretmek |

## Sonuç

Demo sonucunda Local RAG AI Assistant uygulamasının temel RAG akışını başarıyla gerçekleştirdiği görülmüştür.

Sistem, yerel dokümanlardan bilgi bulmuş, bulunan kaynaklara göre cevap üretmiş ve dokümanda olmayan bilgi için cevap uydurmamıştır.
