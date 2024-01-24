import sys
sys.path.insert(0, '..')

from fastapi.testclient import TestClient
from main import app  # Replace with your actual FastAPI app

client = TestClient(app)

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjViNjAyZTBjYTFmNDdhOGViZmQxMTYwNGQ5Y2JmMDZmNGQ0NWY4MmIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbGl2ZXNjb3JlLWFwaSIsImF1ZCI6ImxpdmVzY29yZS1hcGkiLCJhdXRoX3RpbWUiOjE3MDYxMDczNDcsInVzZXJfaWQiOiJaam1OeTA1U29MY0ZFclczOWFCblFlU0pEUHYxIiwic3ViIjoiWmptTnkwNVNvTGNGRXJXMzlhQm5RZVNKRFB2MSIsImlhdCI6MTcwNjEwNzM0NywiZXhwIjoxNzA2MTEwOTQ3LCJlbWFpbCI6Inl2YW5uMDc1QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJ5dmFubjA3NUBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.lnOF1QcKsnTu52qAW0bEl_YswF7qI71h1c8DfXE6NQtl6HOq-TU2EVefOUaBFo7j0cEFZ_n4JsjU5uT2HSjaK8yhAQZRL4ORM7EVSU9sgEEA6AUr9CjftZeyIvmFNjfC5oni4Hwl5ehfSt9DIIgKvXymvB_Aa1XrndYIMHEfbhVAyY7T6xeI0C9lHMKTEWzomWVyibJYTOpxXFXhjzUmjYavBR2XzJ_0MfpKIU6pk3gmqJ95Jz1-ugnUYUhwiOcGwFGe9yeNXzwErXFKz68RdlmbWKMSra-Np7jz5J-MnjqVehImvNCfdtsqRNzd8jE63qbu352AXSAyijkH53Sj5w"

def test_get_standing_by_team_id():
    team_id = "5f88e5c6-0de4-437e-9d4d-5c3828545a27"  # Replace with a valid team UUID
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get(f"/standing/{team_id}", headers=headers)
    assert response.status_code == 200

def test_modify_team_standing():
    team_id = "5f88e5c6-0de4-437e-9d4d-5c3828545a27"  
    modified_standing_data = {
  "id": "5f88e5c6-0de4-437e-9d4d-5c3828545a27",
  "name": "Cap-Vert",
  "competition": "CAN",
  "wins": 2,
  "losses": 0,
  "draws": 1,
  "points": 7,
  "place": "1er du groupe B"
}
    headers = {"Authorization": f"Bearer {token}"}
    response = client.patch(f"/standings/{team_id}", json=modified_standing_data, headers=headers)
    assert response.status_code == 204
