import pyodbc
import os 
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    conn = pyodbc.connect(
        f"DRIVER={os.getenv('DB_DRIVER')};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        f"PORT={os.getenv('DB_PORT')};"
    )

    return conn