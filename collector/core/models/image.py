from typing import Optional
from pydantic import BaseModel

class Image(BaseModel):
    raw: str
    full: str
    regular: Optional[str]
    small: Optional[str]