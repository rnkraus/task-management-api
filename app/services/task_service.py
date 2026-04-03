from app.core.db import SessionLocal
from app.models.task import Task as TaskModel


def create_task(task_data):
    db = SessionLocal()
    try:
        new_task = TaskModel(
            title=task_data.title,
            completed=task_data.completed,
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    finally:
        db.close()


def get_all_tasks():
    db = SessionLocal()
    try:
        return db.query(TaskModel).all()
    finally:
        db.close()


def get_task_by_id(task_id: int):
    db = SessionLocal()
    try:
        return db.query(TaskModel).filter(TaskModel.id == task_id).first()
    finally:
        db.close()


def update_task(task_id: int, task_data):
    db = SessionLocal()
    try:
        task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if task is None:
            return None

        task.title = task_data.title
        task.completed = task_data.completed

        db.commit()
        db.refresh(task)
        return task
    finally:
        db.close()


def patch_task(task_id: int, task_data):
    db = SessionLocal()
    try:
        task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if task is None:
            return None

        if task_data.title is not None:
            task.title = task_data.title
        if task_data.completed is not None:
            task.completed = task_data.completed

        db.commit()
        db.refresh(task)
        return task
    finally:
        db.close()


def delete_task(task_id: int):
    db = SessionLocal()
    try:
        task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if task is None:
            return None

        db.delete(task)
        db.commit()
        return task
    finally:
        db.close()