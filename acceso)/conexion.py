import pymysql

def conectar():
    return pymysql.connect(
        host="localhost",
        user="root",
        passwd="1234",
        db="practica"
    )