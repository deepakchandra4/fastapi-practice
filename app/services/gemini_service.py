from google import genai

from app.config.settings import settings


client = genai.Client(
    api_key=settings.gemini_api_key
)


def generate_response(prompt: str) -> str:

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text