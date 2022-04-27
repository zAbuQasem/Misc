import time

from pwn import *
from rich.console import Console

console = Console()
binary = "./pin_checker"
context.log_level = 'fatal'
global password, password_length, msg, CheckTime
password = ''
password_length = 8
msg = b"Please enter your 8-digit PIN code:"
CheckTime = {}

def gettime():
    global msg, password_length, password
    for i in range(password_length):
        for j in range(0,10):
            p = process(binary)
            payload = getnext(j)
            start = time.time()
            p.sendlineafter(msg, payload)
            p.recvall()
            stop = time.time()
            calculated_time = stop - start
            CheckTime[j] = calculated_time
            #print(f"[@] Time: {calculated_time} --> {j}")
            p.close()
        if password:
            password += str(max(CheckTime, key=CheckTime.get))
        else:
            password = str(max(CheckTime, key=CheckTime.get))

        #print("[!] Starting next iteration")
        console.print(f"[bold blue][+] Password:[/bold blue] [yellow]{password}[/yellow]", end="\r")
    console.print(f"[$] Password: {password}\n[!] Done :)\n", style="yellow")

def getnext(num):
    payload = ''
    global password, password_length, CheckTime
    if not password:
        return str(num) + "0000000"
    else:
        if (len(str(password))) <= password_length:
            offset = password_length - (len(str(password))) - 1
            payload = str(password) + str(num) + "0" * offset
            return payload.encode()
        else:
            print("Kill yourself please")


gettime()
