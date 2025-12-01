# main.py
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.genai as genai
from dotenv import load_dotenv

load_dotenv()

# Load API key from env
api = os.getenv("gemini_key")



# Configure the client
client = genai.Client(api_key=api)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProcessRequest(BaseModel):
    action: str  # "rewrite", "summarize", "grammar", "expand"
    text: str

class ProcessResponse(BaseModel):
    success: bool
    result: str

# Optional: define prompt logic
SYSTEM_PROMPT = (
    "You are EssayFix — a helpful assistant specialized in improving English texts. "
    "Be concise, clear, preserve the author's intent, and provide the requested transform."
)

TASK_INSTRUCTIONS = {
    "rewrite": "Rewrite the following text to improve clarity, flow, and tone while preserving the original meaning.",
    "summarize": "Summarize the following text in 1-2 concise sentences capturing the main point.",
    "grammar": "Fix grammar, punctuation, and awkward phrasing in the text. Keep changes minimal and retain the original voice.",
    "expand": "Expand the following short passage into a more detailed paragraph that adds helpful detail, explanation, or examples while preserving the original intent."
}

@app.post("/api/process", response_model=ProcessResponse)
def process(req: ProcessRequest):
    text = req.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text is required.")

    if req.action not in TASK_INSTRUCTIONS:
        raise HTTPException(status_code=400, detail="Invalid action")

    prompt = (
        SYSTEM_PROMPT
        + "\nTASK: " + TASK_INSTRUCTIONS[req.action]
        + "\nINPUT:\n" + text
        + "\nOUTPUT:"
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",  # or choose another model
            contents=prompt
        )
        # The SDK returns a response object with .text attribute
        result_text = response.text.strip()
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Gemini error: {str(e)}")

    return ProcessResponse(success=True, result=result_text)
