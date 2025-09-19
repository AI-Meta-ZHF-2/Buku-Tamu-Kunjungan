import os
import threading
import streamlit as st
from werkzeug.serving import make_server
from app import app  # pastikan app.py ada di folder yang sama

# Jalankan Flask di thread terpisah
class ServerThread(threading.Thread):
    def __init__(self, app):
        threading.Thread.__init__(self)
        self.server = make_server("127.0.0.1", 5050, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()

# Mulai server Flask
if "server" not in st.session_state:
    st.session_state.server = ServerThread(app)
    st.session_state.server.start()

st.title("📖 Buku Tamu Online via Streamlit")
st.markdown("Flask app berjalan di: [http://127.0.0.1:5050](http://127.0.0.1:5050)")
st.markdown("Klik link di atas untuk membuka aplikasi Buku Tamu.")
