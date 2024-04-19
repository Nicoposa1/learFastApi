from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    book_id: int
    title: str
    author: str


@app.get("/")
def index():
    return {"message": "Hello, World"}


@app.get("/books/{book_id}")
def get_book(book_id: int):
    return {"book_id": book_id, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}


@app.post("/books/")
def create_book(book: Book):
    return {"book_id": book.book_id, "title": book.title, "author": book.author}
