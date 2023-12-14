# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(user: User):
    return {"message": f"Login successful for {user.username}"}

@app.post("/signup")
def signup(user: User):
    # Add signup logic (validate and store user data)
    return {"message": f"Signup successful for {user.username}"}