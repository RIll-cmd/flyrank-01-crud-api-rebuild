from fastapi.testclient import TestClient
from app import app
with TestClient(app) as c:
 assert c.post("/tasks",json={"title":"New"}).status_code==201
 assert len(c.get("/tasks").json())==4
 assert c.post("/tasks",json={}).status_code==400
 print("PASS create 201, list update, validation 400")
