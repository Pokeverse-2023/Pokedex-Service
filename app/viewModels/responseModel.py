from typing import Optional

from pydantic import BaseModel


class Response(BaseModel):
    message: str
    detail: Optional[list] = None
    success: bool = False
