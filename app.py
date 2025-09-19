from flask import Flask, render_template, request, redirect
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

# Lokasi file penyimpanan
GUESTBOOK_FILE = os.path.join(BASE_DIR, "guestbook.txt")

# Fungsi baca data tamu dari file
def load_entries():
    entries = []
    if os.path.exists(GUESTBOOK_FILE):
        with open(GUESTBOOK_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(" | ")
                if len(parts) == 6:  # Waktu + 5 kolom
                    entries.append({
                        "waktu": parts[0],
                        "nama": parts[1].replace("Nama: ", ""),
                        "kontak": parts[2].replace("Kontak: ", ""),
                        "institusi": parts[3].replace("Institusi: ", ""),
                        "tujuan": parts[4].replace("Tujuan: ", ""),
                        "catatan": parts[5].replace("Catatan: ", "")
                    })
    return entries

# Route utama
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form.get("nama")
        kontak = request.form.get("kontak")
        institusi = request.form.get("institusi")
        tujuan = request.form.get("tujuan")
        catatan = request.form.get("catatan") or "-"

        waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        entry = f"{waktu} | Nama: {nama} | Kontak: {kontak} | Institusi: {institusi} | Tujuan: {tujuan} | Catatan: {catatan}"

        # Simpan ke file
        with open(GUESTBOOK_FILE, "a", encoding="utf-8") as f:
            f.write(entry + "\n")

        return redirect("/")

    entries = load_entries()
    # Urutkan terbaru paling atas
    entries.reverse()
    return render_template("index.html", entries=entries)

# Route untuk clear daftar tamu
@app.route("/clear", methods=["POST"])
def clear():
    open(GUESTBOOK_FILE, "w", encoding="utf-8").close()
    return redirect("/")
    
