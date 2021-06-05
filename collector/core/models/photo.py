from typing import Optional, List
from datetime import date
from pydantic import BaseModel

from collector.core.models.image import Image
from collector.core.models.user import User
from collector.core.enums import StockType


class Photo(BaseModel):
    title: Optional[str]
    description: Optional[str]
    urls: Image
    likes: Optional[int]

    user: User

    tags: Optional[List[str]] = []
    categories: Optional[List[str]]

    published_at: date

    stock_type: StockType
