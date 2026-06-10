# Esteler App — Dapur Hijrah

Aplikasi web pemesanan makanan untuk Dapur Hijrah. Pelanggan dapat menelusuri menu, membuat preorder, dan melacak status pesanan tanpa perlu login. Admin dapat mengelola menu, memproses pesanan, dan memantau performa bisnis melalui dashboard analitik.

---

## Tech Stack

| Layer              | Teknologi                          |
| ------------------ | ---------------------------------- |
| **Backend**        | Python · Flask 3.0                 |
| **ORM**            | Flask-SQLAlchemy · Flask-Migrate   |
| **Database**       | PostgreSQL (Neon Serverless)       |
| **Auth**           | Flask-Login · Werkzeug             |
| **Frontend**       | Jinja2 · HTML/CSS/JavaScript       |
| **Deployment**     | Vercel (Python Serverless Runtime) |
| **Env Management** | python-dotenv                      |

---

## Fitur

### Pelanggan

- Telusuri menu berdasarkan kategori dan pencarian
- Rekomendasi menu berbasis aturan (best seller, favorit, rating)
- Kelola keranjang belanja berbasis sesi
- Buat preorder online dengan jadwal pengambilan
- Pilih metode pembayaran: QRIS, Tunai, COD
- Lacak status pesanan secara real-time via kode order

### Admin

- **Dashboard** — ringkasan pendapatan harian, tren mingguan, top menu, pesanan aktif
- **Manajemen Menu** — tambah/edit/hapus menu, atur status aktif, tandai best seller & favorit
- **Manajemen Pesanan** — ubah status pesanan (menunggu → memasak → siap → selesai), batalkan pesanan
- **Walk-in Order** — buat pesanan langsung untuk pelanggan offline
- **Analitik** — distribusi sumber pesanan (online vs walk-in), jam sibuk, tren pendapatan

---

## Instalasi

### Prasyarat

- Python 3.10+
- PostgreSQL database (disarankan: [Neon](https://neon.tech) untuk gratis serverless)

### Langkah

**1. Clone repository**

```bash
git clone <url-repository>
cd esteler-app
```

**2. Buat virtual environment**

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

**3. Install dependensi**

```bash
pip install -r requirements.txt
```

**4. Konfigurasi environment**

```bash
cp .env.example .env
```

Edit file `.env` dan isi variabel berikut:

```env
DATABASE_URL=postgresql://user:password@host-pooler.region.aws.neon.tech/dapur_hijrah?sslmode=require
SECRET_KEY=random-string-yang-panjang-dan-aman
FLASK_ENV=development
```

> Untuk generate `SECRET_KEY`:
>
> ```bash
> python -c "import secrets; print(secrets.token_hex(32))"
> ```

**5. Inisialisasi database**

```bash
flask db upgrade
python seed.py
```

**6. Jalankan aplikasi**

```bash
python app.py
```

Aplikasi berjalan di `http://localhost:5000`

---

## Struktur Proyek

```
esteler-app/
├── api/index.py          # Entry point Vercel & registrasi blueprint
├── routes/               # Definisi route (auth, admin, customer)
├── services/             # Business logic (menu, cart, order, analitik)
├── templates/            # Template HTML Jinja2
│   ├── auth/
│   ├── admin/
│   └── customer/
├── static/               # Aset statis (CSS, JS)
├── models.py             # Model database SQLAlchemy
├── config.py             # Konfigurasi Flask & database
├── app.py                # Entry point lokal
├── seed.py               # Seeder data awal
└── vercel.json           # Konfigurasi deployment Vercel
```

---

## Deployment ke Vercel

**1. Install Vercel CLI**

```bash
npm i -g vercel
```

**2. Set environment variables di Vercel dashboard**

Tambahkan `DATABASE_URL` dan `SECRET_KEY` di **Project Settings → Environment Variables**.

**3. Deploy**

```bash
vercel --prod
```
