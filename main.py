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

    conn.close()

    return render_template('index.html', 
                           tabel=highlighted_rows, 
                           current_page=page, 
                           total_pages=total_pages, 
                           search_query=search_query)


if __name__ == '__main__':
    app.run(debug=True)
