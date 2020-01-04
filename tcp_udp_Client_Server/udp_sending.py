import socket
import time

print("starting UDP communication with .....")


UDP_IP = "192.168.1.177"
UDP_PORT = 8888
MESSAGE = "set peripheral HIGH"


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((UDP_IP, UDP_PORT))
s.send(MESSAGE.encode())

def My_receive():
    msg = ""
    while True:
        try:
            temp = s.recv(1024)
            msg = temp.decode()
        except socket.timeout:
            break
        return msg

response = My_receive()
if (not response.strip()):
    print("no response")
else:
    print(response)


s.close()

