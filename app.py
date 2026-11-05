from fastapi import FastAPI
app=FastAPI(docs_url=None,redoc_url=None,openapi_url=None)
@app.get("/")
def root(): return {"message":"Hello"}
@app.get("/health")
def health(): return {"status":"ok"}
