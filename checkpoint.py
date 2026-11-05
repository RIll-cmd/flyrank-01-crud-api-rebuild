from fastapi.testclient import TestClient
from app import app
with TestClient(app) as c:
 assert c.get("/").json()
 assert c.get("/health").json()=={"status":"ok"}
 print("PASS root and health JSON")
