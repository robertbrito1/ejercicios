import sqlite3
from sqlite3 import Error
from conexion import crear_conexion
import sqlite3
from sqlite3 import Error



# Función para insertar datos en la tabla Investigadores
def insertar_investigadores(conn):
    try:
        # Insertar datos en la tabla Investigadores
        insertar_investigadores_sql = '''
        INSERT INTO Investigadores (nombre, identificacionInstitucional)
        VALUES
        ('Juan Pérez', 'INV12345'),
        ('María González', 'INV67890'),
        ('Carlos Rodríguez', 'INV11223');
        '''
        conn.execute(insertar_investigadores_sql)
        print("Datos de investigadores insertados correctamente.")
    except Error as e:
        print(f"Error al insertar datos en la tabla 'Investigadores': {e}")

# Función para insertar datos en la tabla EstacionesMonitoreo
def insertar_estaciones_monitoreo(conn):
    try:
        # Insertar datos en la tabla EstacionesMonitoreo
        insertar_estaciones_monitoreo_sql = '''
        INSERT INTO EstacionesMonitoreo (coordenadas, nivelActividad, investigador_id)
        VALUES
        ('40.7128° N, 74.0060° W', 5, 1),  -- Asignando al Investigador 1
        ('34.0522° N, 118.2437° W', 3, 2),  -- Asignando al Investigador 2
        ('51.5074° N, 0.1278° W', 7, 3);    -- Asignando al Investigador 3
        '''
        conn.execute(insertar_estaciones_monitoreo_sql)
        print("Datos de estaciones de monitoreo insertados correctamente.")
    except Error as e:
        print(f"Error al insertar datos en la tabla 'EstacionesMonitoreo': {e}")

# Función para insertar datos en la tabla Experimentos
def insertar_experimentos(conn):
    try:
        # Insertar datos en la tabla Experimentos
        insertar_experimentos_sql = '''
        INSERT INTO Experimentos (nombreExperimento, resultado, investigador_id)
        VALUES
        ('Experimento A', 'Éxito', 1),  -- Asignado al Investigador 1
        ('Experimento B', 'Fracaso', 2),  -- Asignado al Investigador 2
        ('Experimento C', 'Éxito', 3);    -- Asignado al Investigador 3
        '''
        conn.execute(insertar_experimentos_sql)
        print("Datos de experimentos insertados correctamente.")
    except Error as e:
        print(f"Error al insertar datos en la tabla 'Experimentos': {e}")

# Función principal para insertar los datos
def insertar_datos(conn):
    insertar_investigadores(conn)
    insertar_estaciones_monitoreo(conn)
    insertar_experimentos(conn)

# Establecer la conexión
conn = crear_conexion()

# Si la conexión fue exitosa, insertar los datos
if conn:
    insertar_datos(conn)
    conn.commit()  # Confirmar las inserciones en la base de datos
    print("Datos insertados y confirmados en la base de datos.")
    
    # Cerrar la conexión después de la operación
    conn.close()
    print("Conexión cerrada correctamente.")
else:
    print("No se pudo establecer conexión a la base de datos.")
