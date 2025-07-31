from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/hello")
def hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}
