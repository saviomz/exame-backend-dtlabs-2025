import psycopg2
from passlib.context import CryptContext
from psycopg2 import sql

class AuthController:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    
    def verify_password(self, plain_password, stored_password):
        return plain_password == stored_password

    
    def authenticate_user(self, username: str, password: str):

        conn = psycopg2.connect(
            dbname="DBdesafio",
            user="postgres",
            password="5575",
            host="localhost", 
            port="5432"
        )
        
        cur = conn.cursor()

        # Consulta para buscar o usuário
        query = sql.SQL("SELECT username, password_hash FROM usuarios WHERE username = %s")
        cur.execute(query, (username,))

        user = cur.fetchone()
        
        cur.close()
        conn.close()

        # Verifica se o usuário existe e se a senha bate
        if not user or not self.verify_password(password, user[1]):
            return None
        return user[0]  # Retorna o nome de usuário autenticado
