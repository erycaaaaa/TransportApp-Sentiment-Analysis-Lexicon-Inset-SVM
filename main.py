import pandas as pd
from flask import Flask, render_template, request
import sqlite3
import math
import re
from markupsafe import Markup

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    search_query = request.args.get('search', default="", type=str)
    page = request.args.get('page', default=1, type=int)
    per_page = 10
    offset = (page - 1) * per_page

    conn = sqlite3.connect('DatabaseKAI.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM komentar WHERE komentar LIKE ?", ('%' + search_query + '%',))
    total_rows = cursor.fetchone()[0]
    total_pages = math.ceil(total_rows / per_page)

    cursor.execute("SELECT * FROM komentar WHERE komentar LIKE ? LIMIT ? OFFSET ?", ('%' + search_query + '%', per_page, offset))
    rows = cursor.fetchall()

    # Buat highlight kata yang dicari
    highlighted_rows = []
    for row in rows:
        komentar = row["komentar"]
        if search_query:
            # Escape HTML chars and apply highlight
            pattern = re.compile(re.escape(search_query), re.IGNORECASE)
            komentar = pattern.sub(lambda m: f"<mark>{m.group(0)}</mark>", komentar)
        highlighted_rows.append({
            "komentar": Markup(komentar),
            "sentimen": row["sentimen"]
        })

    # Baca akurasi dari file
    with open('./static/akurasi.txt', 'r') as f:
        akurasi_nilai = float(f.read())

    # Hitung jumlah sentimen
    cursor.execute("SELECT COUNT(*) FROM komentar WHERE sentimen='Positif'")
    positif_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM komentar WHERE sentimen='Negatif'")
    negatif_count = cursor.fetchone()[0]

    total_count = positif_count + negatif_count

    # Hitung persentase
    positif_percent = (positif_count / total_count) * 100 if total_count > 0 else 0
    negatif_percent = (negatif_count / total_count) * 100 if total_count > 0 else 0

    conn.close()
    
    return render_template('index.html', 
                           tabel=highlighted_rows, 
                           current_page=page, 
                           total_pages=total_pages, 
                           search_query=search_query,
                           akurasi=round(akurasi_nilai, 2),
                           positif_percent=round(positif_percent, 2),
                           negatif_percent=round(negatif_percent, 2)
                           )

# Route untuk halaman visualisasi
@app.route('/visualisasi/kai')
def visualisasi_kai():
    # Buka koneksi ke SQLite
    conn = sqlite3.connect("DatabaseKAI.db")
    df = pd.read_sql_query("SELECT sentimen FROM komentar", conn)
    conn.close()

    # Hitung jumlah masing-masing sentimen
    sentimen_count = df["sentimen"].value_counts().to_dict()

    # Kirim ke template
    return render_template("visualisasi_kai.html", sentimen=sentimen_count)


# Route untuk halaman visualisasi MRTJ
@app.route('/visualisasi/mrtj')
def visualisasi_MRTJ():
    # Buka koneksi ke SQLite
    conn = sqlite3.connect("DatabaseMRT.db")
    df = pd.read_sql_query("SELECT sentimen FROM komentar", conn)
    conn.close()

    # Hitung jumlah masing-masing sentimen
    sentimen_count = df["sentimen"].value_counts().to_dict()

    # Kirim ke template
    return render_template("visualisasi_MRTJ.html", sentimen=sentimen_count)

# Route untuk halaman visualisasi Mitra Darat
@app.route('/visualisasi/mitraDarat')
def visualisasi_mitraDarat():
    # Buka koneksi ke SQLite
    conn = sqlite3.connect("DatabaseMitraDarat.db")
    df = pd.read_sql_query("SELECT sentimen FROM komentar", conn)
    conn.close()

    # Hitung jumlah masing-masing sentimen
    sentimen_count = df["sentimen"].value_counts().to_dict()

    # Kirim ke template
    return render_template("visualisasi_mitraDarat.html", sentimen=sentimen_count)


if __name__ == '__main__':
    app.run(debug=True)