from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
from repository import Repository

repo = Repository()

@asynccontextmanager
async def lifespan(app):
    repo.initialize()
    yield

app = FastAPI(title="Task API", lifespan=lifespan, docs_url=None, redoc_url=None, openapi_url=None)

@app.get("/", summary="Describe the API")
def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health", summary="Check service health")
def health(): return {"status": "ok"}

@app.get("/tasks", summary="List tasks")
def list_tasks(): return repo.list()

@app.get("/tasks/{task_id}", summary="Get a task")
def get_task(task_id: int):
    task = repo.get(task_id)
    return task if task else JSONResponse({"error": f"Task {task_id} not found"}, status_code=404)

