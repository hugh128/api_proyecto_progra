from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DB_DRIVER = os.getenv('DB_DRIVER')
    DB_SERVER = os.getenv('DB_SERVER')
    DB_DATABASE = os.getenv('DB_DATABASE')
    DB_UID = os.getenv('DB_UID')
    DB_PWD = os.getenv('DB_PWD')
