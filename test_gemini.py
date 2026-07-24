from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
# for model in client.models.list():
#     print(model.name)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain what an API is in simple language."
)

print(response.text)