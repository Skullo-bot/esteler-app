<!-- TABLE OF CONTENTS -->
<details>
  <summary>📚 Table of Contents</summary>
  <ol>
    <li>
      <a href="#-about-the-project">⭐ About The Project</a>
    </li>
    <li><a href="#-feature">📋 Feature</a></li>
    <li><a href="#-tech-stack">⚡ Tech Stack</a></li>
    <li>
      <a href="#-getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#setup-environtment">Setup Environment</a></li>
        <li><a href="#run-the-project">Run The Project</a></li>
      </ul>
    </li>
    <li><a href="#-team">Team</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## ⭐ About The Project

Es Teler App

## 📋 Feature

- [ ] 📅 Reservation
  - [ ] Advanced Doctor Search : Patients can filter doctors by Polyclinic, Day, and Time.
- [ ] 📝 Data Management for Admin
  - [ ] Doctor Management
- [ ] 🔐 Autentikasi & Akun (Auth)
  - [ ] Login & Logout : Akses masuk dan keluar sistem.
  - [ ] Registrasi Akun : Pendaftaran pengguna baru.
  - [ ] Lupa & Reset Password : Fitur pemulihan kata sandi (menggunakan token).

- [ ] 🛒 Fitur Pelanggan (Customer)
  - [ ] Katalog Menu : Menampilkan daftar menu es teler yang sedang aktif beserta detailnya (deskripsi, harga, gambar).
  - [ ] Pencarian Menu : Fitur untuk mencari menu spesifik berdasarkan kata kunci.
  - [ ] Rekomendasi Pintar : Menampilkan saran/rekomendasi menu berdasarkan match score atau best sellers.
  - [ ] Keranjang Belanja (Cart) : Fitur penampungan sementara untuk menambah, mengubah kuantitas, menghapus item, hingga mengosongkan keranjang (berbasis sesi).
  - [ ] Checkout / Pre-order : Mengubah isi keranjang menjadi pesanan resmi.
  - [ ] Lacak Pesanan : Pelanggan dapat melacak status pesanan mereka (menunggu, dimasak, selesai, dibatalkan) menggunakan kode pesanan (order code).

- [ ] ⚙️ Fitur Admin & Operasional
  - [ ] Dashboard Analitik : Menampilkan ringkasan metrik penting seperti total pendapatan, total pesanan, pelanggan baru, skor kepuasan, tren pendapatan mingguan, dan daftar menu terlaris.
  - [ ] Manajemen Menu (CRUD) : Fitur bagi admin untuk menambah menu baru, mengubah data menu, menghapus, serta menyalakan/mematikan status menu (toggle active).
  - [ ] Manajemen Pesanan : Melihat seluruh daftar pesanan masuk, lalu mengubah statusnya (memproses, menyelesaikan, atau membatalkan pesanan).
  - [ ] Cetak Struk / Resi : Fitur untuk men-generate dan mengunduh resi pesanan (receipt).
  - [ ] Ekspor Laporan : Mengunduh data laporan penjualan berdasarkan rentang waktu tertentu ke dalam format file PDF atau CSV.

## ⚡ Tech Stack

- [![Flask][Flask.py]][Flask-url]
- [![TailwindCSS][Tailwind]][Tailwind-url]

<!-- GETTING STARTED -->

## 🚀 Getting Started

Berikut ini adalah _prerequisites_ dan _installation_ jika ingin menjalankan proyek secara lokal.
Ikuti instruksi dibawah untuk mendapatkan _local copy_ dari proyek ini.

### Prerequisites

Before you begin, ensure you have met the following requirements:

1. Operating System
   Windows (Recommended for SQL Server compatibility), macOS, or Linux.

2. Software & Tools
   - Python 3.11.0: Make sure Python is installed and added to your system PATH.
   - Git: To clone the repository.

3. Knowledge
   - Basic understanding of how to use the Command Line or Terminal.

### Installation

1. Clone repository
   ```sh
   git clone https://github.com/yudhasw/Telkomedika-Online-Reservation.git
   ```
2. Buat Virtual Environment Python
   ```sh
   python -m venv .venv
   ```
   Aktifkan Environment
   ```sh
   .venv\Scripts\activate
   ```
3. Install Dependencies Python
   ```sh
   pip install -r requirements.txt
   ```
4. Install Dependencies NPM
   ```sh
   npm install
   ```

### Setup Environment

1. Make .env File
2. Copy this Code and fill it with your own data.
   ```sh
   SERVER_NAME=YourServerName
   DATABASE_NAME=YourDatabaseName
   DB_USERNAME=YourDatabaseUsername
   DB_PASSWORD=password_rahasia
   SECRET_KEY=random_secret_key
   MAIL_USERNAME=email@gmail.com
   MAIL_PASSWORD=app_password_google
   ```

### Run the Project

```sh
npm run dev
```

## 👨🏻‍💻 Team

- Devo Gassan Savero
- Arya Wijaya 103012330330
- Arif Rahmatiana 103012300446
- Syauqi Nurfikri Rahman 103012300299
- Dhafin Ghiffary 103012300348
- Yudha Setiawan Wicaksono 103012300480
- Muhammad Nazriel Ihram 103012300269

<br />
<a href="https://github.com/yudhasw/esteler-app/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yudhasw/esteler.app" alt="contrib.rocks image" />
</a>
