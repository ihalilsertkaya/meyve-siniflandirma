import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image
import requests

# ImageNet etiketleri
labels_url = "https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt"
labels = requests.get(labels_url).text.strip().split("\n")

# Giriş şekli
input_shape = (224, 224, 3)

# Model tanımı
mobilenet_layer = hub.KerasLayer(
    "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4",
    input_shape=input_shape
)


def load_model():
    return mobilenet_layer

model = load_model()

# Gorsel yeniden boyutlama ve model icin duzenleme
def preprocess_image(img: Image.Image) -> np.ndarray:
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array.astype(np.float32)

# Tahmin fonksiyonu
def predict(img: Image.Image) -> str:
    processed = preprocess_image(img)
    preds = model(processed).numpy()
    top_pred = np.argmax(preds[0])
    return labels[top_pred]
