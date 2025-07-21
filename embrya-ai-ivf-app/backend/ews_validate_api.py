from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai, os

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/generate_protocol/")
async def generate_protocol(request: Request):
    req = await request.json()
    prompt = req.get("prompt")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return {"result": response["choices"][0]["message"]["content"]}
