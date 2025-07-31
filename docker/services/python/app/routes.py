from fastapi import APIRouter, HTTPException
from .schemas import ChatRequest, ChatResponse
from .model import tokenizer, model
import torch

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):

    # tokenize
    inputs = tokenizer(req.prompt, return_tensors="pt")
    if torch.cuda.is_available():
        inputs = {k: v.cuda() for k, v in inputs.items()}

    # generate
    try:
        outputs = model.generate(
            **inputs,
            max_length=req.max_length,
            temperature=req.temperature,
            top_p=req.top_p,
            pad_token_id=tokenizer.eos_token_id,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # only return the new content after the prompt
    response_text = decoded[len(req.prompt):].strip()
    return ChatResponse(response=response_text)
