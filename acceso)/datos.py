from conexion import conectar

try:

    conexion=conectar()

    with conexion.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario(
        id INT AUTO_INCREMENT PRIMARY KEY ,
        nombre VARCHAR (200)                
                       )


        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS documento(
        id INT AUTO_INCREMENT PRIMARY KEY ,
        tipo VARCHAR (200),
        id_usuario INT UNIQUE,
        FOREIGN KEY (id_usuario) REFERENCES usuario(id)
                    )
        """)

        cursor.execute("INSERT INTO usuario (nombre) VALUES (%s)",("robert") )
        id_usuario=cursor.lastrowid
        cursor.execute("INSERT INTO documento (tipo,id_usuario) VALUES (%s,%s)",("informe medico",id_usuario) )
        conexion.commit()

        cursor.execute("""
        SELECT u.nombre
        FROM usuario u
        LEFT JOIN documento d ON d.id_usuario = u.id
        WHERE d.tipo = "informe medico";
            
""")
        resultado=cursor.fetchall()
        for filas in resultado:
            print(filas)
except Exception as e:
    print("error", e)

finally:
    if 'conexion' in locals():
        conexion.close()