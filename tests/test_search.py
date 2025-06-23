import pytest
from utils.api_client import search_objects
from models.art_models import SearchResponse

@pytest.mark.parametrize("query", ["sunflower", "van Gogh", "portrait", "Egypt", "armor"])
def test_search_various_keywords(query):
    response = search_objects(query)
    assert response.status_code == 200
    result = SearchResponse(**response.json())
    assert isinstance(result.total, int)
    if result.total > 0:
        assert isinstance(result.objectIDs, list)

def test_search_with_no_results():
    response = search_objects("asdjhaskjdhkajshdk")
    assert response.status_code == 200
    result = SearchResponse(**response.json())
    assert result.total == 0 or result.objectIDs == []

@pytest.mark.parametrize("has_images", [True, False])
def test_search_with_image_filter_toggle(has_images):
    response = search_objects("sunflower", has_images=has_images)
    assert response.status_code == 200
    result = SearchResponse(**response.json())
    assert isinstance(result.total, int)
    assert isinstance(result.objectIDs, list) or result.objectIDs is None

def test_search_with_empty_query():
    response = search_objects("")
    assert response.status_code == 200
    result = SearchResponse(**response.json())
    assert isinstance(result.total, int)