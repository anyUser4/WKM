#[Web Kit Medic (WKM); Programa principal].
import os
import requests
from colorama import *

init()
os.system('clear')
#[Corpus; Creación de verificador de conexión a internet].
def verifi():
    try:
        request = requests.get("https://www.google.com/?hl=es", timeout = 5)
    except (requests.ConnectionError, requests.Timeout):
        return 0
    else:
        return 1

#[Corpus; Inicio].
mad = verifi()

#[Corpus; Ratificación].
if mad == 0:
    print(Fore.RED + Style.BRIGHT)
    print("[WKM]: Programa no iniciado, sin conexión a internet.")
elif mad == 1:
    import config_es
    print(config_es)