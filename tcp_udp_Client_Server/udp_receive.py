import socket
import time
import struct


print("wait UDP communication from ......")

LOCAL_IP = "192.168.1.100"
UDP_IP = "192.168.1.177"
UDP_PORT = 8888
LOCAL_PORT = 50007
MESSAGE = "set peripheral HIGH"

#______________________________________________________ 


#______________________________________________________ 

rx_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rx_s.bind((LOCAL_IP, LOCAL_PORT))

while True:
    data, addr = rx_s.recvfrom(1024)
    time.sleep(1)
    rx_msg = data.decode()
    rx_msg = rx_msg.strip()
    print(rx_msg)

rx_s.close()

