from typing import Optional, List
from pydantic import BaseModel
from datetime import date

from collector.core.models.image import Image
from collector.core.models.user import User
from collector.core.enums import StockType


class Photo(BaseModel):
    photo_id: str
    title: str
    description: str
    urls: Image
    likes: int

    user: User

    tags: List[str]
    categories: Optional[List[str]]

    published_at: date

    stock_type: StockType
