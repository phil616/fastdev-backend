from fastapi.testclient import TestClient


def test_root_request(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data == {"message": "Hello World"}
