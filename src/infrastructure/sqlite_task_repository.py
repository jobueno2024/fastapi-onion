import sqlite3
import tempfile
from domain.task import Task, TaskRepository
from typing import List, Optional


class SqliteTaskRepository(TaskRepository):
    def __init__(self, db_path: str = "tasks.db"):
        self.db_path = db_path
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT
                )
                """
            )
            conn.commit()

    async def create(self, task: Task) -> Task:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tasks (title, description) VALUES (?, ?)",
                (task.title, task.description),
            )
            conn.commit()
            task.id = cursor.lastrowid  # Assign the newly generated ID
        return task

    async def get(self, task_id: int) -> Optional[Task]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
            row = cursor.fetchone()
            if row:
                return Task(id=row[0], title=row[1], description=row[2])
        return None

    # def __del__(self):
    #     if self.conn:
    #         self.conn.close()