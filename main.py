from fastapi import FastAPI, Request, HTTPException
from agent import solve_quiz
from pydantic import BaseModel
import os

app = FastAPI()

SECRET = os.getenv("SECRET", "my_secret")  # Set in .env

class QuizRequest(BaseModel):
    email: str
    secret: str
    url: str

@app.post("/solve")
async def solve(request: QuizRequest):
    if request.secret != SECRET:
        raise HTTPException(status_code=403, detail="Forbidden")
    try:
        answer = solve_quiz(request.url)
        return {"email": request.email, "url": request.url, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
