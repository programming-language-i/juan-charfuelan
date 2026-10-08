import socket
import threading

HOST = "127.0.0.1"
PORT = 8000

clientes = []
lock = threading.Lock()


def enviar_mensaje(mensaje, cliente_actual=None):
    with lock:
        for cliente in clientes:
            if cliente != cliente_actual:
                try:
                    cliente.sendall(mensaje)
                except OSError:
                    print("Error")


def atender_cliente(conexion, direccion):
    print(f"[+] Cliente conectado: {direccion}")

    with lock:
        clientes.append(conexion)

    try:
        while True:
            datos = conexion.recv(1024)

            if not datos:
                break
            print(f"[{direccion}] {datos.decode()}")

            enviar_mensaje(datos, conexion)

    except ConnectionResetError:
        print(f"[!] Desconexion inesperada de clinete: {direccion}")

    finally:
        with lock:
            if conexion in clientes:
                clientes.remove(conexion)
        conexion.close()

        print(f"Cliente desconectado: {direccion}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"Servidor escuchando en {HOST}:{PORT}")

    while True:
        conexion, direccion = servidor.accept()
        hilo = threading.Thread(target=atender_cliente, args=(conexion, direccion))

        hilo.start()
