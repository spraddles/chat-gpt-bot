from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Local GPT-Neo Chat")
app.include_router(router, prefix="/api")

@app.get("/health", tags=["health"])
def healthcheck():
    return {"status": "ok"}
