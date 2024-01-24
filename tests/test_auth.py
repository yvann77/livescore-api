import sys
sys.path.insert(0, '..')

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_signup():
    new_user_data = {"email": "postest@gmail.com", "password": "12345678"}
    response = client.post("/auth/signup", json=new_user_data)
    assert response.status_code == 201

def test_login():
    user_credentials = {"username": "yvann77@gmail.com", "password": "12345678"}
    response = client.post("/auth/login", data=user_credentials)
    assert response.status_code == 201
    assert "access_token" in response.json()  # Check if response contains access_token
