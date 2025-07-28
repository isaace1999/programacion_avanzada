import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ofSfW94YaY1r1Zob",
        database="videojuegos"
    )
