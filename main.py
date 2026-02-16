from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

@app.post("/whatsapp")
async def whatsapp_reply(request: Request):
    form = await request.form()
    incoming_msg = form.get("Body", "").strip().lower()

    response = MessagingResponse()
    msg = response.message()

    if incoming_msg in ["hi", "hello"]:
        msg.body(
            "Welcome to Dr. Smile Dental Clinic 🦷\n\n"
            "How can we help you today?\n\n"
            "1️⃣ Book Appointment\n"
            "2️⃣ Clinic Timing\n"
            "3️⃣ Location\n"
            "4️⃣ Emergency Contact"
        )

    elif incoming_msg == "1":
        msg.body(
            "Please enter:\n"
            "• Your Full Name\n"
            "• Preferred Date (DD/MM)\n"
            "• Morning or Evening slot"
        )

    elif incoming_msg == "2":
        msg.body("Clinic Timing:\nMon–Sat\n10 AM – 12 PM\n4 PM – 7 PM")

    elif incoming_msg == "3":
        msg.body("Clinic Location:\nhttps://maps.google.com")

    elif incoming_msg == "4":
        msg.body("For emergencies call: 9876543210")

    else:
        msg.body(
            "Thank you! ✅\n"
            "Your appointment request has been received.\n"
            "Clinic staff will confirm shortly."
        )

    return PlainTextResponse(str(response))