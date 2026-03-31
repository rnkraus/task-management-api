# Task Management API

Simple backend API built with FastAPI.

## Task Model

- id: int
- title: str
- completed: bool

## Endpoints

- POST /tasks
- GET /tasks
- GET /tasks/{task_id}
- PUT /tasks/{task_id}
- DELETE /tasks/{task_id}

## Rules

- title is required
- id is generated automatically
- completed defaults to false
- return 404 if task not found