from fastapi import APIRouter

from src.auth.schemas.user_schema import User

router = APIRouter(
    prefix="/users",
    tags=["Auth"]
)


@router.post("", response_model=User)
def get_user() -> User:
    user_db = {
        "id": 1,
        "age": 24,
        "name": "User",
        "surname": "Userskiy",
        "email": "user@example.com"
    }
    user = User(**user_db)
    return user
