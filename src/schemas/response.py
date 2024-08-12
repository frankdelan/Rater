from typing import Any

from pydantic import BaseModel


class ResponseSchema(BaseModel):
    status: int = 200
    data: Any = None
    detail: str = ''
