from fastapi import APIRouter, HTTPException
from .schemas import ChatRequest, ChatResponse
from .model import tokenizer, model
import torch

router = APIRouter()
INSTRUCTION = (
    "You are a helpful assistant. Answer the question concisely and factually.\n"
)

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    prompt = (INSTRUCTION + req.prompt.strip()).strip()
    inputs = tokenizer(prompt, return_tensors="pt")
    if torch.cuda.is_available():
        inputs = {k: v.cuda() for k, v in inputs.items()}

    try:
        outputs = model.generate(
            **inputs,
            max_length=req.max_length,
            do_sample=True,
            temperature=req.temperature,
            top_p=req.top_p,
            repetition_penalty=1.2,
            no_repeat_ngram_size=2,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    answer = decoded[len(prompt):].strip()
    return ChatResponse(response=answer)
