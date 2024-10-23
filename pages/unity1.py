import streamlit as st
from flask import Flask, send_from_directory
import threading
import os

# Flask sunucusu oluşturma
app = Flask(__name__)

# WebGL dosyalarının bulunduğu dizin
WEBGL_DIR = "../Game"

@app.route('/')
def serve_index():
    return send_from_directory(WEBGL_DIR, 'index.html')

@app.route('/<path:path>')
def serve_build(path):
    return send_from_directory(WEBGL_DIR, path)

def run_flask():
    app.run(port=8500, debug=False, use_reloader=False)

# Flask sunucusunu ayrı bir threadde başlatıyoruz
threading.Thread(target=run_flask).start()

# Streamlit içinde WebGL'i görüntülemek için iframe kullanıyoruz
st.title("WebGL Uygulaması Streamlit İçinde")
st.markdown(f"""
    <iframe src="http://localhost:8500" width="100%" height="600px" frameborder="0"></iframe>
    """, unsafe_allow_html=True)

# Bu projede markdown kullandik. digerinde st.components.v1