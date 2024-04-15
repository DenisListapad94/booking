from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, PositiveInt, Field

app = FastAPI()


class User(BaseModel):
    item_id: PositiveInt
    age: int = Field(default=1, gt=0, lt=120)
    name: str = "User"
    surname: str = "Userskiy"
    email: EmailStr = "user@example.com"


@app.get("/items/{item_id}/{name}")
def get_path_params(item_id: int, name: str, ) -> dict:  # Эндпоинт, вьюшка, ручка
    return {
        "item_id": item_id,
        "name": name
    }


@app.get("/items")
def get_query_params(item_id: int, name: str, ) -> dict:
    return {
        "item_id": item_id,
        "name": name
    }


@app.get("/items/{item_id}")
def get_query_path_params(item_id: int, name: str) -> dict:
    return {
        "item_id": item_id,
        "name": name
    }


@app.post("/users",response_model=User)
def get_user() -> User:
    user_db = {
        "item_id": 1,
        "age": 24,
        "name": "User",
        "surname": "Userskiy",
        "email": "user@example.com"
    }
    user = User(**user_db)
    return user
