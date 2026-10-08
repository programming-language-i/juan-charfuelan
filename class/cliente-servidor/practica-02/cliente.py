import socket

HOST = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.sendto("ana".encode("utf-8"), (HOST, PORT))
