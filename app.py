from fastapi import FastAPI, Request
from pydantic import BaseModel
from producer.producer import send_otp_event

app = FastAPI()


class OTPRequest(BaseModel):
    rider_id: str
    customer_id: str


@app.post("/send")
async def send_otp(data: OTPRequest):
    send_otp_event(data.rider_id, data.customer_id)
    return {"status": "sent"}
