import psycopg2
from passlib.context import CryptContext
from psycopg2 import sql
import os

class AuthController:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        # Create connection when starting a class
        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME", "DBdesafio"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "5575"),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432")
        )
        self.conn.autocommit = True  

    def hash_password(self, password: str) -> str:
        """ Gera o hash da senha """
        return self.pwd_context.hash(password)

    def insert_user(self, username: str, email: str, password: str):
        """ Insere um novo usuário no banco de dados """
        try:     #self.conn.cursor() opens a temporary cursor that allows commands in the database
            with self.conn.cursor() as cur:
                cur.execute("SELECT id FROM usuarios WHERE username = %s OR email = %s", (username, email))
                existing_user = cur.fetchone()

                if existing_user:
                    print("Usuário já cadastrado!")
                    return None

                hashed_password = self.hash_password(password)

                # Insert in Database
                query = sql.SQL("""
                    INSERT INTO usuarios (username, email, password_hash) 
                    VALUES (%s, %s, %s) RETURNING id
                """)
                cur.execute(query, (username, email, hashed_password))

                user_id = cur.fetchone()[0] # get the entered user ID

                print("Usuário cadastrado com sucesso!")
                return user_id

        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
            return None
        

    def authenticate_user(self, username: str, password: str):
        """ Autentica um usuário verificando o username e senha """
        try:
            with self.conn.cursor() as cur:
                # Query search for the user
                query = sql.SQL("SELECT username, password_hash FROM usuarios WHERE username = %s")
                cur.execute(query, (username,))
                user = cur.fetchone()

                #Checks if the user exists and if the password matches
                if not user or not self.verify_password(password, user[1]):
                    return None
                return user[0]  

        except Exception as e:
            print(f"Erro ao autenticar usuário: {e}")
            return None
        

    def verify_password(self, plain_password, stored_password):
        """ Verifica se a senha informada confere com a armazenada """
        return self.pwd_context.verify(plain_password, stored_password)

    def close_connection(self):
        """ Fecha a conexão ao encerrar a aplicação """
        if self.conn:
            self.conn.close()
            print("Conexão com o banco de dados encerrada.")
