from typing import List, Optional
from pydantic import BaseModel


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None


class TaskRepository:
    async def create(self, task: Task) -> Task:
        raise NotImplementedError

    async def get(self, task_id: int) -> Optional[Task]:
        raise NotImplementedError
