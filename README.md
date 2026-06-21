# 🚀 Infrastructure as Code & Automated Data Analysis with Terraform, Ansible, and Docker

## 📖 Deskripsi Proyek

Proyek ini merupakan implementasi konsep **Infrastructure as Code (IaC)** dan **Configuration Management** menggunakan **Terraform**, **Ansible**, dan **Docker** untuk membangun lingkungan Data Science secara otomatis.

Sistem akan:

* Membuat container Ubuntu menggunakan Terraform.
* Mengonfigurasi environment menggunakan Ansible.
* Menginstal Python dan seluruh dependency yang dibutuhkan.
* Menyalin dataset dan program Python ke dalam container.
* Menjalankan analisis data secara otomatis menggunakan Python dan Pandas.

Proyek ini dibuat sebagai pemenuhan tugas mata kuliah **DevOps & MLOps**.

---

# 🏗️ Arsitektur Sistem

```text
┌─────────────┐
│ Terraform   │
└──────┬──────┘
       │
       ▼
┌──────────────────────┐
│ Docker Container     │
│ server_uas_analitik  │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ Ansible Automation   │
│ Install Python       │
│ Install Dependencies │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ Python Application   │
│ uts.py               │
│ hasil_nilai.csv      │
└──────────────────────┘
```

---

# 📂 Struktur Proyek

```text
UTS/
│
├── terraform/
│   └── main.tf
│
├── ansible/
│   ├── inventory.ini
│   └── playbook.yml
│
├── app/
│   ├── uts.py
│   ├── requirements.txt
│   └── hasil_nilai.csv
│
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

# 🛠️ Teknologi yang Digunakan

| Teknologi | Fungsi                   |
| --------- | ------------------------ |
| Terraform | Infrastructure as Code   |
| Docker    | Containerization         |
| Ansible   | Configuration Management |
| Python    | Analisis Data            |
| Pandas    | Pengolahan Dataset       |

---

# ⚙️ Prasyarat

Pastikan software berikut telah terinstal:

### Docker Desktop

Verifikasi:

```bash
docker --version
```

Pastikan Docker Desktop menunjukkan status:

```text
Engine Running
```

---

### Terraform

Verifikasi:

```bash
terraform version
```

---

# 🚀 Cara Menjalankan Proyek

## 1️⃣ Clone Repository

```bash
git clone <repository-url>
cd UTS
```

---

## 2️⃣ Membuat Infrastruktur dengan Terraform

Masuk ke folder Terraform:

```bash
cd terraform
```

Inisialisasi Terraform:

```bash
terraform init
```

Buat container Ubuntu:

```bash
terraform apply -auto-approve
```

Jika berhasil akan muncul:

```text
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

Verifikasi container:

```bash
docker ps
```

Output:

```text
server_uas_analitik
```

---

## 3️⃣ Konfigurasi Environment Menggunakan Ansible

Kembali ke root project:

```bash
cd ..
```

Jalankan Ansible:

```powershell
docker run --rm -it `
-v /var/run/docker.sock:/var/run/docker.sock `
-v "${PWD}:/ansible" `
-w /ansible `
--entrypoint sh alpine/ansible `
-c "apk add --no-cache docker-cli && ansible-playbook -i ansible/inventory.ini ansible/playbook.yml"
```

Jika berhasil:

```text
PLAY RECAP

server_uas_analitik :
ok=2
changed=2
failed=0
```

---

## 4️⃣ Salin Program dan Dataset ke Container

```powershell
docker cp app/uts.py server_uas_analitik:/uts.py
docker cp app/hasil_nilai.csv server_uas_analitik:/hasil_nilai.csv
```

Verifikasi:

```powershell
docker exec -it server_uas_analitik ls /
```

Output:

```text
hasil_nilai.csv
uts.py
```

---

## 5️⃣ Menjalankan Program Analisis Data

```powershell
docker exec -it server_uas_analitik python3 /uts.py
```

Contoh output:

```text
---Nilai Mahasiswa---

Rata-rata nilai: 88.5
Nilai Terendah: 78
Nilai Tertinggi: 100

Hasil nilai telah disimpan ke file hasil_nilai.csv

Selesai
```

---

# 🧹 Cleanup Infrastruktur

Masuk ke folder Terraform:

```bash
cd terraform
```

Hapus seluruh resource:

```bash
terraform destroy -auto-approve
```

Verifikasi:

```bash
docker ps -a
```

Container:

```text
server_uas_analitik
```

sudah tidak ada.

---

# 🔍 Troubleshooting

## Container Sudah Ada

Error:

```text
The container name "/server_uas_analitik" is already in use
```

Solusi:

```bash
docker rm -f server_uas_analitik
```

Kemudian jalankan kembali:

```bash
terraform apply -auto-approve
```

---

## Terraform Tidak Menemukan main.tf

Pastikan berada pada folder:

```bash
cd terraform
```

Lalu jalankan:

```bash
terraform init
```

---

## Docker Tidak Berjalan

Cek:

```bash
docker ps
```

Jika muncul:

```text
Cannot connect to the Docker daemon
```

Pastikan Docker Desktop sudah aktif.

---

# 📷 Dokumentasi Project

PLAY RECAP:

![Dokumentasi PLAY RECAP](doc/running ansible.png)

Terr

# 🎯 Tujuan Pembelajaran

Melalui proyek ini mahasiswa mampu:

* Mengimplementasikan Infrastructure as Code (IaC).
* Menggunakan Terraform untuk provisioning infrastruktur.
* Menggunakan Ansible untuk otomatisasi konfigurasi.
* Mengelola container Docker.
* Menjalankan aplikasi Data Science dalam lingkungan terisolasi.
* Mengintegrasikan konsep DevOps dan MLOps dalam satu alur kerja.

---

# 👨‍💻 Author

**Bintang Gilangkasa Syailendra**

Program Studi Sains Data

Universitas Islam Negeri Salatiga

Mata Kuliah DevOps for Data Science