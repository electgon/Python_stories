import socket
import time
import struct


print("waiting TCP communication with .....")


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
MESSAGE = "set peripheral HIGH"


# # Start TCP Connection
rx_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rx_s.bind((LOCAL_IP, LOCAL_PORT))
rx_s.listen(1)


conn, addr = rx_s.accept()

print("connecting address:")
print(addr)


rx_s.close()
