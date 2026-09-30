# PocketSmart AI

## Your Smart Budget & Recommendation Assistant

PocketSmart AI is a Generative AI-based web application that helps users plan their budgets and receive personalized recommendations.

### Features

- 🏠 Home Interior Planning
- 🎉 Party Budget Planning
- 💎 Jewelry Recommendations
- 💰 Budget-based recommendations
- 🤖 AI-powered suggestions using Google Gemini

### Technologies Used

- HTML
- CSS
- JavaScript
- Python
- FastAPI
- Google Gemini API
- Pydantic
- Uvicorn

### How It Works

1. Select a category.
2. Enter your budget.
3. Enter your requirements.
4. PocketSmart AI sends the details to the backend.
5. Gemini generates personalized recommendations.
6. The recommendations are displayed to the user.

### Project Structure

```text
PocketSmart-AI/
├── main.py
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
Note
The Gemini API key is stored securely in a .env file and is not included in this repository.
