import pyodbc
from config import Config

conn_str = (
	f"DRIVER={Config.DB_DRIVER};"
	f"SERVER={Config.DB_SERVER};"
	f"DATABASE={Config.DB_DATABASE};"
	f"UID={Config.DB_UID};"
	f"PWD={Config.DB_PWD}"
)

def get_connection():
	try:
		conn = pyodbc.connect(conn_str)
		print("Conexion exitosa a la base de datos")
		return conn

	except pyodbc.Error as ex:
		print(f"Error de conexion: {ex}")
