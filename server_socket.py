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
    res = 'Hello new connect'.encode('utf8')
    conn.send(res)