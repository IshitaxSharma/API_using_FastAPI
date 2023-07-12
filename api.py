from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Create a model for the mail data
class Mail(BaseModel):
    sender: str
    recipients: List[str]
    subject: str
    body: str

# Define a route to send mail
@app.post("/send-mail/")
def send_mail(mail: Mail):
    # Your code to send the mail goes here
    # You can use libraries like smtplib or third-party APIs
    
    return {"message": "Mail sent successfully"}

# Run the API server with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
