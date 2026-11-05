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

async def valid_body(request, partial=False):
    try: body = await request.json()
    except ValueError: return None
    if not isinstance(body, dict) or not body or set(body) - {"title", "done"}: return None
    if not partial and "title" not in body: return None
    if "title" in body and (not isinstance(body["title"], str) or not body["title"].strip()): return None
    if "done" in body and type(body["done"]) is not bool: return None
    return body

@app.post("/tasks", status_code=201, summary="Create a task", openapi_extra={"requestBody":{"required":True,"content":{"application/json":{"schema":{"type":"object","properties":{"title":{"type":"string"}},"required":["title"]}}}}})
async def create_task(request: Request):
    body = await valid_body(request)
    if body is None: return JSONResponse({"error": "A non-empty title is required"}, status_code=400)
    return repo.create(body["title"])

