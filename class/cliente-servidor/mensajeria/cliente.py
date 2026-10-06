import socket
import threading

HOST = "127.0.0.1"
PORT = 8000


def recibir_mensajes(conexion):
    while True:
        try:
            datos = conexion.recv(1024)

            if not datos:
                print("\nServidor desconectado")
                break

            print(f"\nMensaje: {datos.decode()}")
            print("> ", end="", flush=True)

        except ConnectionResetError:
            print("\nConexión cerrada por el servidor")
            break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))

    print("Conectado al servidor")
    print("Escribe mensajes. Usa '0' para terminar.")

    hilo = threading.Thread(target=recibir_mensajes, args=(cliente,), daemon=True)

    hilo.start()

    while True:
        mensaje = input("> ")

        if mensaje.lower() == "0":
            break

        cliente.sendall(mensaje.encode())
