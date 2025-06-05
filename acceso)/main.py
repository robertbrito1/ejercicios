import pymysql

try:
    # Conexión a la base de datos
    conexion = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='prueba'
    )
    print("✅ Conexión exitosa.")

    with conexion.cursor() as cursor:
        # Crear tabla usuarios
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100)
        )
        """)

        # Crear tabla ordenes con clave foránea
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ordenes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            usuario_id INT,
            producto VARCHAR(100),
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
        """)

        # Insertar un usuario
        cursor.execute("INSERT INTO usuarios (nombre) VALUES ('jose')")
        usuario_id = cursor.lastrowid

        # Insertar una orden para ese usuario
        cursor.execute("INSERT INTO ordenes (usuario_id, producto) VALUES (%s, %s)", (usuario_id, 'pasta'))

        # Confirmar los cambios
        conexion.commit()

        # Consultar órdenes con nombre del usuario
        cursor.execute("""
        SELECT usuarios.nombre, ordenes.producto
        FROM ordenes
        JOIN usuarios ON ordenes.usuario_id = usuarios.id
        """)
        for nombre, producto in cursor.fetchall():
            print(f"{nombre} pidió: {producto}")

except Exception as e:
    print("❌ Error al conectar o ejecutar:", e)

finally:
    if 'conexion' in locals():
        conexion.close()
        print("🔌 Conexión cerrada.")
