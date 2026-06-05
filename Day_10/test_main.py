from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Book API"
    }
    
def test_get_books():
    response = client.get("/books")

    assert response.status_code == 200
def test_create_book():
    response = client.post(
        "/books",
        json={
            "title": "Harry Potter",
            "author": "J.K. Rowling"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Book created"
    
def test_update_book():
    response = client.put(
        "/books/1",
        json={
            "title": "Updated Python",
            "author": "John"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Book updated"
    
def test_delete_book():
    response = client.delete("/books/2")

    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted"