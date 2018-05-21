



from _socket import *
from datetime import datetime
import  _json


address = ('localhost', 7777)
max_size = 1024
print('Starting the client at', datetime.now())
client = socket(AF_INET, SOCK_STREAM)
client.connect(address)
mess = {

    "action": "presence",
    "time": 'unix timestamp',
    "type": "status",
    "user": {
            "account_name": "C0deMaver1ck",
            "status": "Yep, I am here!"
    }
}
mess_json = json.dump(mess)
client.sendall(mess_json)
message = client.recv(max_size)
print('At', datetime.now(), 'someone replied', message.decode('utf-8'))
client.close()