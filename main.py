import os
from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

# Health check (stops Render "/" 404)
@app.get("/")
def home():
    return {"status": "running"}

# Twilio WhatsApp webhook
@app.post("/webhook", response_class=PlainTextResponse)
async def whatsapp_webhook(
    Body: str = Form(default=""),
    From: str = Form(default=""),
):
    reply_text = f"Hi! You said: {Body}"

    twiml = MessagingResponse()
    twiml.message(reply_text)
    return str(twiml)