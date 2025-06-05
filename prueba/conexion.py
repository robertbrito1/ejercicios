import sqlite3
from sqlite3 import Error

# Función para crear la conexión a la base de datos
def crear_conexion():
    conn = None
    try:
        # Establecer el timeout a 10 segundos para evitar el "database is locked"
        conn = sqlite3.connect("db.db", timeout=10)
        print(f"Conexión exitosa. Versión de SQLite: {sqlite3.sqlite_version}")

    except Error as e:
        print(e)

    return conn

# Función para crear la tabla Investigadores
def crear_tabla_investigadores(conn):
    try:
        # Crear tabla Investigadores
        crear_investigadores_sql = '''
        CREATE TABLE IF NOT EXISTS Investigadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            identificacionInstitucional TEXT UNIQUE NOT NULL
        );
        '''
        # Ejecutar la consulta para crear la tabla
        print("Creando tabla Investigadores...")
        conn.execute(crear_investigadores_sql)
        print("Tabla 'Investigadores' creada o ya existe.")
    except Error as e:
        print(f"Error al crear la tabla 'Investigadores': {e}")

# Función para crear la tabla EstacionesMonitoreo
def crear_tabla_estaciones_monitoreo(conn):
    try:
        # Crear tabla EstacionesMonitoreo
        crear_estaciones_monitoreo_sql = '''
        CREATE TABLE IF NOT EXISTS EstacionesMonitoreo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            coordenadas TEXT NOT NULL,
            nivelActividad INTEGER NOT NULL,
            investigador_id INTEGER,
            FOREIGN KEY (investigador_id) REFERENCES Investigadores(id)
        );
        '''
        # Ejecutar la consulta para crear la tabla
        print("Creando tabla EstacionesMonitoreo...")
        conn.execute(crear_estaciones_monitoreo_sql)
        print("Tabla 'EstacionesMonitoreo' creada o ya existe.")
    except Error as e:
        print(f"Error al crear la tabla 'EstacionesMonitoreo': {e}")

# Función para crear la tabla Experimentos
def crear_tabla_experimentos(conn):
    try:
        # Crear tabla Experimentos
        crear_experimentos_sql = '''
        CREATE TABLE IF NOT EXISTS Experimentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombreExperimento TEXT NOT NULL,
            resultado TEXT NOT NULL,
            investigador_id INTEGER,
            FOREIGN KEY (investigador_id) REFERENCES Investigadores(id)
        );
        '''
        # Ejecutar la consulta para crear la tabla
        print("Creando tabla Experimentos...")
        conn.execute(crear_experimentos_sql)
        print("Tabla 'Experimentos' creada o ya existe.")
    except Error as e:
        print(f"Error al crear la tabla 'Experimentos': {e}")

# Función principal para crear las tablas
def crear_tablas(conn):
    crear_tabla_investigadores(conn)
    crear_tabla_estaciones_monitoreo(conn)
    crear_tabla_experimentos(conn)

# Establecer la conexión
conn = crear_conexion()

# Si la conexión fue exitosa, crear las tablas
if conn:
    crear_tablas(conn)

    # Cerrar la conexión después de la operación
    conn.close()
    print("Conexión cerrada correctamente.")
else:
    print("No se pudo establecer conexión a la base de datos.")
