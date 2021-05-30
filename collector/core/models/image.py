from typing import Optional
from pydantic import BaseModel


class Image(BaseModel):
    raw: Optional[str]
    large: str
    regular: Optional[str]
    small: Optional[str]
