from google import genai
import os 
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


load_dotenv()

api = os.getenv("gemini_key")

client = genai.Client(api_key=api)

class Request(BaseModel):
    message: str
    model:str = "gemini-2.5-flash"

# variable for persona
persona = """
you are a loan agent, only answer relating to that
- always answer briefly
"""

@app.get("/")
def root():
    return {"message": "Welcome to Loan Agent"}


@app.post("/chat")
def chat(input:Request):
    userInput=input.message 
    model = input.model
    final_input=f"{persona}\n\n {userInput}"

    response = client.models.generate_content(
        model=model,
        contents= final_input
    )


    return(f"{response.text}")
