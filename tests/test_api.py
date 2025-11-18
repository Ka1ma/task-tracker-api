import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_register_and_login():
    async with AsyncClient() as ac:
        # Register user
        register_payload = {"email": "testuser@example.com", "username": "testuser", "password": "123456"}
        reg_response = await ac.post("http://127.0.0.1:8000/api/auth/register", json=register_payload)
        assert reg_response.status_code in [200, 400]

        # Login
        login_payload = {"email": "testuser@example.com", "password": "123456"}
        login_response = await ac.post("http://127.0.0.1:8000/api/auth/login", json=login_payload)
        assert login_response.status_code == 200
        token = login_response.json()["access_token"]

        # Create task
        task_payload = {"title": "Test Task", "description": "Testing task creation"}
        task_response = await ac.post("http://127.0.0.1:8000/api/tasks/", json=task_payload, headers={"Authorization": f"Bearer {token}"})
        assert task_response.status_code in [200, 201]

        # List tasks
        list_response = await ac.get("http://127.0.0.1:8000/api/tasks/", headers={"Authorization": f"Bearer {token}"})
        assert list_response.status_code == 200
        assert "tasks" in list_response.json()

        # Update task
        task_id = list_response.json()["tasks"][0]["id"]
        update_payload = {"title": "Updated Task"}
        update_response = await ac.put(f"http://127.0.0.1:8000/api/tasks/{task_id}", json=update_payload, headers={"Authorization": f"Bearer {token}"})
        assert update_response.status_code == 200

        # Delete task
        delete_response = await ac.delete(f"http://127.0.0.1:8000/api/tasks/{task_id}", headers={"Authorization": f"Bearer {token}"})
        assert delete_response.status_code == 200
