from sqlalchemy import Column, Integer, String, DateTime, func

from src.database.database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    nickname = Column(String, index=True)
    password = Column(String, index=True)
    email = Column(String, index=True)
    create_at = Column(DateTime, default=func.now())
