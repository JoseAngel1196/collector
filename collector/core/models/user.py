from typing import Optional
from typing import Optional
from pydantic import BaseModel

from collector.core.models.image import Image


class User(BaseModel):
    user_id: str
    username: str
    first_name: str
    last_name: str
    portfolio_url: str
    bio: str
    profile_image: Image

    # Build with first_name and last_name
    full_name: Optional[str]

    # Social Media
    instagram_username: Optional[str]
    twitter_username: Optional[str]

    # Rating
    total_likes: Optional[int]
    total_photos: Optional[int]
    for_hire: Optional[bool]
