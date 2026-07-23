from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum


app = FastAPI()

class Difficulty(str , Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"

class QuestionRequest(BaseModel):
    question : str
    difficulty : Difficulty



def build_prompt( question , difficulty):
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

prompt = build_prompt()

@app.post("/ask")
def ask_question(request : QuestionRequest):
    return {
        "message" : "Prompt created Successfully", 
        {prompt}
    }