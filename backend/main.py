from fastapi import FastAPI
from schemas import ChatRequest
from model_loader import generate_response
from chat_service import get_chat_history, update_history

app = FastAPI(title="Mental Health Chatbot API")

SYSTEM_PROMPT = """
You are a compassionate mental health assistant.
Respond with empathy and supportive guidance.
"""

@app.post("/chat")

def chat(req: ChatRequest):
    #Endpoint used get chat 
    history = get_chat_history(req.session_id)

    prompt = SYSTEM_PROMPT + "\n"

    for h in history:
        prompt += f"User: {h['user']}\nAssistant: {h['bot']}\n"

    prompt += f"User: {req.message}\nAssistant:"

    response = generate_response(prompt)

    update_history(req.session_id, req.message, response)

    return {"response": response}