from pydantic import BaseModel, EmailStr

class User(BaseModel):
    nickname: str
    password: str
    email: EmailStr
