import sys
sys.path.insert(0, '..')

from fastapi.testclient import TestClient
from main import app  # Importez app depuis main.py

client = TestClient(app)

def test_get_leagues():
    response = client.get("/leagues")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_league():
    response = client.post("/leagues", json={"name": "Serie A", "country": "Italie"})
    assert response.status_code == 200
    assert response.json()["name"] == "Serie A"
    assert response.json()["country"] == "Italie"

def test_modify_league():
    # Assurez-vous que la ligue à modifier existe déjà
    response = client.patch("/leagues/Premier League", json={"name": "Premier League Up", "country": "Angleterre"})
    assert response.status_code == 200
    assert response.json()["name"] == "Premier League Up"

def test_delete_league():
    # Ajoutez d'abord une ligue pour la supprimer
    client.post("/leagues", json={"name": "Test League", "country": "Test Country"})
    response = client.delete("/leagues/Test League")
    assert response.status_code == 204

    # Vérifier que la ligue a été supprimée
    response = client.get("/leagues")
    assert all(league["name"] != "Test League" for league in response.json())