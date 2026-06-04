from fastapi import APIRouter, HTTPException
from models import Book

router = APIRouter()

books = {
    1: {"title": "Python Basics", "author": "John"},
    2: {"title": "FastAPI Guide", "author": "Alice"}
}

# GET all books
@router.get("/books")
def get_books():
    return books


# GET one book
@router.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")

    return books[book_id]


# CREATE
@router.post("/books")
def create_book(book: Book):

    new_id = max(books.keys()) + 1

    books[new_id] = {
        "title": book.title,
        "author": book.author
    }

    return {
        "message": "Book created",
        "book_id": new_id
    }


# UPDATE
@router.put("/books/{book_id}")
def update_book(book_id: int, book: Book):

    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")

    books[book_id] = {
        "title": book.title,
        "author": book.author
    }

    return {
        "message": "Book updated"
    }


# DELETE
@router.delete("/books/{book_id}")
def delete_book(book_id: int):

    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")

    del books[book_id]

    return {
        "message": "Book deleted"
    }