from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Model for the mail data
class Mail(BaseModel):
    sender: str
    recipients: List[str]
    subject: str
    body: str

# Define to send mail
@app.post("/send-mail/")
def send_mail(mail: Mail):
    # 
    
    return {"message": "Mail sent successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
