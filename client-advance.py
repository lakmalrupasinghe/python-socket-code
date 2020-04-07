import socket

HEADER = 64
PORT = 8098
SERVER = "192.168.8.101"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNET_MSG  = " GOTDISCONNET"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def Client_send(message):
    message = message.encode(FORMAT)
    length_msg = len(message)
    length_send = str(length_msg).encode(FORMAT)
    length_send += b' ' * (HEADER - len(length_send))
    client.send(length_send)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

Client_send("Hi SIIT People How are You ")
input()
Client_send("Hi HOW IS HACKING ")
input()
Client_send("Hi HOW IS LOCKEDDOWN ")

Client_send(DISCONNET_MSG)