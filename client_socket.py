import socket


HOST = (socket.gethostname(), 7777)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(HOST)
print(f"Connected to host - {HOST}")

msg = client.recv(1024)
print(msg.decode('utf8'))