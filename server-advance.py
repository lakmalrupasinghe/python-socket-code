#server code

import socket
import threading

#address information
PORT = 8092
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNET_MSG  = " GOTDISCONNET"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#purpose of the fucntion is to serve multiple clients
def incoming_clients (conn, addr):
    print(" Client {addr} Connected ")

    condition = True
    while condition:
        length_msg = conn.recv(1024).decode(FORMAT)
        if length_msg:
            length_msg = int (length_msg)
            message = conn.recv(length_msg).decode(FORMAT)
            if message == DISCONNET_MSG:
                condition = False
            print ("{addr} {message}")
            conn.send("Msg Received Loud and Clear".encode(FORMAT))

    conn.close()


#the fucntion is to handle the server end
def setupServer():
    server.listen()  #listning funciton
    print (" SLIIT Echo server is now listning : ")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread (target= incoming_clients , args=(conn, addr))
        thread.start()
        print ("[Incoming Connections] {threading.activeCount() - 1}")


print("[Evil Server] is starting .....")
setupServer()









#print (socket.gethostbyname(socket.gethostname()))


