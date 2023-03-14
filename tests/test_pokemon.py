from fastapi.testclient import TestClient

from app.core.pokemon import PokemonCore
from app.main import app


def test_bulk_insert():
    """
    Test: Bulk Insert Pokemons
    """
    with TestClient(app) as client:
        response = client.post("/api/v1/pokemon")
        assert response.status_code == 200


def test_root():
    """
    Test: Welcome
    """
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200


def test_get_pokemon():
    """
    Test: Get All Pokemom
    """
    with TestClient(app) as client:
        response = client.get("/api/v1/pokemon")
        assert response.status_code == 200


def test_get_pokemon_with_filter():
    """
    Test: Get A Pokemon With Filter
    """
    with TestClient(app) as client:
        response = client.get("/api/v1/pokemon?search=ch")
        assert response.status_code == 200
