from fastapi import FastAPI, Depends
from domain.task import Task, TaskRepository
from usecase.task_usecase import TaskUseCase
from infrastructure.sqlite_task_repository import SqliteTaskRepository
from presentation.schemas import TaskSchema

app = FastAPI()


def task_usecase_factory():
    task_repository: TaskRepository = SqliteTaskRepository()
    return TaskUseCase(task_repository)


@app.post("/tasks", response_model=TaskSchema)
async def create_task(task: TaskSchema, usecase: TaskUseCase = Depends(task_usecase_factory)):
    created_task = await usecase.create_task(Task(**task.dict()))
    return TaskSchema.from_orm(created_task)


@app.get("/tasks/{task_id}", response_model=TaskSchema)
async def get_task(task_id: int, usecase: TaskUseCase = Depends(task_usecase_factory)):
    task = await usecase.get_task(task_id)
    return TaskSchema.from_orm(task)
