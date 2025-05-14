# 🍍 Meyve Sınıflandırıcı - MobilNetV2

Bu uygulama, kullanıcıdan aldığı meyve görselini analiz ederek ne olduğunu tahmin eder. Model olarak TensorFlow Hub üzerinden hazır eğitilmiş **MobilNetV2** kullanılmıştır.

## 👨‍💻 Geliştirici
**İbrahim Halil Sertkaya - Öğr No: 200303045**

## 🧠 Kullanılan Teknolojiler
- TensorFlow
- TensorFlow Hub
- Streamlit
- PIL

## 🚀 Nasıl Çalıştırılır?
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📷 Kullanım
1. Streamlit arayüzünden bir meyve fotoğrafı yükleyin.
2. Model görseli sınıflandıracak ve sonucu gösterecektir.

## 📎 Notlar
- Model, ImageNet sınıflarına göre eğitildiği için en yaygın meyveleri doğru sınıflandırır.
