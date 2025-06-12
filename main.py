# main.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

# Import dari file yang baru kita buat
from database import get_db, Base, engine # Import Base dan engine untuk migrasi
import models # Import model ORM kita
import schemas # Import schemas Pydantic kita

# Inisialisasi aplikasi FastAPI
app = FastAPI(
    title="FastAPI Book Management API (with MySQL & SQLAlchemy)",
    description="A more robust API to manage books, using MySQL as the database.",
    version="1.0.0"
)

# --- Life Cycle Events (untuk membuat tabel saat aplikasi startup) ---
# Ini akan membuat tabel 'books' di database jika belum ada
@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        # Menghapus tabel jika sudah ada (opsional, untuk development)
        # await conn.run_sync(Base.metadata.drop_all)
        # Membuat semua tabel yang didefinisikan di Base.metadata
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created/checked!")

# --- ENDPOINTS API ---

# 1. Root Endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI Book API! Go to /docs for interactive documentation."}

# 2. Get All Books
@app.get("/books/", response_model=List[schemas.Book], summary="Get all books")
async def get_all_books(db: AsyncSession = Depends(get_db)):
    """
    Retrieve a list of all books from the database.
    """
    # Mengambil semua buku dari database
    # session.execute(select(models.Book)) adalah cara SQLAlchemy modern
    # .scalars().all() akan mengambil objek Book dari hasil query
    result = await db.execute(models.Book.__table__.select())
    books = result.scalars().all()
    return books

# 3. Get Book by ID
@app.get("/books/{book_id}", response_model=schemas.Book, summary="Get a book by its ID")
async def get_book_by_id(book_id: int, db: AsyncSession = Depends(get_db)):
    """
    Retrieve a single book by its unique ID.
    Raises a 404 error if the book is not found.
    """
    # Mengambil satu buku berdasarkan ID
    book = await db.get(models.Book, book_id) # Lebih sederhana daripada select().where()
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")
    return book

# 4. Add a New Book
@app.post("/books/", response_model=schemas.Book, status_code=201, summary="Add a new book")
async def add_book(book: schemas.BookCreate, db: AsyncSession = Depends(get_db)):
    """
    Add a new book to the database.
    """
    # Membuat instance model ORM dari data Pydantic
    db_book = models.Book(**book.model_dump()) # model_dump() untuk Pydantic v2+

    db.add(db_book) # Menambahkan objek ke sesi database
    await db.commit() # Menyimpan perubahan ke database
    await db.refresh(db_book) # Memuat ulang objek untuk mendapatkan ID yang dihasilkan database
    return db_book

# 5. Update an Existing Book
@app.put("/books/{book_id}", response_model=schemas.Book, summary="Update an existing book")
async def update_book(book_id: int, updated_book_data: schemas.BookCreate, db: AsyncSession = Depends(get_db)):
    """
    Update the details of an existing book.
    Raises a 404 error if the book is not found.
    """
    book_to_update = await db.get(models.Book, book_id)
    if not book_to_update:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")

    # Update atribut objek model ORM dengan data baru
    for key, value in updated_book_data.model_dump(exclude_unset=True).items(): # exclude_unset=True agar tidak mengupdate field yang tidak dikirim
        setattr(book_to_update, key, value)

    await db.commit()
    await db.refresh(book_to_update)
    return book_to_update

# 6. Delete a Book
@app.delete("/books/{book_id}", status_code=204, summary="Delete a book")
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    """
    Delete a book from the database by its ID.
    Raises a 404 error if the book is not found.
    """
    book_to_delete = await db.get(models.Book, book_id)
    if not book_to_delete:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")

    await db.delete(book_to_delete)
    await db.commit()
    return {"message": "Book deleted successfully."} # Return pesan untuk 200 OK jika mau, tapi 204 tidak perlu body