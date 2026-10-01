import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect(("127.0.0.1", 8000))
    print("mi extremo", cliente.getsockname())
    print("el servidor:", cliente.getpeername())
    cliente.sendall("mensaje a servidor".encode("utf-8"))
    print("respuesta:", cliente.recv(1024).decode("utf-8"))

