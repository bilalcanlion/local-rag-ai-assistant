# Foundry Local Integration Notes

Bu dosya, Local RAG AI Assistant projesinin Microsoft Foundry Local entegrasyonu için hazırlık notlarını içerir.

## Mevcut Durum

Proje şu anda çalışan bir temel RAG altyapısına sahiptir.

Mevcut sistem şunları yapabilmektedir:

- `data` klasöründeki `.txt` dosyalarını okur
- Dokümanları paragraflara böler
- Parçaları SQLite veritabanına kaydeder
- Kullanıcı sorusunu alır
- Basit vektör benzerliği ile en alakalı parçaları bulur
- Query expansion ile bazı soru tiplerini daha iyi eşleştirir
- Cevapta kaynak dosya, parça ID ve benzerlik skorunu gösterir
- Bilgi dokümanlarda yoksa cevap uydurmaz

## Şu Anki Embedding Mantığı

Şu an projede gerçek embedding modeli kullanılmamaktadır.

Bunun yerine eğitim amaçlı basit bir yöntem kullanılmaktadır:

1. Metin kelimelere ayrılır.
2. Her metin basit kelime sayımı vektörüne çevrilir.
3. Soru vektörü ile doküman parçası vektörleri karşılaştırılır.
4. Cosine similarity ile en benzer parçalar bulunur.

Bu yöntem, embedding ve vektör arama mantığını öğrenmek için hazırlanmıştır.

## Foundry Local ile Hedeflenen Geliştirme

Microsoft Foundry Local entegrasyonuyla hedeflenen yapı şudur:

1. Doküman parçalarını gerçek embedding modelinden geçir.
2. Üretilen embedding vektörlerini SQLite içinde sakla.
3. Kullanıcı sorusunu aynı embedding modeliyle vektöre çevir.
4. Soru vektörü ile doküman vektörlerini karşılaştır.
5. En alakalı kaynak parçaları bul.
6. Bulunan parçaları yerel LLM modeline bağlam olarak ver.
7. Yerel modelden doğal dilde cevap üret.

## Beklenen Nihai Akış

```text
Kullanıcı sorusu
↓
Soru embedding vektörüne çevrilir
↓
SQLite içindeki doküman embeddingleriyle karşılaştırılır
↓
En alakalı parçalar seçilir
↓
Bu parçalar prompt içine bağlam olarak eklenir
↓
Foundry Local üzerinde çalışan yerel LLM cevap üretir
↓
Cevap kaynak bilgileriyle birlikte kullanıcıya gösterilir
```

## Kurulum Notu

Foundry Local kurulumu ve SDK kullanımı, cihaz ve işletim sistemi durumuna göre değişebilir.

Bu nedenle mevcut çalışan sistem korunacak, Foundry Local entegrasyonu ayrı bir aşamada ve kontrollü şekilde eklenecektir.

## Sonraki Teknik Hedefler

- Foundry Local SDK kurulumunu test etmek
- Yerel embedding modeliyle örnek embedding üretmek
- Mevcut `embeddings.py` dosyasını Foundry Local embedding modeliyle geliştirmek
- SQLite tablosuna embedding alanı eklemek
- Retrieval sistemini gerçek embedding sonuçlarına bağlamak
- Yerel LLM ile cevap üretmek

## Proje Planıyla İlişkisi

Bu notlar, proje planında geçen Foundry Local, embeddings, vector search, SQLite ve RAG uygulama entegrasyonu aşamalarına hazırlık amacıyla oluşturulmuştur.
