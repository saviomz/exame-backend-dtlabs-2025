from http import HTTPStatus
from schemas.userSchema import userSchema

# Remova o decorador @app.post e a criação do app aqui
def create_user(user: userSchema):
    return user  # Ou lógica de criação no banco de dados