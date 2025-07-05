import pytest
from fastapi.testclient import TestClient


# 使用 fixture 共享 user_id
@pytest.fixture(scope="module")
def created_user_id(client: TestClient) -> int:
    response = client.post(
        "/user/create", json={"username": "testUser", "password": "123456"}
    )
    assert response.status_code == 200
    data = response.json()
    return data["id"]  # 假设返回结果包含 id 字段


def test_get_user_by_id(client: TestClient) -> None:
    response = client.post(
        "/user/create", json={"username": "waitingForUpdate", "password": "123456"}
    )
    prepared_user_id = response.json()["id"]
    assert response.status_code == 200
    response = client.get(f"/user/{prepared_user_id}")
    assert response.status_code == 200


def test_create_user(client: TestClient) -> None:
    response = client.post(
        "/user/create", json={"username": "testUser", "password": "123456"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data


def test_delete_user(client: TestClient) -> None:
    response = client.post(
        "/user/create", json={"username": "waitingForDelete", "password": "123456"}
    )
    prepared_user_id = response.json()["id"]
    assert response.status_code == 200
    response = client.delete(f"/user/{prepared_user_id}")
    assert response.status_code == 204


def test_update_user(client: TestClient) -> None:
    response = client.post(
        "/user/create", json={"username": "waitingForUpdate", "password": "123456"}
    )
    prepared_user_id = response.json()["id"]
    assert response.status_code == 200
    response = client.put(
        f"/user/{prepared_user_id}", json={"username": "Updated", "password": "123456"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "Updated"


def test_get_all_user(client: TestClient) -> None:
    response = client.get("/user/all")
    assert response.status_code == 200
