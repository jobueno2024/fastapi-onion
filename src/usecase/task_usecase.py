from domain.task import Task, TaskRepository


class TaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    async def create_task(self, task: Task) -> Task:
        created_task = await self.task_repository.create(task)
        return created_task

    async def get_task(self, task_id: int) -> Task:
        task = await self.task_repository.get(task_id)
        if task is None:
            raise Exception("Task not found") # Exception handling should be more robust.
        return task
