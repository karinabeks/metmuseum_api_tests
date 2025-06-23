import requests
from models.art_models import SearchResponse

BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"

def test_search_objects():
    response = requests.get(f"{BASE_URL}/search", params={"q": "sunflower"})
    assert response.status_code == 200
    data = response.json()
    result = SearchResponse(**data)
    assert result.total >= 0

def test_search_limit_results():
    response = requests.get(f"{BASE_URL}/search", params={"q": "flower"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data.get("objectIDs"), list)
    assert data["total"] <= len(data["objectIDs"])