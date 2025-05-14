import streamlit as st
from PIL import Image
from predict import predict

st.set_page_config(page_title="🍎 Meyve Sınıflandırıcı", layout="centered")

st.markdown("<h1 style='text-align: center;'>🍍 Meyve Tanıma Sistemi</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>İbrahim Halil Sertkaya</h3>", unsafe_allow_html=True)
st.write("---")

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme_content = readme_file.read()

with st.expander("📄 README Bilgilerini Göster"):
    st.markdown(readme_content)

st.write("---")

uploaded = st.file_uploader("📤 Lütfen bir meyve görseli yükleyin:", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Yüklenen Görsel", use_container_width=True)
    st.write("🔍 Tahmin ediliyor...")
    label = predict(img)
    st.success(f"✅ Bu meyve: **{label}**")
