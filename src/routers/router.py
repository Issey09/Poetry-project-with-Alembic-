from fastapi import APIRouter, Depends
from typing import Annotated

from sqlalchemy.orm import Session

from src.database.crud import create_user, show_user
from src.database.database import SessionLocal
from src.schems.schemas import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users/")
async def get_users(db: Annotated[Session, Depends(get_db)],user: Annotated[User, Depends()]):
    create_user(db,user=user)
    return "User registred successfully!"

@router.get("/get_users/")
async def get_users(db: Annotated[Session, Depends(get_db)], user_id: int):
    b = show_user(db, user_id=user_id)
    return b