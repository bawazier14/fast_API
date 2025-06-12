# models.py

from sqlalchemy import Column, Integer, String, Text
from database import Base # Import Base dari database.py

# Definisikan tabel "books"
class Book(Base):
    __tablename__ = "books" # Nama tabel di database

    id = Column(Integer, primary_key=True, index=True) # Primary key, auto-increment, index untuk pencarian cepat
    title = Column(String(255), index=True) # String dengan panjang maksimal 255, index
    author = Column(String(255))
    year = Column(Integer)
    description = Column(Text, nullable=True) # Text untuk string panjang, nullable=True berarti boleh kosong

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}')>"