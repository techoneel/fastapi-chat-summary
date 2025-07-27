from fastapi import FastAPI, Request
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    chat = data.get("chat", "")
    prompt = (
        "Summarize the following customer chat and "
        "suggest a next action:\n\n" + chat
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"summary": response.choices[0].message["content"]}
