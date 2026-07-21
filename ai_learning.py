from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
qanda = {
    "question" : str, 
    "difficulty" : str
}

@app.ask_router("/ask")
def asking():
    return 