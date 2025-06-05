import pymysql

try:
    conexion=pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='prueba'

    )
    print("conexion exitosa")
    with conexion.cursor() as cursor:

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS jugador(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(400)  ,
        apellido VARCHAR(400)        
                    )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipo(
        id INT AUTO_INCREMENT PRIMARY KEY,
        club VARCHAR(100),
        id_jugador INT,
        FOREIGN KEY (id_jugador) REFERENCES jugador(id)             
                       )
        

        """)

        cursor.execute("INSERT INTO jugador (nombre,apellido ) VALUES (%s,%s)",('juan','jose'))
        id_jugador=cursor.lastrowid
        cursor.execute("INSERT INTO equipo (club,id_jugador) VALUES (%s,%s)", ('madrid',id_jugador))
        conexion.commit()

        cursor.execute("""
            SELECT jugador.nombre, equipo.club
            FROM equipo
            JOIN jugador ON equipo.id_jugador = jugador.id
            """) 
        resultados = cursor.fetchall()
        for fila in resultados:
                print(fila)
except Exception as e:
    print("error",e)
finally:
    if 'conexion' in locals():
        conexion.close
        print("conexion cerrada")