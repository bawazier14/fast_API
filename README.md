# FastAPI Book Management API (with MySQL & SQLAlchemy)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![fastapi](https://img.shields.io/badge/Framework-FastAPI-05998b.svg)](https://fastapi.tiangolo.com/) [![license](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ini adalah sebuah proyek API RESTful untuk manajemen buku. [cite_start]Proyek ini mendemonstrasikan implementasi yang kuat dan terstruktur dengan menggunakan database MySQL, SQLAlchemy untuk ORM asinkron, dan Pydantic untuk validasi data.

## Fitur Utama
-   **Operasi CRUD Lengkap**: Menyediakan endpoint untuk menambah, membaca, memperbarui, dan menghapus buku.
-   [cite_start]**Asinkron Penuh**: Semua operasi database bersifat asinkron untuk performa tinggi , menggunakan `async/await` dengan `AsyncSession` dari SQLAlchemy.
-   **Dokumentasi API Otomatis**: Dokumentasi interaktif (Swagger UI) dibuat secara otomatis oleh FastAPI dan tersedia di endpoint `/docs`.
-   **Validasi Data**: Menggunakan skema Pydantic untuk validasi permintaan (*request*) dan serialisasi respons (*response*) yang ketat.
-   **Migrasi Tabel Otomatis**: Tabel database (`books`) dibuat secara otomatis saat aplikasi dimulai berdasarkan model SQLAlchemy.

## Tumpukan Teknologi
Proyek ini menggunakan beberapa proyek *open source* untuk dapat bekerja dengan baik:
-   [FastAPI] - *Framework* web modern berkinerja tinggi untuk membangun API dengan Python.
-   [Uvicorn] - Server ASGI secepat kilat untuk menjalankan aplikasi.
-   [cite_start][SQLAlchemy] - *SQL Toolkit* dan ORM untuk Python, digunakan dalam mode asinkron.
-   [Pydantic] - Validasi data dan manajemen pengaturan menggunakan *type hints* Python.
-   [aiomysql] - *Driver* asinkron untuk mengakses *database* MySQL.
-   [cite_start][python-dotenv] - Membaca *key-value pair* dari file `.env` dan mengaturnya sebagai *environment variable*.

## Instalasi
Proyek ini membutuhkan Python 3.8+ dan server MySQL yang sedang berjalan.

**1. Clone Repositori**
```sh
git clone [https://github.com/nama-anda/nama-repo-ini.git](https://github.com/nama-anda/nama-repo-ini.git)
cd nama-repo-ini
