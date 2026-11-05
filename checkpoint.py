from fastapi.testclient import TestClient
from app import app
with TestClient(app) as c:
 assert c.get("/").status_code==200
 print("PASS hello HTTP 200")
