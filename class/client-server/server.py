import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(("127.0.0.1", 8000))
    servidor.listen()
    print("escuchando en", servidor.getsockname())
    conexion, direccion = servidor.accept()
    with conexion:
        print("cliente desde", direccion)
        datos = conexion.recv(1024)
        print("recibido:", datos)
        conexion.sendall((datos.upper()))
