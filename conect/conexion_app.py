import os
from psycopg2 import pool
import urllib.parse as urlparse
from dotenv import load_dotenv

load_dotenv()

# Validar que la variable exista
url_str = os.getenv("DATABASE_URL")
if not url_str:
    raise ValueError("DATABASE_URL no está definida en el entorno")

# Parsear la URL
url = urlparse.urlparse(url_str)

db_config = {
    "dbname": url.path[1:],
    "user": url.username,
    "password": url.password,
    "host": url.hostname,
    "port": url.port
}

# Crear pool de conexiones
conecction_pool = pool.ThreadedConnectionPool(
    minconn=1,
    maxconn=10,
    **db_config
)

def get_connection():
    return conecction_pool.getconn()

def put_connection(conn):
    conecction_pool.putconn(conn)

def close_all_connections():
    conecction_pool.closeall()
