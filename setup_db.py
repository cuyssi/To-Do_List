import os
import pg8000
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))

try:
    # Conexión temporal a la base 'postgres' para poder crear la nueva
    conn = pg8000.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database="postgres"  # conectamos primero a la base 'postgres'
    )
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}';")
    exists = cursor.fetchone()

    if not exists:
        cursor.execute(f"CREATE DATABASE {DB_NAME};")
        print(f"✅ Base de datos '{DB_NAME}' creada con éxito.")
    else:
        print(f"⚠️ La base de datos '{DB_NAME}' ya existe.")

    cursor.close()
    conn.close()

except Exception as e:
    print("🚩 Error creando la base de datos:", e)