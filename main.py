from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mlx_lm import load, generate  # Assuming mlx-lm has a ModelLoader class for loading models

# Initialize FastAPI app
app = FastAPI()

# Define the local model path
model_name = "mlx-community/Meta-Llama-3-8B-Instruct"  # Update this path to your local model directory

# Load the LLaMA model using mlx-lm
model, tokenizer = load(model_name)


# Define input data model
class TextInput(BaseModel):
    text: str


@app.post("/generate/")
async def generate_text(input: TextInput):
    try:
        generated_text = generate(model, tokenizer, prompt=input.text)
        return {"generated_text": generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the app with: uvicorn app:app --reload
