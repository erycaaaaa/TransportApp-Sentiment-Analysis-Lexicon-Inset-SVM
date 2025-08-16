# 🚆 TransportApp Sentiment Analysis (Lexicon InSet + SVM) 🤖
<p align="center">
  <img src="/assets/anime-little-monster.gif" alt="sumber pinterest anime little monster by https://pin.it/6JKHEsDeO " width="720"/>
</p>

![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)
![Framework](https://img.shields.io/badge/Flask-Framework-green?logo=flask)
![License](https://img.shields.io/badge/license-MIT-orange)
![Stars](https://img.shields.io/github/stars/erycaaaaa/TransportApp-Sentiment-Analysis-Lexicon-Inset-SVM?style=social)

<div align="center">

Proyek ini menganalisis **ulasan aplikasi transportasi Indonesia** dari Google Play Store  
(**MitraDarat, Access by KAI, MyMRTJ**) menggunakan **leksikon InSet** untuk labeling sentimen  
dan **Support Vector Machine (SVM)** untuk klasifikasi 🔎📊.  

</div>

---

## 📑 Daftar Isi

<details>
  <summary>Daftar</summary>

- [🎯 Tujuan Proyek](#-tujuan-proyek)
- [🗺️ Alur Penelitian](#️-alur-penelitian)
- [🔧 Pre-processing & TF-IDF](#-pre-processing--tf-idf)
- [📊 Distribusi Sentimen](#-distribusi-sentimen-label-inset)
- [🤖 Evaluasi Model SVM](#-evaluasi-model-svm)
- [✅ Kesimpulan](#-kesimpulan)
- [🛠️ Cara Menjalankan](#️-cara-menjalankan-proyek)
- [📂 Struktur Direktori](#-struktur-direktori)
- [👩‍💻 Penulis](#-penulis)

</details>

---

## 🎯 Tujuan Proyek
✨ Menganalisis ulasan pengguna untuk:

- [x] 🔍 Identifikasi keluhan & pujian  
- [x] ⚖️ Perbandingan sentimen antar aplikasi  
- [x] 🏷️ Pengelompokan polaritas (positif/negatif)  

---

## 🗺️ Alur Penelitian

<p align="center">
  <img src="/assets/flowcart.jpg" alt="Flowchart Alur Penelitian" width="800"/>
</p>

> 🔄 **Pipeline:** Data → Preprocessing → Labeling → TF-IDF → SVM → Evaluasi  

---

## 🔧 Pre-processing & TF-IDF

<p align="center">
  <img src="/assets/tf.jpg" alt="Preprocessing & TF-IDF" width="800"/>
</p>

- ✂️ Cleaning, stopword removal, stemming  
- 🧾 TF-IDF untuk bobot kata penting  

---

## 📊 Distribusi Sentimen (Label InSet)

<p align="center">
  <img src="/assets/neg.jpg" alt="Distribusi Positif Negatif" width="800"/>
</p>

<div align="center">

| Aplikasi        | Positif (Jumlah) | Negatif (Jumlah) |
|:---------------:|:----------------:|:----------------:|
| 🚄 Access by KAI | 🟩 **446**        | 🟥 292            |
| 🚇 MyMRTJ        | 🟩 **286**        | 🟥 182            |
| 🚌 MitraDarat    | 🟩 **322**        | 🟥 153            |

</div>

> ✅ **Access by KAI** → dominasi positif  
> ⚠️ **MitraDarat** → banyak keluhan soal stabilitas  

---

## 🤖 Evaluasi Model SVM

<p align="center">
  <img src="/assets/svm-pos.jpg" alt="Evaluasi SVM" width="800"/>
</p>

<div align="center">

| Aplikasi        | Accuracy | Precision | Recall |
|:---------------:|:--------:|:---------:|:------:|
| 🚄 Access by KAI | 84%      | 85%       | 90%    |
| 🚇 MyMRTJ        | 87%      | 91%       | 88%    |
| 🚌 MitraDarat    | 82%      | 79%       | **97%** |

</div>

📌 **Recall** MitraDarat tinggi → sensitif mendeteksi positif, tapi precision rendah  
📌 **MyMRTJ** terbaik dalam presisi → prediksi positif lebih akurat  

---

## ✅ Kesimpulan
- **Access by KAI** → Mayoritas ulasan positif → benchmark terbaik  
- **MyMRTJ** → Seimbang, UX masih bisa ditingkatkan  
- **MitraDarat** → Perlu perbaikan stabilitas teknis  
- **InSet + SVM** → Efektif (>80% akurasi) untuk analisis sentimen bahasa Indonesia  

---

## 🛠️ Cara Menjalankan Proyek

### 🔹 1. Clone Repo
```bash
- . Tahap Instalansi (Clone Repository)
    - git clone https://github.com/erycaaaaa/TransportApp-Sentiment-Analysis-Lexicon-Inset-SVM.git 
    - cd TransportApp-Sentiment-Analysis-Lexicon-Inset-SVM

- .Install semua dependensi
    - pip install -r requirements.txt

- . menjalaskan aplikasi 
 -     pip install flask 
 -     set FLASK_APP=main.py
 -     set FLASK_ENV=development
 -     flask run
 -     flask --app main run
`

### 2) Buat & Aktifkan Virtual Environment

**venv (disarankan)**

```bash
# macOS/Linux
python3 -m venv .venv && source .venv/bin/activate
# Windows PowerShell
python -m venv .venv; .venv\Scripts\Activate.ps1
```

**conda (opsional)**

```bash
conda create -n transport-sentiment python=3.10 -y
conda activate transport-sentiment
```

### 3) Instal Dependensi

```bash
python -m pip install -U pip setuptools wheel
pip install -r requirements.txt
```


### 3) Menjalankan Aplikasi Flask

> Tentukan `FLASK_APP` sesuai struktur: `main` (root) **atau** `app.main` (dalam folder `app/`).

**Windows – PowerShell**

```powershell
pip install flask
$env:FLASK_APP="app.main"     # ganti ke "main" jika file di root
$env:FLASK_ENV="development"
flask run --debug
```

**Windows – CMD**

```cmd
pip install flask
set FLASK_APP=app.main
set FLASK_ENV=development
flask run
```

**macOS/Linux**

```bash
pip install flask
export FLASK_APP=app.main
export FLASK_ENV=development
flask run --debug
```

## 📂 Struktur Direktori (disarankan)

```
├─ app/                 # Flask app (entry: app/main.py)
├─ data/                # raw / interim / processed
├─ models/              # artefak model (vectorizer, SVM, dll.)
├─ src/                 # scripts: scrape, preprocess, build_features, train, evaluate
├─ assets/              # gambar hasil dan buku panduan
│   ├─ flowcart.jpg
│   ├─ tf.jpg
│   ├─ neg.jpg
│   └─ svm-pos.jpg
├─ requirements.txt
└─ README.md
```

---

## 🎥 4 Buku Panduan 


<p align="center">
  <a href="assets/Buku Panduan Penggunaan.pdf" target="_blank">📄 Lihat Buku Panduan Penggunaan</a>
</p>


---

## 🧰 Troubleshooting Cepat

* **`flask: command not found` / `'flask' is not recognized`** → Aktifkan venv & `pip install flask`.
* **`Error: Could not import "app.main"`** → Cek struktur & nilai `FLASK_APP` (gunakan `main` jika file di root).
* **Port 5000 sudah dipakai** → `flask run --port 8001` atau hentikan proses lain.
* **PowerShell policy error** → Jalankan sebagai Admin: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
* **Hot reload tidak jalan** → Pastikan `FLASK_ENV=development` atau tambahkan `--debug`.

---


