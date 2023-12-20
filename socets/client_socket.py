import pickle
import socket
import time

HOST = (socket.gethostname(), 7777)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(HOST)
print(f"Connected to host - {HOST}")

# msg = client.recv(1024)
# print(msg.decode('utf8'))
client.send(b'Hello!\n')
client.sendall(b'GET / HTTP/1.1\nHost:localhost:1000\n')
print('Sent msg')

res = client.recv(4096)
print(res)
print(pickle.loads(res))
