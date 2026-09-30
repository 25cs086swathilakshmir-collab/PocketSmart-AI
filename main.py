import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

app = FastAPI()

# Serve CSS and other static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Frontend
@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as file:
        return file.read()


# Test Gemini
@app.get("/test-gemini")
def test_gemini():
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Say hello to PocketSmart AI in one short sentence."
    )

    return {"gemini_response": response.text}
from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    category: str
    budget: float
    requirements: str


@app.post("/recommend")
def recommend(request: RecommendationRequest):

    prompt = f"""
    You are PocketSmart AI, a smart budget and recommendation assistant.

    Category: {request.category}
    Budget: ₹{request.budget}
    Requirements: {request.requirements}

    Give practical recommendations that fit within the user's budget.
    Include suggested items, approximate costs, and a simple budget breakdown.
    Keep the answer clear and easy to understand.
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return {
        "recommendation": response.text
    }