from typing import Optional
from pydantic import BaseModel


class Image(BaseModel):
    raw: Optional[str]
    small: Optional[str]
    regular: Optional[str]
    large: Optional[str]
