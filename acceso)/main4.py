import pymysql

try:
    conexion=pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        db='practica'
    )
    print("conexion exitosa")
    with conexion.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS biografia(
            id INT AUTO_INCREMENT PRIMARY KEY,
            fechaN DATE, 
            lugarN VARCHAR (200)           
                       )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS autor(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR (200),
            nacionalidad VARCHAR (200),
            bio_id INT UNIQUE,
            FOREIGN KEY (bio_id) REFERENCES biografia(id)      
                    )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS libro(
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(200),
            genero VARCHAR(200),
            autor_id INT,
            FOREIGN KEY (autor_id) REFERENCES autor(id)            
                       )

        """)
        #
        cursor.execute("""
        SELECT a.nombre 
        FROM autor a
        LEFT JOIN libro l ON l.autor_id = a.id
        WHERE l.id IS NULL; 

        """)
        print("nombre de los autores sin nombre")
        resultado=cursor.fetchall()
        for filas in resultado:
            print(filas)
        cursor.execute("""
        SELECT a.nombre, b.lugarN
        FROM  biografia b
        JOIN autor a ON a.bio_id = b.id
        WHERE a.nacionalidad = "argentina"
""")
        print("nacionalidad argentina")
        resultado=cursor.fetchall()
        for filas in resultado:
            print(filas)
        cursor.execute("""
        SELECT l.titulo , l.genero
        FROM libro l
        JOIN autor a ON l.autor_id= a.id
        JOIN biografia b ON  a.bio_id= b.id
        WHERE b.fechaN < '1970/01/08'

        """)
        print("nacimiento antes de 1970")
        resultado=cursor.fetchall()
        for filas in resultado:
            print(filas)

        
except Exception as e:
    print("error",e)
finally :
    if 'conexion' in locals():
        conexion.close()
        print("conexion cerrada")
