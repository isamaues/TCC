import socket
from time import sleep

# Device specific information
#m5stick_addr = '5c:cd:5b:7e:0c:15'
addr = '3c:71:bf:52:c8:d6'
port = 1 # This needs to match M5Stick setting

# Establish connection and setup serial communication
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((addr, port))

# Send and receive data
while True:
    a = input()
    if a == 'quit': break
    s.sendall(b'B')
    # data = s.recv(1024)
    # print(data)

s.close()