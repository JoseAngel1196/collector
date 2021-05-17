from pydantic import BaseModel


class Settings(BaseModel):
    stock_name: str
