
#!/usr/bin/env python3

import socket

IP = "127.0.0.1" #loopback 
PORT = 8092  # non-privileged ports  > 1023)
AMT_DATA = 64 

#socket () function

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    #connect ()
    mySocket.connect((IP,PORT))
    mySocket.sendall("Hello from SLIIT -->")
    data = mySocket.recv(AMT_DATA)
    print("Reveid with thanks: ", repr(data))
    mySocket.sendall("Hello 2 from SLIIT -->")
    data = mySocket.recv(AMT_DATA)
    print("Reveid with thanks: ", repr(data))
    mySocket.sendall("Hello 3 from SLIIT -->")
    data = mySocket.recv(AMT_DATA)
    print("Reveid with thanks: ", repr(data))