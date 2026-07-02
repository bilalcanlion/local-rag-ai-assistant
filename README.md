# Local RAG AI Assistant

Bu proje, yerel dokümanlardan bilgi bulabilen basit bir RAG tabanlı yapay zeka asistanı geliştirmek için hazırlanmıştır.

## Projenin Amacı

Bu projenin amacı, kullanıcının sorduğu soruya göre yerel dokümanlar içinden en alakalı bilgi parçasını bulabilen bir sistem oluşturmaktır.

İlerleyen aşamalarda bu sistem Microsoft Foundry Local ile birleştirilerek internet bağlantısı olmadan çalışan yerel bir soru-cevap asistanına dönüştürülecektir.

## Şu Anki Özellikler

- Python proje yapısı oluşturuldu
- Örnek doküman `data/sample_doc.txt` içine eklendi
- Doküman Python ile okunabiliyor
- Doküman paragraflara ayrılabiliyor
- Parçalar SQLite veritabanına kaydediliyor
- Kullanıcı soru sorduğunda en alakalı kaynak parça bulunuyor
- Uygulama `python main.py` komutu ile çalışıyor

## Proje Yapısı

```text
local-rag-ai-assistant/
├── data/
│   └── sample_doc.txt
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
