from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
         id=uuid4(),
         first_name="Witold",
         last_name="Shout",
         gender=Gender.male,
         roles=[Role.admin, Role.user]
         ),
    User(
         id=uuid4(),
         first_name="Alex",
         last_name="Maciano",
         gender=Gender.male,
         roles=[Role.student]
         )
]


@app.get("/")
async def root():
    return {"Hello": "Witold"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_users(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} doesn't exists"
        )
