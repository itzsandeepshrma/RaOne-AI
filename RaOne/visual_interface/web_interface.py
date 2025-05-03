from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserMessage(BaseModel):
    message: str

@app.post("/api/chat")
def chat(msg: UserMessage):
    return {"response": f"RaOne (web): You said '{msg.message}'"}
