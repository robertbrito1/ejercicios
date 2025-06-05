import socket
import threading
import time
def recibir(sock):  # Función para recibir datos del socket
 while True:
    try:
        mensaje = sock.recv(1024).decode("utf-8")
        if mensaje.startswith("/cuenta"):
            segundos = int(mensaje.split()[1])
            for i in range(segundos, 0, -1):
                print(f"Cuenta atrás: {i}")
                time.sleep(1)
            print("¡Tiempo terminado!")
        else:
            print(f"Servidor: {mensaje}")
    except:
        print("Conexión cerrada.")
        break
def main():
    host = "127.0.0.1" # Cambia por la IP del servidor si estás en red
    puerto = 9001
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, puerto))
    print(f"[CLIENTE] Conectado a {host}:{puerto}")
    threading.Thread(target=recibir, args=(cliente,), daemon=True).start()
    while True:
        msg = input()
        if msg.lower() == "salir":
            break
        cliente.sendall(msg.encode("utf-8"))
    cliente.close()
if __name__ == "__main__":
 main()