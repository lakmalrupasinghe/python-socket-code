#!/usr/bin/env python3

import socket

IP = "127.0.0.1" #loopback 
PORT = 8092  # non-privileged ports  > 1023)
AMT_DATA = 64 

#socket created socket()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    #bind the socket with proper IP and a port bind()
    mySocket.bind((IP, PORT))    #bind done

    #listning socket listen()
    mySocket.listen()

    # blocking mode  accept()
    conn, addr = mySocket.accept()

    with conn:
        print("Connected by: ", addr)
        while True:
            data = conn.recv(AMT_DATA)
            if not data:
                break
            conn.sendall(data) ##echo server

#send recv data