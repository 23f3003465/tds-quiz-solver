from fastapi import FastAPI, Request
from solver.fetch import fetch_quiz
from solver.parse import parse_quiz
from solver.submit import submit_answer
import config

app = FastAPI()

@app.post("/")
async def solve_quiz(request: Request):
    try:
        data = await request.json()
    except:
        return {"status": "Invalid JSON"}, 400

    if data.get("secret") != config.STUDENT_SECRET:
        return {"status": "Forbidden"}, 403

    url = data.get("url")
    if not url:
        return {"status": "Missing URL"}, 400

    # Fetch, parse, submit
    quiz_content = await fetch_quiz(url)
    answer = await parse_quiz(quiz_content)
    result = await submit_answer(url, answer)
    return result
