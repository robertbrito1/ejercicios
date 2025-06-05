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
            CREATE TABLE IF NOT EXISTS sede (
            id INT AUTO_INCREMENT PRIMARY KEY,
            direccion VARCHAR (200),
            capacidad INT
            )
            """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS curador(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(200),
            numeroEmpleado VARCHAR(200),
            sede_id INT UNIQUE,
            FOREIGN KEY (sede_id) REFERENCES sede(id)
            )
            
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS  exposicion (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(200),
            descripcion VARCHAR(200),
            curador_id INT,
            FOREIGN KEY (curador_id) REFERENCES curador(id)
                       )
        """)
       
       

        cursor.execute("INSERT INTO sede (direccion,capacidad) VALUES (%s,%s)", ('av maric15',1000))
        sede_id= cursor.lastrowid
        cursor.execute('INSERT INTO curador (nombre,numeroEmpleado,sede_id) VALUES (%s,%s,%s)', ('juan','3',sede_id))
        curador_id=cursor.lastrowid
        cursor.execute('INSERT INTO exposicion (titulo,descripcion,curador_id) VALUES (%s,%s,%s)',(',ago','tecnologia',curador_id))
        conexion.commit()
        print("Datos insertados correctamente")
        cursor.execute("""
        SELECT c.nombre
        FROM curador c
        LEFT JOIN exposicion e ON c.id = e.curador_id
        WHERE e.id IS NULL;
                       """)
        print("curadores sin exposiciones ")
        resultados= cursor.fetchall()
        for fila in resultados:
            print(fila)
        cursor.execute("""
        SELECT e.titulo, e.descripcion
        FROM exposicion e
        JOIN curador c ON e.curador_id = c.id
        JOIN sede s ON c.sede_id = s.id
        WHERE s.capacidad > 500;


        """)
        print("sedes mayores a 500 con exposicion")
        resultados=cursor.fetchall()
        for fila in resultados:
            print(fila)
        cursor.execute("""
        SELECT c.nombre , s.direccion
        FROM curador c 
        JOIN sede s ON c.sede_id = s.id
        WHERE s.capacidad < 200 
        """)
        print ("sede con capacidad menor a 100 ")
        resultados=cursor.fetchall()
        for fila in resultados:
            print(fila )
except Exception as e:
    print("error",e)
finally:
    if 'conexion' in locals():
        conexion.close
        print("conexion cerrada ")