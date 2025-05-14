# 🍍 Meyve Sınıflandırıcı - Yapay Zeka ile Görsel Tanıma

Bu proje, meyve görsellerini tanıyabilen yapay zeka destekli bir sınıflandırma sistemidir. 
Kullanıcı, Streamlit arayüzü üzerinden bir meyve görseli yükler. Model bu görseli analiz ederek ne olduğunu tahmin eder ve sonucu kullanıcıya gösterir.
- **İbrahim Halil Sertkaya - 200303045**


---

## 📌 Proje Bilgileri

- **Proje Adı:** Yapay Zeka Destekli Görsel Sınıflandırıcı
- **Model:** MobilNetV2 (TensorFlow Hub üzerinden önceden eğitilmiş)
- **Kapsam:** Görselden meyve türü tahmini
- **Platform:** Python (Streamlit arayüzü ile)

---

## 🧠 Kullanılan Teknolojiler

| Teknoloji        | Açıklama                                      |
|------------------|-----------------------------------------------|
| `TensorFlow`     | Görüntü işleme ve model çalıştırma            |
| `TensorFlow Hub` | Hazır eğitilmiş model (mobilnet_v2)           |
| `Streamlit`      | Web tabanlı kullanıcı arayüzü                 |
| `Pillow`         | Görsel yükleme ve işleme                      |
| `HuggingFace Hub`| Alternatif model araştırmaları                |
| `Python`         | Backend dil                                   |

---

## 🚀 Kurulum Talimatları

### 1. Python Ortamının Hazırlanması
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Gerekli Paketlerin Kurulması
```bash
pip install -r requirements.txt
```

### 3. Uygulamanın Başlatılması
```bash
streamlit run app.py
```

---

## 🎯 Uygulama Özellikleri

- ✅ Görsel yükleyerek sınıflandırma
- ✅ Kullanıcı dostu ve sade arayüz
- ✅ Anında tahmin sonucu
- ✅ README dosyasını uygulama içinde görme
- ✅ Model eğitimi gerekmeden hazır modeli kullanır

---

## 📷 Örnek Kullanım

1. Uygulama açılır
2. Görsel yüklenir: ![örnek](https://storage.googleapis.com/download.tensorflow.org/example_images/banana.jpg)
3. Model sonucu verir: `Banana`

---

## 📝 Notlar

- Kullanılan model `mobilenet_v2`, ImageNet sınıflarında eğitildiği için sadece yaygın meyveleri tanıyabilir.
- Eğer görsel veri setin dışında ise tahminler hatalı olabilir.
- Daha doğru sonuçlar için Fruits-360 gibi özelleşmiş veri setleri ile eğitilmiş modeller tercih edilebilir.

---
