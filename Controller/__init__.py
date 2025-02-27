# auth_controller.py

from sqlalchemy.orm import Session
import modelsDB  # Importando os modelos do banco

class AuthController:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def autenticar(self):
        # Consultar o banco de dados para buscar o usuário
        user = self.db.query(modelsDB.User).filter(modelsDB.User.username == self.username).first()
        
        if user(self.password, user.password):
            # Se o usuário for encontrado e a senha for válida
            return True
        return False
