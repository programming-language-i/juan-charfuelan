import socket

host_destino = "www.google.com"
puerto_destino = 80

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host_destino, puerto_destino))

cliente.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

resp = cliente.recv(4096)
print(resp.decode())
cliente.close()

