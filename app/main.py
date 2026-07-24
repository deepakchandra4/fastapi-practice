from fastapi import FastAPI

from app.models.requests import QuestionRequest
from app.services.prompt_service import build_prompt
from app.services.gemini_service import generate_response


app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "AI Tutor API is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    prompt = build_prompt(
        request.question,
        request.difficulty
    )

    answer = generate_response(prompt)

    return {
        "question": request.question,
        "difficulty": request.difficulty,
        "answer": answer
    }