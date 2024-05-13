from socket import *
import threading

def receive_thread(s):
    while True:
        x = s.recv(500)
        print("Server: ", x.decode('utf-8'))

# Client code

s = socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 8000

s.connect((host, port))

receive = threading.Thread(target=receive_thread, args=(s,))
receive.start()

while True:
    s.send(input("client: ").encode('utf-8'))













