from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

user_data = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123"
}


def get_token():
    client.post("/auth/register", json=user_data)

    response = client.post(
        "/auth/login",
        json={
            "email": user_data["email"],
            "password": user_data["password"]
        }
    )

    return response.json()["access_token"]


def test_register():
    response = client.post(
        "/auth/register",
        json={
            "username": "user1",
            "email": "user1@test.com",
            "password": "password123"
        }
    )

    assert response.status_code in [200, 400]


def test_login():
    client.post("/auth/register", json=user_data)

    response = client.post(
        "/auth/login",
        json={
            "email": user_data["email"],
            "password": user_data["password"]
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_create_task():
    token = get_token()

    response = client.post(
        "/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Learn JWT",
            "description": "Finish auth"
        }
    )

    assert response.status_code == 200


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200


def test_get_task():
    response = client.get("/tasks/1")

    assert response.status_code in [200, 404]


def test_update_task():
    token = get_token()

    response = client.put(
        "/tasks/1",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Updated",
            "description": "Updated desc",
            "completed": True
        }
    )

    assert response.status_code in [200, 404]


def test_delete_task():
    token = get_token()

    response = client.delete(
        "/tasks/1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code in [200, 404]


def test_sentiment():
    token = get_token()

    create_response = client.post(
        "/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "I love FastAPI",
            "description": "Amazing framework"
        }
    )

    task_id = create_response.json()["id"]

    response = client.post(
        f"/tasks/{task_id}/sentiment",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert "label" in response.json()
