from Controller.AuthController import AuthController  
from typing import List, Dict


auth_controller = AuthController()

# Function to fetch data from servers
def get_dados_do_banco() -> List[Dict]:
    try:
        with auth_controller.conn.cursor() as cursor:
            # Perform SELECT on the database
            cursor.execute("""
                SELECT server_id, server_ulid, timestamp, sensor_type, value, unit 
                FROM sensores;
            """)

            dados = cursor.fetchall()

            dados_formatados = [
                {
                    "server_id": row[0],
                    "server_ulid": row[1],
                    "timestamp": row[2].isoformat(),  
                    "sensor_type": row[3],
                    "value": row[4],
                    "unit": row[5]
                }
                for row in dados
            ]

            return dados_formatados
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return []
