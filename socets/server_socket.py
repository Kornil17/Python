import pickle
import socket

HOST = (socket.gethostname(), 7777)
print(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(HOST)

s.listen()
print('I am listening connection...')

while True:
    conn, address = s.accept()
    print(f"Connected - {address}")
    # res = 'Hello new connect'.encode('utf8')
    # conn.send(res)
    print('Waiting for request')
    d = {"test":"abc", "res":"resr"}
    conn.send(pickle.dumps(d))
    # req = ''
    # while True:
    #     data = conn.recv(4096)
    #     if not len(data):
    #         break
    #     req += data.decode('utf8')
    # print(req)

    conn.close()