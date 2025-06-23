import requests
import logging

logging.basicConfig(level=logging.INFO, filename="logs/test_log.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"

def get_object(object_id: int):
    url = f"{BASE_URL}/objects/{object_id}"
    logging.info(f"GET {url}")
    response = requests.get(url)
    logging.info(f"Response [{response.status_code}]: {response.text[:200]}")
    return response

def search_objects(query: str, has_images: bool = False):
    url = f"{BASE_URL}/search"
    params = {"q": query}
    if has_images:
        params["hasImages"] = "true"
    logging.info(f"GET {url} with params {params}")
    response = requests.get(url, params=params)
    logging.info(f"Response [{response.status_code}]: {response.text[:200]}")
    return response