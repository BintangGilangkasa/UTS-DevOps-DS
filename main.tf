terraform{
    required_providers {
        docker = {
            source = "kreuzwerker/docker"
            version = "~> 3.0.0"
        }
    }
}

provider "docker" {}

# Mengunduh image Ubuntu terbaru
resource "docker_image" "ubuntu" {
  name         = "ubuntu:latest"
  keep_locally = false
}

# Menciptakan wadah komputer kosong sesuai instruksi
resource "docker_container" "server_uas_analitik" {
  image = docker_image.ubuntu.image_id
  name  = "server_uas_analitik"
  
  # Menjaga kontainer tetap menyala agar bisa diakses oleh Ansible
  tty   = true
  stdin_open = true
}