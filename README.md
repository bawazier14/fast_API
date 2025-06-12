# FastAPI Book Management API (with MySQL & SQLAlchemy)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![fastapi](https://img.shields.io/badge/Framework-FastAPI-05998b.svg)](https://fastapi.tiangolo.com/) [![license](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ini adalah sebuah proyek API RESTful untuk manajemen buku. Proyek ini mendemonstrasikan implementasi yang kuat dan terstruktur dengan menggunakan database MySQL, SQLAlchemy untuk ORM asinkron, dan Pydantic untuk validasi data.

## Fitur Utama
-   **Operasi CRUD Lengkap**: Menyediakan endpoint untuk menambah, membaca, memperbarui, dan menghapus buku.
-   **Asinkron Penuh**: Semua operasi database bersifat asinkron untuk performa tinggi , menggunakan `async/await` dengan `AsyncSession` dari SQLAlchemy.
-   **Dokumentasi API Otomatis**: Dokumentasi interaktif (Swagger UI) dibuat secara otomatis oleh FastAPI dan tersedia di endpoint `/docs`.
-   **Validasi Data**: Menggunakan skema Pydantic untuk validasi permintaan (*request*) dan serialisasi respons (*response*) yang ketat.
-   **Migrasi Tabel Otomatis**: Tabel database (`books`) dibuat secara otomatis saat aplikasi dimulai berdasarkan model SQLAlchemy.

## Tech Stack   
Proyek ini menggunakan beberapa proyek *open source* untuk dapat bekerja dengan baik:
-   `[FastAPI]` - *Framework* web modern berkinerja tinggi untuk membangun API dengan Python.
-   `[Uvicorn]` - Server ASGI secepat kilat untuk menjalankan aplikasi.
-   `[SQLAlchemy]` - *SQL Toolkit* dan ORM untuk Python, digunakan dalam mode asinkron.
-   `[Pydantic]` - Validasi data dan manajemen pengaturan menggunakan *type hints* Python.
-   `[aiomysql]` - *Driver* asinkron untuk mengakses *database* MySQL.
-   `[python-dotenv]` - Membaca *key-value pair* dari file `.env` dan mengaturnya sebagai *environment variable*.

## Instalasi
Proyek ini membutuhkan Python 3.8+ dan server MySQL yang sedang berjalan.

**1. Clone Repositori**
```sh
git clone [https://github.com/nama-anda/nama-repo-ini.git](https://github.com/nama-anda/nama-repo-ini.git)
cd nama-repo-ini

ATAU DOWNLOAD FILE ZIP

```
**2. Buat dan Aktifkan Virtual Environment**
# Untuk Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```
# Untuk macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
## Install Dependensi
Pastikan virtual environment Anda aktif, lalu jalankan perintah berikut untuk menginstal semua paket yang diperlukan dari file ``requirements.txt``
```bash
pip install -r requirements.txt
```
## Konfigurasi Environment Variable
Aplikasi ini memuat URL database dari *environment variable.* Buat file bernama ``.env`` di direktori root proyek. Salin konten berikut ke dalamnya dan sesuaikan dengan konfigurasi MySQL Anda.

```bash
# Format: mysql+aiomysql://<user>:<password>@<host>:<port>/<database_name>
DATABASE_URL="mysql+aiomysql://root:password_anda@localhost:3306/db_buku"
```

## Jalankan Aplikasi
Gunakan Uvicorn untuk menjalankan server FastAPI
```bash
uvicorn main:app --reload
```
Server akan berjalan di http://localhost:8000. Buka http://localhost:8000/docs di browser Anda untuk mengakses dokumentasi API interaktif.

# Ringkasan Endpoint API
 | Metode | Path | Deskripsi |
| ------ | ------ | ------- |
| `GET` |	`/books/`	| Memanggil Semua Buku |
| `GET` |	`/books/{book_id}` | Panggil Buku Berdsarkan ID |
| `POST` | `/books/`	| Tambah Buku Baru |
| `PUT` | `/books/{book_id}` | Update Buku yang Sudah Ada |
| `DELETE` | `/books/{book_id}` | Hapus Buku |
