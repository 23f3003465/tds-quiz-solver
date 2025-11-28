import asyncio
import httpx
import config

async def test_demo():
    payload = {
        "email": config.STUDENT_EMAIL,
        "secret": config.STUDENT_SECRET,
        "url": "https://tds-llm-analysis.s-anand.net/demo"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post("http://127.0.0.1:8000/", json=payload, timeout=120)
        print(response.status_code)
        print(response.text)

asyncio.run(test_demo())
