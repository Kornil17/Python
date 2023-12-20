import socket

host =  ('localhost', 8888)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(host)
s.listen()

print('I am listening connection...')

while 1:
    client, addr = s.accept()
    print(f"Connected client - {client} with address - {addr}")
    data = client.recv(8)
    while data:
        print(data)
        data = client.recv(8)
    print(f"All data is {data}")
    client.close()