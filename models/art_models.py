from pydantic import BaseModel
from typing import Optional, List


class ArtObject(BaseModel):
    objectID: int
    title: str
    artistDisplayName: Optional[str]
    objectDate: Optional[str]
    primaryImage: Optional[str]
    objectURL: Optional[str]


class SearchResponse(BaseModel):
    total: int
    objectIDs: Optional[List[int]]