# UTS DevOps for Sains Data

## Judul Proyek

Sistem Analisis Nilai Mahasiswa dengan Docker dan PostgreSQL

---

## Deskripsi Proyek

Proyek ini merupakan aplikasi Python sederhana yang digunakan untuk melakukan analisis data nilai mahasiswa. Program mengambil data nilai dari environment variable, kemudian menghitung:

- Rata-rata nilai
- Nilai terendah
- Nilai tertinggi

Hasil analisis akan ditampilkan di terminal, disimpan ke file CSV (`hasil_nilai.csv`), dan juga dimasukkan ke dalam database PostgreSQL menggunakan Docker Compose.

Proyek ini dibuat untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah DevOps for Sains Data.

---

## Arsitektur Sistem

Proyek ini menggunakan base image `python:3.9-slim` karena image ini ringan, cepat, dan cocok untuk menjalankan aplikasi Python sederhana tanpa library yang berat. Penggunaan image ringan membantu proses build menjadi lebih efisien dan hemat resource.

Sistem terdiri dari dua container utama:

### 1. app

Container ini menjalankan file Python `uts.py` yang berfungsi untuk memproses data nilai mahasiswa, menghitung statistik sederhana, menyimpan hasil ke file CSV, dan mengirim data ke database PostgreSQL.

### 2. db

Container ini menggunakan PostgreSQL sebagai database utama untuk menyimpan data nilai mahasiswa secara permanen.

Komunikasi antara container `app` dan `db` terjadi melalui network internal Docker Compose. Service `app` terhubung ke database menggunakan host `db`, yaitu nama service PostgreSQL pada file `docker-compose.yml`.

Penggunaan `depends_on` memastikan container aplikasi berjalan setelah container database dimulai, sedangkan `volumes` digunakan agar data PostgreSQL tidak hilang meskipun container dimatikan atau dihapus.

---

## Struktur Project

```text
UTS/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── uts.py
├── README.md
│
└── .github/
    └── workflows/
        └── main.yml
