from fastapi import FastAPI
from app.api.tasks import router as task_router

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API läuft"}

app.include_router(task_router)