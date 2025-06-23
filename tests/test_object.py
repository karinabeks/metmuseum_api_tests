import pytest
from utils.api_client import get_object
from models.art_models import ArtObject

@pytest.mark.parametrize("object_id", [436121, 437853, 459097])
def test_get_valid_objects(object_id):
    response = get_object(object_id)
    assert response.status_code == 200
    data = response.json()
    obj = ArtObject(**data)
    assert obj.objectID == object_id
    assert isinstance(obj.title, str)
    assert "http" in obj.objectURL

def test_get_invalid_object():
    response = get_object(999999999)
    assert response.status_code == 404 or response.json().get("message", "") != ""