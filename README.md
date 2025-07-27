# fastapi-chat-summary

A simple FastAPI micro-agent using OpenAI to summarize chats and suggest next actions.

## Setup

```bash
git clone https://github.com/techoneel/fastapi-chat-summary.git
cd fastapi-chat-summary
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
uvicorn main:app --reload
