import socket
import threading
import time
def recibir(cliente):       # Función para recibir y procesar los mensajes del cliente
    while True:
        try:
            mensaje = cliente.recv(1024).decode("utf-8")
            if mensaje.startswith("/cuenta"):
                segundos = int(mensaje.split()[1])
                for i in range(segundos, 0, -1):
                    print(f"Cuenta atrás: {i}")
                    time.sleep(1)
                print("¡Tiempo terminado!")
            else:
                print(f"Cliente: {mensaje}")
        except:
            print("Conexión cerrada.")
            break
def main():   # Función principal para iniciar el chat   
    host = "0.0.0.0"  # Host para conectar al cliente  # Aquí puede usar su IP pública o "localhost" para conectar al mismo host en la misma red local.  # Por
    puerto = 9001
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, puerto))
    servidor.listen(1)
    print(f"[SERVIDOR] Esperando conexión en {host}:{puerto}...")
    cliente, addr = servidor.accept()
    print(f"[SERVIDOR] Conectado con {addr}")
    threading.Thread(target=recibir, args=(cliente,), daemon=True).start()
    while True:
        msg = input()
        if msg.lower() == "salir":
                break
        cliente.sendall(msg.encode("utf-8"))
    cliente.close()
    servidor.close()
if __name__ == "__main__":
 main()