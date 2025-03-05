from http import HTTPStatus
from schemas.userSchema import userSchema

def create_user(User: userSchema):
    return User  