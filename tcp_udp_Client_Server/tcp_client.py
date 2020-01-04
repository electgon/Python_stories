import socket
import time
import struct


print("starting TCP communication with .....")


def My_receive():
    msg = ""
    while True:
        try:
            temp = s.recv(1024)
            msg = temp.decode()
        except socket.timeout:
            break
        return msg
	

LOCAL_IP = "192.168.1.100"
TCP_IP = "192.168.1.177"
TCP_PORT = 23
LOCAL_PORT = 50007
MESSAGE = "set peripheral  HIGH"


# # Start TCP Connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())


data = s.recv(1024)
rx_msg = data.decode()
rx_msg = rx_msg.strip()
print(rx_msg)


s.close()
