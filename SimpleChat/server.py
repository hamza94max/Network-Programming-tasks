from _thread import start_new_thread
from thread import *
import threading
from socket import *
# The aim of the program is making a server working with more than 1 client in parallel
def client_thread(conn):
    receive = threading.thread(target=receive_thread, args=(conn,))
    receive.start()
    # Target means the function will run in parallel
    while True:
        conn.send(input("Enter").encode('utf-8'))
def receive_thread(conn):
    while True:
        x = conn.recv(500)
        print(x.decode('utf-8'))

s = socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 8000

s.bind((host, port))
s.listen(5)  # 5 mean if there are many requests ==> make a queue with size of 5 elements

while True:
    conn, address = s.accept()
    print("Connection from ", address[0])
    start_new_thread(client_thread, (conn,))
    # client_thread ==> function that will work in parallel in the new thread.
