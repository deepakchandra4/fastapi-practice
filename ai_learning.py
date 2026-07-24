from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from dotenv import load_dotenv
import os 
from google import genai


app = FastAPI()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if api_key:
    print("API key is verified")
else:
    print("API key doesn't exist")


class Difficulty(str , Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"

class QuestionRequest(BaseModel):
    question : str
    difficulty : Difficulty



def build_prompt(question , difficulty):
    if difficulty == "beginner":
        return f"""You are a programming tutor.
        Explain the concept to a complete beginner.
        Use simple language.
        Avoid unnecessary technical jargon.
        Give a real-world analogy.
        Question: {question}"""
    elif difficulty == "intermediate":
        return f"""You are an experienced programming instructor.
        Explain the concept at an intermediate level.
        Use appropriate technical terminology.
        Include practical examples.
        Question: {question}"""
    elif difficulty == "advanced":
        return f"""You are a senior software engineer.
        Explain the concept at an advanced technical level.
        Discuss implementation details and trade-offs.
        Use appropriate technical terminology.
            Question: {question}"""
    else:
        return "Invalid "



@app.post("/ask")
def ask_question(request : QuestionRequest):

    prompt = build_prompt(
        request.question,
        request.difficulty
    )
    return {
        "message" : "Prompt created Successfully", 
        "prompt":prompt
    }