import streamlit as st
import threading
import app  # import Flask app dari app.py

# Jalankan Flask di thread terpisah
def run_flask():
    app.app.run(host="0.0.0.0", port=5000)

threading.Thread(target=run_flask, daemon=True).start()

st.title("Buku Tamu Online via Streamlit")
st.write("Di bawah ini adalah versi online dari Buku Tamu:")

st.components.v1.iframe("http://localhost:5050", height=600)
