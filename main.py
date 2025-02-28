
from fastapi import FastAPI, Form, HTTPException, status
from dados import DADOS
from models.create_user import create_user
from schemas.userSchema import userSchema, userPublic
from Controller.auth import LoginRequest
from Controller.AuthController import AuthController
from auth.auth_utils import create_jwt_token

app = FastAPI()
auth_controller = AuthController()

@app.get("/")
def read_root():
    return {"message": "API funcionando!"}

@app.get("/dados")
def get_dados():
    return DADOS



@app.post("/login")
async def login(login_request: LoginRequest):
    """
    Endpoint para autenticação e geração de token JWT.
    """
    # Autentica o usuário usando o AuthController
    username = auth_controller.authenticate_user(login_request.username, login_request.password)

    if not username:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    
    token_data = {"sub": username}  # "sub" é o assunto (subject) do token
    access_token = create_jwt_token(token_data)

    if not access_token:
        raise HTTPException(status_code=500, detail="Erro ao gerar o token")

    return {"access_token": access_token, "token_type": "bearer"}
    
@app.post("/users/", status_code=201, response_model=userPublic)
def create_user_route(user: userSchema):  
    return create_user(user)