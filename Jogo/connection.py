import socket

class Bluetooth:
    def __init__(self, addr='3c:71:bf:52:c8:d6', port=1):
        self.addr = addr
        self.port = port
        self.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.socket.connect((self.addr, self.port))

    def send(self, code):
        self.socket.sendall(bytes(code, 'utf-8'))
