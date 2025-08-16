# 🚆 TransportApp Sentiment Analysis (Lexicon InSet + SVM) 🤖

![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)
![Framework](https://img.shields.io/badge/Flask-Framework-green?logo=flask)
![License](https://img.shields.io/badge/license-MIT-orange)
![Stars](https://img.shields.io/github/stars/erycaaaaa/TransportApp-Sentiment-Analysis-Lexicon-Inset-SVM?style=social)

Proyek ini menganalisis **ulasan aplikasi transportasi Indonesia** dari Google Play Store  
(**MitraDarat, Access by KAI, MyMRTJ**) menggunakan **leksikon InSet** untuk labeling sentimen  
dan **Support Vector Machine (SVM)** untuk klasifikasi 🔎📊.  

---

## 📑 Daftar Isi
- [🎯 Tujuan Proyek](#-tujuan-proyek)
- [🗺️ Alur Penelitian](#️-alur-penelitian)
- [🔧 Pre-processing & TF-IDF](#-pre-processing--tf-idf)
- [📊 Distribusi Sentimen](#-distribusi-sentimen-label-inset)
- [🤖 Evaluasi Model SVM](#-evaluasi-model-svm)
- [✅ Kesimpulan](#-kesimpulan)
- [🛠️ Cara Menjalankan](#️-cara-menjalankan-proyek)
- [📂 Struktur Direktori](#-struktur-direktori)
- [👩‍💻 Penulis](#-penulis)

---

## 🎯 Tujuan Proyek
✨ Menganalisis ulasan pengguna untuk:
- 🔍 Mengidentifikasi **keluhan** dan **pujian**
- ⚖️ Membandingkan **sentimen antar aplikasi transportasi**
- 🏷️ Mengelompokkan ulasan (positif / negatif)

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

| Aplikasi       | Positif | Negatif |
|----------------|---------|---------|
| 🚄 Access by KAI | **446** | 292 |
| 🚇 MyMRTJ        | **286** | 182 |
| 🚌 MitraDarat    | **322** | 153 |

> ✅ **Access by KAI** → dominasi positif  
> ⚠️ **MitraDarat** → banyak keluhan soal stabilitas  

---

## 🤖 Evaluasi Model SVM

<p align="center">
  <img src="/assets/svm-pos.jpg" alt="Evaluasi SVM" width="800"/>
</p>

| Aplikasi       | Accuracy | Precision | Recall |
|----------------|----------|-----------|--------|
| 🚄 Access by KAI | 84%      | 85%       | 90%    |
| 🚇 MyMRTJ        | 87%      | 91%       | 88%    |
| 🚌 MitraDarat    | 82%      | 79%       | **97%** |

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
git clone https://github.com/erycaaaaa/TransportApp-Sentiment-Analysis-Lexicon-Inset-SVM.git
cd TransportApp-Sentiment-Analysis-Lexicon-Inset-SVM
