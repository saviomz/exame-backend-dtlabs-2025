# main.py
from fastapi import FastAPI, Form, HTTPException, status
from dados import DADOS
from models.create_user import create_user
from schemas.userSchema import userSchema, userPublic
from Controller.auth import LoginRequest
from Controller.AuthController import AuthController


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "API funcionando!"}

@app.get("/dados")
def get_dados():
    return DADOS



@app.post("/login")
async def login(data: LoginRequest):
    auth_controller = AuthController()
    user = auth_controller.authenticate_user(data.username, data.password)
    
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"message": f"User {user} authenticated"}


@app.post("/users/", status_code=201, response_model=userPublic)
def create_user_route(user: userSchema):  
    return create_user(user)