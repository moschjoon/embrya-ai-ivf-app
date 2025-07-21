
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate_protocol")
async def generate_protocol(req: Request):
    body = await req.json()
    prompt = body.get("prompt", "")
    role = body.get("role", "Clinician")
    full_prompt = f"You are a {role} tasked with the following:\n{prompt}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": full_prompt}],
        temperature=0.7,
        max_tokens=800
    )
    return {"response": response['choices'][0]['message']['content']}
