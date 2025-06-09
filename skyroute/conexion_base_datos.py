import mysql.connector 
from config import db_config

def obtener_conexion():
    return mysql.connector.connect(db_config)

def traer_clientes():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    conexion.close()
    return clientes