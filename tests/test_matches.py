import sys
sys.path.insert(0, '..')

from fastapi.testclient import TestClient
from main import app  # Replace with your actual FastAPI app

client = TestClient(app)

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjViNjAyZTBjYTFmNDdhOGViZmQxMTYwNGQ5Y2JmMDZmNGQ0NWY4MmIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbGl2ZXNjb3JlLWFwaSIsImF1ZCI6ImxpdmVzY29yZS1hcGkiLCJhdXRoX3RpbWUiOjE3MDYxMDczNDcsInVzZXJfaWQiOiJaam1OeTA1U29MY0ZFclczOWFCblFlU0pEUHYxIiwic3ViIjoiWmptTnkwNVNvTGNGRXJXMzlhQm5RZVNKRFB2MSIsImlhdCI6MTcwNjEwNzM0NywiZXhwIjoxNzA2MTEwOTQ3LCJlbWFpbCI6Inl2YW5uMDc1QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJ5dmFubjA3NUBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.lnOF1QcKsnTu52qAW0bEl_YswF7qI71h1c8DfXE6NQtl6HOq-TU2EVefOUaBFo7j0cEFZ_n4JsjU5uT2HSjaK8yhAQZRL4ORM7EVSU9sgEEA6AUr9CjftZeyIvmFNjfC5oni4Hwl5ehfSt9DIIgKvXymvB_Aa1XrndYIMHEfbhVAyY7T6xeI0C9lHMKTEWzomWVyibJYTOpxXFXhjzUmjYavBR2XzJ_0MfpKIU6pk3gmqJ95Jz1-ugnUYUhwiOcGwFGe9yeNXzwErXFKz68RdlmbWKMSra-Np7jz5J-MnjqVehImvNCfdtsqRNzd8jE63qbu352AXSAyijkH53Sj5w"


def test_get_matchs():
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/matchs", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_matches_by_competition():
    team_id = "0aad8f61-fc10-4e67-8b44-fdf69eb5cc30"  
    competition = "CAN"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get(f"/matchs/{team_id}/competition?competition={competition}", headers=headers)
    assert response.status_code == 200

def test_post_match():
    new_match_data = {
  "equipe_domicile": "string",
  "equipe_exterieure": "string",
  "score_domicile": 0,
  "score_exterieur": 0,
  "competition": "string",
  "statut": "string",
  "minute": 0
} 
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/matchs", json=new_match_data, headers=headers)
    assert response.status_code == 201  


def test_patch_match():
    match_id = "0aad8f61-fc10-4e67-8b44-fdf69eb5cc30"
    modified_match_data =   {
    "id": "0aad8f61-fc10-4e67-8b44-fdf69eb5cc30",
    "equipe_domicile": "Guinée Bissau",
    "equipe_exterieure": "Nigéria",
    "score_domicile": 0,
    "score_exterieur": 1,
    "competition": "CAN",
    "statut": "Terminé",
    "minute": 0
  }  
    headers = {"Authorization": f"Bearer {token}"}
    response = client.patch(f"/{match_id}", json=modified_match_data, headers=headers)
    assert response.status_code == 204  



