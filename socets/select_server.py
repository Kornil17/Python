import socket
import select
from typing import Union

HEADER_LENGTH = 10

HOST = ('localhost', 7777)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(HOST)

s.listen()

print('I am listening connection...')
socket_lists = [s]
client_lists = {}

def recieve_msg(client: socket.socket)->Union[dict, bool]:
    try:
        msg_header = client.recv(HEADER_LENGTH)
        if not len(msg_header):
            return False
        msg_length = int(msg_header.decode('utf8').strip())
        return {
            'header':msg_header,
            'data': client.recv(msg_header).decode('utf8'),
        }
    except:
        return False

while 1:
    re, _, el = select.select(socket_lists, [], socket_lists)
    for ss in re:
        if ss == s:
            client, addr = s.accept()
            user = recieve_msg(client)
            if not user:
                continue
            socket_lists.append(client)
            client_lists[client] = user
        else:
            msg = recieve_msg(ss)
            if msg:
                print(f'Connection from interpreted')
                socket_lists.remove(ss)
                del client_lists[ss]
                continue
            user = client_lists[ss]


        for ss in el:
            socket_lists.remove(ss)
            del client_lists[ss]
