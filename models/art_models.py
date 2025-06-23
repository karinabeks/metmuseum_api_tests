from pydantic import BaseModel
from typing import List, Optional

class ArtObject(BaseModel):
    objectID: int
    title: str
    artistDisplayName: str
    objectDate: str
    objectName: str
    medium: Optional[str]

class SearchResponse(BaseModel):
    total: int
    objectIDs: List[int]