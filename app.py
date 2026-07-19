import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Gemini configurations
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

app = FastAPI(
    title="Thanuja.k AI Chat Assistant API",
    description="Live AI Chat Model powered by Gemini & FastAPI",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    user_message: str

class ChatResponse(BaseModel):
    user_query: str
    ai_response: str
    status: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat_with_model(request: ChatRequest):
    if not request.user_message.strip():
        raise HTTPException(status_code=400, detail="Message empty-ah irukka koodathu!")
        
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(request.user_message)
        return ChatResponse(
            user_query=request.user_message,
            ai_response=response.text,
            status="Success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

