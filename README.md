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
- Cevapta kaynak dosya adı, parça ID ve skor gösteriliyor
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
Soruyla en alakalı parçaları bul
↓
En iyi parçaya göre cevap göster
↓
Kaynak dosya ve parça ID bilgilerini yazdır
```

## Örnek Çıktı

```text
Sorunuzu yazın: SQLite ne işe yarar?

=== Cevap ===
Dokümanlara göre: SQLite, doküman parçalarını saklamak için kullanılan hafif bir yerel veritabanıdır.

Kaynaklar:
- Dosya: project_faq.txt | Parça ID: 2 | Skor: 2
```

Bilgi dokümanlarda yoksa:

```text
Sorunuzu yazın: Türkiye'nin başkenti neresi?

=== Cevap ===
Bu bilgi mevcut dokümanlarda bulunamadı.
```

## Sonraki Hedefler

- Embedding tabanlı arama eklemek
- Vektör benzerliği ile daha akıllı retrieval yapmak
- Microsoft Foundry Local ile yerel LLM bağlantısı kurmak
- Daha doğal cevap üretimi sağlamak
- Basit bir web arayüzü eklemek
