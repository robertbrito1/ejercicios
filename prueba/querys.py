import sqlite3
from sqlite3 import Error

from conexion import crear_conexion


def realizar_consultas(conn):
    try:
        cursor = conn.cursor()

        # Consulta 1: Mostrar los nombres de los investigadores y los nombres de sus experimentos
        print("\n1. Nombres de los investigadores y los nombres de sus experimentos:")
        cursor.execute('''
        SELECT Investigadores.nombre, Experimentos.nombreExperimento
        FROM Investigadores
        JOIN Experimentos ON Investigadores.id = Experimentos.investigador_id;
        ''')
        for row in cursor.fetchall():
            print(f"Investigador: {row[0]}, Experimento: {row[1]}")

        # Consulta 2: Mostrar el nombre e identificador de todos los investigadores con más de un experimento
        print("\n2. Investigadores con más de un experimento:")
        cursor.execute('''
        SELECT Investigadores.id, Investigadores.nombre
        FROM Investigadores
        JOIN Experimentos ON Investigadores.id = Experimentos.investigador_id
        GROUP BY Investigadores.id
        HAVING COUNT(Experimentos.id) > 1;
        ''')
        for row in cursor.fetchall():
            print(f"ID: {row[0]}, Investigador: {row[1]}")

        # Consulta 3: Mostrar las coordenadas GPS de la estación del investigador con id = 1
        print("\n3. Coordenadas GPS de la estación del investigador con ID = 1:")
        cursor.execute('''
        SELECT EstacionesMonitoreo.coordenadas
        FROM EstacionesMonitoreo
        WHERE EstacionesMonitoreo.investigador_id = 1;
        ''')
        row = cursor.fetchone()
        if row:
            print(f"Coordenadas GPS: {row[0]}")
        else:
            print("No se encontró la estación de monitoreo para el investigador con ID = 1.")

    except Error as e:
        print(f"Error al realizar las consultas: {e}")

# Establecer la conexión
conn = crear_conexion()

# Si la conexión fue exitosa, realizar las consultas
if conn:
    realizar_consultas(conn)
    conn.close()
    print("Conexión cerrada correctamente.")
else:
    print("No se pudo establecer conexión a la base de datos.")