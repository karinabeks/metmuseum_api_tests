import requests
from models.art_models import ArtObject

BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"

def test_get_existing_object():
    object_id = 436535
    response = requests.get(f"{BASE_URL}/objects/{object_id}")
    assert response.status_code == 200
    data = response.json()
    art = ArtObject(**data)

def test_get_nonexistent_object():
    object_id = 0
    response = requests.get(f"{BASE_URL}/objects/{object_id}")
    assert response.status_code == 404 or response.json().get("message") is not None