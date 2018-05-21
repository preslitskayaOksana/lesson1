
from _socket import *
from datetime import datetime

import json

address = ('localhost', 7777)
max_size = 1024
print('подключение', datetime.now())
print('ожидается запрос')
server = socket(AF_INET, SOCK_STREAM)
server.bind(address)
server.listen(5)
while True:
    client, addr = server.accept()
    message = client.recv(max_size)
    print(client.decode('utf-8'))
    m = 'как дела?'
    client.sendall(m.encode('utf-8'))
client.close()
server.close()