from pydantic import BaseModel

class ChatRequest(BaseModel):
    prompt: str
    max_length: int = 100
    temperature: float = 0.7
    top_p: float = 0.9

class ChatResponse(BaseModel):
    response: str
