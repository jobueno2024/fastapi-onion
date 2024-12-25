from pydantic import BaseModel
from typing import Optional


class TaskSchema(BaseModel):
    id: Optional[int]
    title: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True
