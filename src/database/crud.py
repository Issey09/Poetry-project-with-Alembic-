from sqlalchemy.orm import Session

from src.database.models import Users
from src.schems.schemas import User


def create_user(db: Session, user: User):
    db_user = Users(nickname=user.nickname, password=user.password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

def show_user(db: Session, user_id: int):
    a = db.query(Users).filter(Users.id == user_id).first()
    if a is None:
        return "skibidi"
