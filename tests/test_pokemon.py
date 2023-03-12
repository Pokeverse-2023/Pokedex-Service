from fastapi.testclient import TestClient

from app.main import app


def test_get_pokemon():
    with TestClient(app) as client:
        response = client.get("/api/v1/pokemon")
        assert response.status_code == 200
