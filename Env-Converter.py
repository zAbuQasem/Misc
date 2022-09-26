#!/usr/bin/env python3
from sys import argv

#/** Supply a file with environment variables:
# APP_NAME=someapp
# APP_ENV=local
# APP_KEY=oirowvnwncvwnvwi
# APP_DEBUG=true
# APP_URL=http://localhost:8000

# And the script will convert them to a yaml list as shown:
# - name: NAME
#   value: VALUE

global template
template = '''
- name: "FASOOLYA"
  value: "BEEDA"
'''

def loadfile():
    data = {}
    try:
        with open(argv[1], "r") as f:
            env1 = [i.strip() for i in f.readlines()]
            env = [i for i in env1 if i]
            for i in env:
                try:
                    name,value = i.split("=",1)
                    data[name] = value
                except ValueError:
                    print("[!] YOU PROVIDED THE FOLLOWING KEY WITHOUT A VALUE!!")
                    print(f" -----> {i}")
                    print("[@] Continuing any way\n")
                    pass
            f.close()
            return data
    except FileNotFoundError:
        print("[!] File Not Found!")
        exit(1)

def convert():
    newdata = []
    data = loadfile()
    for k,v in data.items():
        newdata.append(template.lstrip().replace("FASOOLYA",k.replace('"','')).replace("BEEDA",v.replace('"','')))
    for i in newdata:
        print(i, end="")

# Run the Program
convert()
