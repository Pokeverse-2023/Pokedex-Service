from typing import Optional
from pydantic import BaseModel


class Response(BaseModel):
    message: str
    detail: Optional[dict] = None
    success: bool = False
