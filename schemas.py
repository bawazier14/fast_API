# schemas.py

from pydantic import BaseModel, Field
from typing import Optional

# Schema untuk request (saat membuat atau mengupdate buku)
class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    author: str = Field(..., min_length=1, max_length=255)
    year: int = Field(..., gt=1900, lt=2026)
    description: Optional[str] = Field(None, max_length=1000)

    class Config: # Pydantic configuration
        schema_extra = {
            "example": {
                "title": "The Hobbit",
                "author": "J.R.R. Tolkien",
                "year": 1937,
                "description": "A fantasy novel."
            }
        }

# Schema untuk response (saat mengembalikan data buku dari API)
# Kita tambahkan 'id' karena 'id' akan otomatis dihasilkan oleh database
class Book(BookCreate):
    id: int

    class Config:
        orm_mode = True # Ini penting! Memberitahu Pydantic untuk bisa membaca data dari objek ORM SQLAlchemy