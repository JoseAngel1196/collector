from typing import Optional, List
from datetime import date
from pydantic import BaseModel

from collector.core.models.image import Image
from collector.core.models.user import User


class Photo(BaseModel):
    title: Optional[str] = "NULL"
    description: Optional[str] = "NULL"
    photo_image: Image
    likes: Optional[int] = "NULL"

    user: User

    tags: Optional[List[str]] = "NULL"
    categories: Optional[List[str]] = "NULL"

    published_at: Optional[date] = "NULL"
