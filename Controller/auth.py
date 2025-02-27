# Modelo para o corpo da requisição de login
from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str