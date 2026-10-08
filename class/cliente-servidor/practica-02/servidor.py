import socket

HOST = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))
    print("UDP escuchando en", sock.getsockname())
    while True:
        datos, direccion = sock.recvfrom(1024)
        print(direccion, datos.decode("utf-8"))
