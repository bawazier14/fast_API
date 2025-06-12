# database.py

import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base # Digunakan untuk mendefinisikan model
from sqlalchemy.orm import sessionmaker

# Muat variabel lingkungan dari .env
load_dotenv()

# Ambil URL database dari environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Pastikan DATABASE_URL tidak kosong
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set. Please create a .env file.")

# Buat mesin koneksi asinkron SQLAlchemy
# echo=True akan menampilkan query SQL di console (bagus untuk debugging)
engine = create_async_engine(DATABASE_URL, echo=True)

# Konfigurasi AsyncSessionLocal
# expire_on_commit=False mencegah objek di-detached setelah commit
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession # Gunakan AsyncSession untuk operasi asinkron
)

# Base class untuk model ORM kita
Base = declarative_base()

# Dependency untuk mendapatkan sesi database
# Ini akan digunakan di endpoint FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session