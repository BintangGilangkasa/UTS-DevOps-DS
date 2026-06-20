# 🚀 UTS DevOps & MLOps

## Otomatisasi Infrastruktur dan Analisis Data Menggunakan Terraform, Ansible, Docker, dan Python

---

## 📖 Deskripsi Proyek

Proyek ini bertujuan untuk menerapkan konsep **Infrastructure as Code (IaC)** dan **Automation Configuration** dalam membangun lingkungan Data Science secara otomatis.

Teknologi yang digunakan:

* Terraform
* Docker
* Ansible
* Python
* Pandas

Sistem akan:

1. Membuat container Ubuntu menggunakan Terraform.
2. Mengonfigurasi environment menggunakan Ansible.
3. Menginstal Python dan library yang diperlukan.
4. Menyalin file program dan dataset ke dalam container.
5. Menjalankan program analisis data secara otomatis.

---

## 📂 Struktur Folder

```text
UTS/
│
├── main.tf
├── inventory.ini
├── playbook.yml
├── requirements.txt
├── uts.py
├── hasil_nilai.csv
└── README.md
```

---

# ⚙️ Prasyarat

Pastikan software berikut sudah terinstal:

### Docker Desktop

Cek:

```bash
docker --version
```

### Terraform

Cek:

```bash
terraform version
```

Pastikan Docker Desktop dalam keadaan:

```text
Engine Running
```

---

# 🚀 Langkah Menjalankan Proyek

## 1. Masuk ke Folder Proyek

Buka PowerShell kemudian masuk ke direktori proyek:

```powershell
cd D:\KULIAH\SEMESTER-6\devops-ml\UTS
```

---

## 2. Inisialisasi Terraform

Jalankan:

```bash
terraform init
```

Jika berhasil akan muncul:

```text
Terraform has been successfully initialized!
```

---

## 3. Membuat Infrastruktur

Jalankan:

```bash
terraform apply -auto-approve
```

Terraform akan membuat container:

```text
server_uas_analitik
```

---

## 4. Verifikasi Container Berjalan

```bash
docker ps
```

Pastikan terdapat container:

```text
server_uas_analitik
```

---

## 5. Konfigurasi Environment Menggunakan Ansible

Jalankan perintah berikut:

```powershell
docker run --rm -it `
-v /var/run/docker.sock:/var/run/docker.sock `
-v "${PWD}:/ansible" `
-w /ansible `
--entrypoint sh alpine/ansible `
-c "apk add --no-cache docker-cli && ansible-playbook -i inventory.ini playbook.yml"
```

Jika berhasil akan muncul:

```text
PLAY RECAP

server_uas_analitik :
ok=2
changed=2
failed=0
```

Keterangan:

* Python berhasil diinstal
* Pip berhasil diinstal
* Requirements berhasil diinstal
* Tidak ada error

---

## 6. Salin Program ke Dalam Container

```powershell
docker cp uts.py server_uas_analitik:/uts.py
docker cp hasil_nilai.csv server_uas_analitik:/hasil_nilai.csv
```

Jika berhasil:

```text
Successfully copied ...
```

---

## 7. Verifikasi File Berhasil Disalin

```powershell
docker exec -it server_uas_analitik ls /
```

Output:

```text
hasil_nilai.csv
uts.py
```

---

## 8. Menjalankan Program Analisis Data

```powershell
docker exec -it server_uas_analitik python3 /uts.py
```

Contoh output:

```text
---Nilai Mahasiswa---

Rata-rata nilai: 88.5
Nilai Terendah: 78
Nilai tertinggi: 100

Hasil nilai telah disimpan ke file hasil_nilai.csv

Selesai
```

Output tersebut menunjukkan bahwa:

✅ Dataset berhasil dibaca

✅ Analisis berhasil dilakukan

✅ Program berhasil dijalankan di dalam container

---

# 🧹 Menghapus Infrastruktur

Jika sudah selesai:

## Hapus Container

```bash
terraform destroy -auto-approve
```

---

## Hapus Image Ubuntu

```bash
docker rmi -f ubuntu:latest
```

---

# 🔍 Troubleshooting

## Docker Tidak Berjalan

Cek:

```bash
docker ps
```

Jika muncul:

```text
Cannot connect to Docker daemon
```

Pastikan Docker Desktop sudah aktif.

---

## Terraform Tidak Dikenali

Jika muncul:

```text
terraform is not recognized
```

Tambahkan Terraform ke Environment Variable PATH.

---

## Container Tidak Ditemukan

Cek:

```bash
docker ps -a
```

Jika container berhenti:

```bash
terraform apply -auto-approve
```

jalankan kembali.

---

# 👨‍💻 Penulis

**Bintang Gilangkasa Syailendra**

Program Studi Sains Data

Universitas Islam Negeri Salatiga

Mata Kuliah DevOps for Data Science

Semester 6