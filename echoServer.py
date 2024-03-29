# -*- coding: utf-8 -*-
"""
Servidor eco (echo).

un sencillo servidor que devuelve lo que recibe
para ir conociendo como funcionan los sockets.
"""

# Import de módulos de la biblioteca estándar
import socket

# Constantes globales
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


# Código principal
if __name__ == "__main__":
    with socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by',
                  addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
