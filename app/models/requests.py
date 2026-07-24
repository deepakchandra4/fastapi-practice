from enum import Enum

from pydantic import BaseModel, Field


class Difficulty(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"


class QuestionRequest(BaseModel):
    question: str = Field(
        min_length=1,
        max_length=1000
    )
    difficulty: Difficulty