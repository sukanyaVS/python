import json
from pathlib import Path

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

class Book(BaseModel):
    author: str
    title: str
    published_date: str
    category: str

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
BOOKS_FILE = BASE_DIR / "books.txt"



books = json.loads(BOOKS_FILE.read_text())


@app.get("/", response_class=HTMLResponse)
def home():
  return "<h1>Hello FastAPI!</h1>"


@app.get("/api/books")
def get_books():
  return {"books": books}


@app.get("/api/books/{book_id}")
def get_book_by_id(book_id: int):
  for book in books:
    if book["id"] == book_id:
     return book
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found") 


@app.post("/api/books")
def create_book(book: Book):
  new_book = book.model_dump()
  new_book["id"] = len(books) + 1
  books.append(new_book)
  return new_book


@app.put("/api/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
  for book in books:
   if book["id"] == book_id:
    book.update(updated_book.model_dump()) 
    return book
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found") 



@app.delete("/api/books/{book_id}")
def delete_book(book_id: int):
  for book in books:
    if book["id"] == book_id:
        deleted_book = books.remove(book)
        return {"message": "Book deleted"}
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


