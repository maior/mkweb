from jsonparse import jsonparse
import socket

class network:
    def __init__(self, sock=None):
        self.MSGLEN = 2048
        self.version, self.ip, self.port, self.taxi = jsonparse().getSocketConfigure()

        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def getinfo(self):
        return self.version, self.ip, self.port, self.taxi

    def connect(self):
        # print(self.ip + ":" + self.port)
        self.sock.connect((self.ip, int(self.port)))

    def mksend(self, msg):
        totalsent = 0
        while totalsent < self.MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

        self.receive()

    def receive(self):
        chunks = ""
        bytes_recd = 0
        while bytes_recd < self.MSGLEN:
            chunk = self.sock.recv(min(self.MSGLEN - bytes_recd, self.MSGLEN))
            if chunk == b'' or chunk == b'\n':
                #raise RuntimeError("socket connection broken")
                break;

            # print(chunk)
            chunks += str(chunk)
            bytes_recd = bytes_recd + len(chunk)

        self.sock.close()
