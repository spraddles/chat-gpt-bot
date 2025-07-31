from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "EleutherAI/gpt-neo-125M"

print(f"[model.py] Loading {MODEL_NAME}…")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()
if torch.cuda.is_available():
    model.cuda()
print("[model.py] Model ready!")
