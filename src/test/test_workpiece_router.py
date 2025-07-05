from fastapi.testclient import TestClient


def create_user_prepared(client: TestClient) -> dict:  # type: ignore
    response = client.post(
        "/workpiece", json={"name": "World", "info": "Hello World", "status": "active"}
    )
    assert response.status_code == 200
    data = response.json()
    return data


def test_workpiece_create(client: TestClient) -> None:
    response = client.post(
        "/workpiece", json={"name": "World", "info": "Hello World", "status": "active"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data


def test_workpiece_update(client: TestClient) -> None:
    id = create_user_prepared(client)["id"]
    response = client.put(
        f"/workpiece/{id}",
        json={"name": "Updated World", "info": "Hello World", "status": "active"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated World"


def test_workpiece_delete(client: TestClient) -> None:
    id = create_user_prepared(client)["id"]
    response = client.delete(f"/workpiece/{id}")
    assert response.status_code == 200


def test_workpiece_get_by_id(client: TestClient) -> None:
    id = create_user_prepared(client)["id"]
    response = client.get(f"/workpiece/{id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == id


def test_workpiece_update_brand_new(client: TestClient) -> None:
    id = create_user_prepared(client)["id"]  # make sure it doesn't exist
    response = client.put(
        f"/workpiece/{int(id) + 1}",
        json={"name": "Updated World", "info": "Hello World", "status": "active"},
    )
    assert response.status_code == 404


def test_workpiece_delete_brand_new(client: TestClient) -> None:
    id = create_user_prepared(client)["id"]  # make sure it doesn't exist
    response = client.delete(f"/workpiece/{int(id) + 1}")
    assert response.status_code == 404
