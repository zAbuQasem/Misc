#!/usr/bin/python3
import time
from random import shuffle
from string import ascii_letters, digits
from itertools import product, chain


class Monoaplha:
    def __init__(self):
        self.key = None

    def generate_key(self):
        self.key = {}
        string = ascii_letters + digits
        original = list(string)
        shuffled = list(string)
        shuffle(shuffled)
        self.key = dict(zip(original, shuffled))

    def forge_key(self, msg, key):
        """Without spaces"""
        gencipher = list(dict.fromkeys(''.join(msg.split(" "))))
        genkey = list(dict.fromkeys(''.join(key.split(" "))))
        """With Spaces"""
        # gencipher = list(dict.fromkeys(list(msg)))
        # genkey = list(dict.fromkeys(list(key)))
        self.key = dict(zip(gencipher, genkey))

    def encrypt(self, msg, key=None):
        if not key:
            print("[*] User didn't provide a valid key\n[-] Generating a key...")
            self.generate_key()
            print(f"[+] Key generated: {self.key}")
        else:
            self.forge_key(msg, key)
            print(f"[-] Generating a key...\n[+] Key generated: {self.key}")
        encrypted = []
        for char in msg:
            for k, v in self.key.items():
                if char == k:
                    encrypted.append(v)
        """Converting the dictionary to a string"""
        StringKey = ""
        for k, v in self.key.items():
            StringKey += k+v
        print(f"[+] Key as a string: {StringKey}\n[*] Plain text: {''.join(msg)}\n[+] Generated Cipher: {''.join(encrypted)}")

    def decrypt(self, cipher, key):
        if key is None:
            print("[!] Decryption error: please enter a valid key")
            return False
        elif cipher is None or cipher == '':
            print("[!] Decryption error: please enter a valid cipher")
            return False
        """Forging the key"""
        key = list(key)
        key = iter(key)
        Forged_key = dict(zip(key, key))
        # print(Forged_key)
        decrypted = []
        for char in list(cipher):
            for k, v in Forged_key.items():
                if char == v:
                    decrypted.append(k)
        print(f"[+] Decrypted: {''.join(decrypted)}")

    def bruteforce(self, cipher, original):
        strings = ascii_letters + digits
        # Proudly from https://stackoverflow.com/questions/11747254/python-brute-force-algorithm
        permutation = chain.from_iterable(
            (''.join(char) for char in product(strings, repeat=i)) for i in range(1, len(cipher) + 1))
        print("[*] Starting bruteforce...")
        time.sleep(1.5)
        for perm in permutation:
            print(f"[@] Trying: {''.join(perm)}", end="\r", flush=True)
            if ''.join(perm) == original:
                print(f"[+] --- Cracked --- \n[->] Cipher: {cipher} - Original: {original}")
                return True
        print("[!] Bruteforce failed :(")

    def main(self):
        self.banner()
        choice = input("[@] Please choose a number from the following:\n-> 1- Encrypt\n-> 2- Decrypt\n-> 3- BruteForce\n\n[-] Choice: ")
        if choice == "1":
            msg = input("\n[*] Enter a text to encrypt: ")
            key = input("[*] Enter a key as a string (Enter to generate a random key): ")
            """Setting key to none to generate a key"""
            if key == '':
                key = None
            self.encrypt(msg, key)
        elif choice == "2":
            cipher = input("\n[*] Enter a cipher to decrypt: ")
            key = input("[*] Enter a key as a string : ")
            self.decrypt(cipher, key)
        elif choice == "3":
            """To demonstrate that decryption works """
            brute = input("\n[*] Enter a cipher to bruteforce: ")
            plain = input("[*] Enter the expected plain text (same length as the cipher): ")
            self.bruteforce(brute, plain)
        else:
            print("\n[!] Invalid choice!\n[#] Exiting...")
            exit(1)

    def banner(self):
        print("""  
        ████     ████
       ░██░██   ██░██
 ██████░██░░██ ██ ░██  ██████  ███████   ██████
░░░░██ ░██ ░░███  ░██ ██░░░░██░░██░░░██ ██░░░░██
   ██  ░██  ░░█   ░██░██   ░██ ░██  ░██░██   ░██
  ██   ░██   ░    ░██░██   ░██ ░██  ░██░██   ░██
 ██████░██        ░██░░██████  ███  ░██░░██████
░░░░░░ ░░         ░░  ░░░░░░  ░░░   ░░  ░░░░░░ v1337.0
-------------------------------------------------------
 A Code written to demonstrate a -> Mono-alphabetic cipher <- \n\n""")


if __name__ == '__main__':
    try:
        run = Monoaplha()
        run.main()
    except (KeyboardInterrupt, EOFError):
        print("\n[!] GoodBye :(\n")

"""
Checks:
Plain Text: "Attack postponed to tomorrow and do not use our secret paper until further info"
Key : "The quick brown fox jumps over the lazy dog"
"""
