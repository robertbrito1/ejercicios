from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import threading
import time
import uuid

# Diccionario global para guardar el estado de las tareas
tareas = {}

# Función que simula a un animal comiendo
def comer(especie, nombre, tiempo, tarea_id):
    for i in range(1, 4):
        print(f"El {especie} {nombre} está comiendo. Número: {i}")
        time.sleep(tiempo)
    # Cuando termina, actualizamos el estado de la tarea
    tareas[tarea_id]['estado'] = 'finalizado'

# Clase que maneja las peticiones HTTP
class ServidorHTTPRequestHandler(BaseHTTPRequestHandler):

    # Manejo de peticiones GET
    def do_GET(self):
        # Parsear la URL
        url = urlparse(self.path)
        params = parse_qs(url.query)

        if url.path == '/comer':
            # Obtener parámetros
            especie = params.get('especie', [None])[0]
            nombre = params.get('nombre', [None])[0]
            tiempo = params.get('tiempo', [None])[0]

            # Validar que los parámetros estén completos
            if None in (especie, nombre, tiempo):
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Faltan parametros: especie, nombre o tiempo")
                return

            try:
                tiempo = int(tiempo)
            except ValueError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"El parametro 'tiempo' debe ser un numero")
                return

            # Crear un ID único para la tarea
            tarea_id = str(uuid.uuid4())
            tareas[tarea_id] = {'estado': 'en_proceso'}

            # Crear y lanzar el hilo
            hilo = threading.Thread(target=comer, args=(especie, nombre, tiempo, tarea_id))
            hilo.start()

            # Devolver el ID al cliente
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"Tarea iniciada para el {especie} {nombre} con ID: {tarea_id}".encode())

        elif url.path == '/estado':
            # Obtener el ID de la tarea
            tarea_id = params.get('id', [None])[0]

            if not tarea_id or tarea_id not in tareas:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"ID de tarea no encontrado")
                return

            # Ver el estado de la tarea
            estado = tareas[tarea_id]['estado']
            mensaje = f"La tarea con ID {tarea_id} esta {estado}"
            self.send_response(200)
            self.end_headers()
            self.wfile.write(mensaje.encode())

        else:
            # Si no es una ruta válida
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Ruta no valida")

# Función para iniciar el servidor
def iniciar_servidor(puerto=8000):
    servidor = HTTPServer(('localhost', puerto), ServidorHTTPRequestHandler)
    print(f"Servidor HTTP corriendo en http://localhost:{puerto}")
    servidor.serve_forever()

# Iniciar el servidor
if __name__ == '__main__':
    iniciar_servidor()
