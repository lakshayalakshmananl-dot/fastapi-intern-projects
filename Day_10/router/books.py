from fastapi import APIRouter, HTTPException, BackgroundTasks
from models import Book

router = APIRouter()

books = {
    1: {"title": "Python Basics", "author": "John"},
    2: {"title": "FastAPI Guide", "author": "Alice"}
}
def send_notification(book_id: int):
    print(f"Notification sent for book ID: {book_id}")

# GET all books
@router.get("/books")
async def get_books():
    return books


# GET one book
@router.get("/books/{book_id}")
async def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")

    return books[book_id]


# CREATE
@router.post("/books")
async def create_book(book: Book):

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
async def update_book(book_id: int, book: Book):

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
async def delete_book(book_id: int):

    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")

    del books[book_id]

    return {
        "message": "Book deleted"
    } 
@router.post("/books/{book_id}/notify")
async def notify_book(
    book_id: int,
    background_tasks: BackgroundTasks
):
    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    background_tasks.add_task(
        send_notification,
        book_id
    )

    return {
        "message": f"Notification scheduled for book {book_id}"
    }