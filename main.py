
from fastapi import FastAPI, Form, HTTPException, status
from dados import get_dados_do_banco
from typing import List, Dict
from Controller.auth import LoginRequest
from Controller.AuthController import AuthController
from auth.auth_utils import create_jwt_token


auth_controller = AuthController()
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "API funcionando!"}

@app.get("/dados", response_model=List[Dict])
def get_dados():
    dados = get_dados_do_banco()
    return dados


@app.post("/login")
async def login(login_request: LoginRequest):
    # Authenticate the user using the authenticate_user function in auth_controller
    username = auth_controller.authenticate_user(login_request.username, login_request.password)

    if not username:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    
    token_data = {"sub": username}  
    access_token = create_jwt_token(token_data)

    if not access_token:
        raise HTTPException(status_code=500, detail="Erro ao gerar o token")

    return {"access_token": access_token, "token_type": "bearer"}
    

@app.post("/register")
def register_user(username: str, email: str, password: str):
    user_id = auth_controller.insert_user(username, email, password)
    if user_id:
        return {"message": "Usuário cadastrado com sucesso!", "user_id": user_id}
    return {"error": "Usuário já existe ou erro ao cadastrar"}