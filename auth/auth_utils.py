import jwt
import datetime
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2AuthorizationCodeBearer


SECRET_KEY = "SEGREDO_SEGREDO"
ALGORITHM = "HS256"
TOKEN_EXPIRATION_MINUTES = 15


oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="/login", authorizationUrl="/authorize")



def create_jwt_token(data: dict):

    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
    to_encode.update ({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_jwt_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return username  # Retorna o nome de usuário autenticado
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")


