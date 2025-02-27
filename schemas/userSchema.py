from pydantic import BaseModel, EmailStr

class userSchema(BaseModel):
    Username: str
    email: EmailStr
    password: str

class userPublic(BaseModel):
    Username: str
    email: EmailStr