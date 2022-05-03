import time

from pwn import *
from rich.console import Console

console = Console()
binary = "<Executable>"
context.log_level = 'warning'
password = ''
password_length = 9 # change me
CheckTime = {}

def gettime():
    global msg, password_length, password
    for i in range(password_length):
        for j in range(0,10):
            p = process(binary)
            payload = getnext(j)
            start = time.time()
            p.sendlineafter(b"\n", payload.encode())
            p.recvall()
            stop = time.time()
            calculated_time = stop - start
            CheckTime[j] = calculated_time
            p.close()
        if password:
            password += str(max(CheckTime, key=CheckTime.get))
        else:
            password = str(max(CheckTime, key=CheckTime.get))

        console.print(f"[bold red]⎇ [/bold red] [white]Password:[/white] [yellow]{password}[/yellow]", end="\r")
    console.print(f"[🔥] Password: {password}\n[✅] Done :)\n", style="yellow")

def getnext(num):
    payload = ''
    global password, password_length, CheckTime
    if not password:
        return str(num) + "0" * (password_length -1)
    else:
        if (len(str(password))) <= password_length:
            offset = password_length - (len(str(password))) - 1
            payload = str(password) + str(num) + "0" * offset
            return payload
        else:
            print("Kill yourself please")

def banner():
    console.print("""
  ████████ ██      ██
 ██░░░░░░ ░░      ░██
░██        ██     ░██  █████  ██████
░█████████░██  ██████ ██░░░██░░██░░█
░░░░░░░░██░██ ██░░░██░███████ ░██ ░
       ░██░██░██  ░██░██░░░░  ░██
 ████████ ░██░░██████░░██████░███
░░░░░░░░  ░░  ░░░░░░  ░░░░░░ ░░░
----------------------------------
[bold red][⌛] Sider | POC for a simple side channel attack [/bold red]\n\n""", style="blue")

if __name__ == "__main__":
    banner()
    console.print("[⚔] Starting the attack", style="bold blue")
    gettime()
