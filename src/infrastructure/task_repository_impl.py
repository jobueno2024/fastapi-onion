from domain.task import Task, TaskRepository
from typing import List, Optional


class TaskRepositoryImpl(TaskRepository):
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    async def create(self, task: Task) -> Task:
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)
        return task

    async def get(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
