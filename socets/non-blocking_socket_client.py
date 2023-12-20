import socket

host =  ('localhost', 8888)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(host)
print(client.gettimeout())
client.setblocking(0)
# client.setblocking(1)
data = b'Hello World!'*1024*1024
sent = client.send(data)
print(sent, len(data))
