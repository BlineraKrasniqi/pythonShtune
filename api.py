from fastapi import FastAPI
from pydanyc import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age:int
    email: str

@app.post("/users/")
async def create_user(user: User):
    return user