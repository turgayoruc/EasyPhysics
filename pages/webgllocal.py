import os
import threading
from flask import Flask, send_from_directory
from flask_cors import CORS  # CORS sorunları için
import streamlit as st
from waitress import serve
# Flask sunucusu oluşturma
app = Flask(__name__)
CORS(app)  # CORS sorunlarını önlemek için

# WebGL dosyalarının bulunduğu dizin (projenize göre ayarlayın)
WEBGL_DIR = "../Game"

# Ana sayfa için index.html dosyasını sunma
@app.route('/')
def serve_index():
    return send_from_directory(WEBGL_DIR, 'index.html')

# Diğer dosyalar için (CSS, JS, WebGL assetleri)
@app.route('/<path:path>')
def serve_build(path):
    return send_from_directory(WEBGL_DIR, path)

# Flask sunucusunu çalıştırma fonksiyonu
def run_flask():
    serve(app, host='0.0.0.0', port=5100)
   # port = int(os.environ.get('PORT', 5000))  # Portu ayarla (Varsayılan: 5000)
   # app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)


# Flask sunucusunu ayrı bir thread'de çalıştır
threading.Thread(target=run_flask).start()

# Streamlit içinde WebGL uygulamasını iframe ile gösterme
st.title("Yerel WebGL Uygulaması")
st.markdown(f"""
    <iframe src="http://localhost:5100" width="100%" height="600px" frameborder="0"></iframe>
    """, unsafe_allow_html=True)