# Local RAG AI Assistant

Bu proje, yerel dokümanlardan bilgi bulabilen basit bir RAG tabanlı soru-cevap asistanıdır.

## Projenin Amacı

Bu projenin amacı, kullanıcının sorduğu soruya göre yerel dokümanlar içinden en alakalı bilgi parçalarını bulabilen bir sistem geliştirmektir.

İlerleyen aşamalarda bu sistem Microsoft Foundry Local ile birleştirilerek internet bağlantısı olmadan çalışan yerel bir yapay zeka asistanına dönüştürülecektir.

## Şu Anki Özellikler

- Python proje yapısı oluşturuldu
- `data` klasöründeki birden fazla `.txt` dosyası okunabiliyor
- Dokümanlar paragraflara ayrılıyor
- Parçalar SQLite veritabanına kaydediliyor
- Kullanıcı soru sorduğunda en alakalı kaynak parçalar bulunuyor
- Basit vektör benzerliği ile arama yapılabiliyor
- Query expansion ile bazı soru tipleri daha doğru eşleştiriliyor
- Cevapta kaynak dosya adı, parça ID ve benzerlik skoru gösteriliyor
- Bilgi dokümanlarda yoksa sistem cevap uydurmuyor
- Uygulama `python main.py` komutu ile çalışıyor

## Proje Yapısı

```text
local-rag-ai-assistant/
├── data/
│   ├── sample_doc.txt
│   └── project_faq.txt
├── docs/
│   └── project_notes.md
├── database.py
├── embeddings.py
├── ingest.py
├── main.py
├── rag.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Nasıl Çalıştırılır?

Gerekli paketleri kur:

```bash
pip install -r requirements.txt
```

Uygulamayı çalıştır:

```bash
python main.py
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
Parçaları SQLite veritabanına kaydet
↓
Kullanıcıdan soru al
↓
Soruyu query expansion ile güçlendir
↓
Soru ve doküman parçalarını vektöre çevir
↓
Cosine similarity ile en alakalı parçaları bul
↓
En iyi parçaya göre cevap göster
↓
Kaynak dosya, parça ID ve benzerlik skorunu yazdır
```

## Kullanılan Temel Kavramlar

### RAG

RAG, Retrieval-Augmented Generation anlamına gelir. Bu yöntemde sistem önce ilgili bilgiyi dokümanlardan bulur, sonra cevabı bu bilgiye göre üretir.

### SQLite

SQLite, doküman parçalarını yerel olarak saklamak için kullanılan hafif bir veritabanıdır.

### Vektör Benzerliği

Bu projede metinler basit bir yöntemle sayısal vektörlere çevrilir. Daha sonra soru vektörü ile doküman parçası vektörleri karşılaştırılır.

### Query Expansion

Kullanıcının sorusu bazı ek kelimelerle genişletilir. Örneğin “ne demek?” sorusu için “anlam”, “tanım”, “açıklama” gibi kelimeler eklenir. Böylece sistem daha doğru parçaları bulabilir.

## Örnek Çıktı

```text
Sorunuzu yazın: SQLite ne işe yarar?

=== Cevap ===
Dokümanlara göre: SQLite, doküman parçalarını saklamak için kullanılan hafif bir yerel veritabanıdır.

Kaynaklar:
- Dosya: project_faq.txt | Parça ID: 2 | Benzerlik: 0.408
```

Başka bir örnek:

```text
Sorunuzu yazın: RAG ne demek?

=== Cevap ===
Dokümanlara göre: RAG, Retrieval-Augmented Generation anlamına gelir. Önce ilgili bilgi dokümanlardan bulunur, sonra bu bilgi yapay zeka modeline bağlam olarak verilir.

Kaynaklar:
- Dosya: sample_doc.txt | Parça ID: 5 | Benzerlik: 0.524
```

Bilgi dokümanlarda yoksa:

```text
Sorunuzu yazın: Türkiye'nin başkenti neresi?

=== Cevap ===
Bu bilgi mevcut dokümanlarda bulunamadı.
```

## Dosyaların Görevleri

| Dosya           | Görevi                                                        |
| --------------- | ------------------------------------------------------------- |
| `main.py`       | Uygulamayı başlatır ve kullanıcıdan soru alır                 |
| `ingest.py`     | Dokümanları okur ve parçalara böler                           |
| `database.py`   | SQLite veritabanı işlemlerini yapar                           |
| `rag.py`        | Soruya göre en alakalı doküman parçalarını bulur              |
| `embeddings.py` | Basit vektör oluşturma ve cosine similarity işlemlerini yapar |
| `data/`         | Sistemin cevap verirken kullanacağı dokümanları içerir        |
| `docs/`         | Proje notlarını içerir                                        |

## Sonraki Hedefler

- Microsoft Foundry Local embedding modeli ile gerçek embedding araması yapmak
- Microsoft Foundry Local ile yerel LLM bağlantısı kurmak
- Daha doğal cevap üretimi sağlamak
- Kaynaklı cevap formatını geliştirmek
- Basit bir web arayüzü eklemek
- Daha fazla doküman türü desteklemek
