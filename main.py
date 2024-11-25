import requests
import sys 
import os
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Style
import socket

init(autoreset=True)

with open("paths.txt","r") as file:
    paths=file.read().splitlines()
try:
    target=sys.argv[1]
    session=requests.session()
    for path in paths:
        respone=session.get(target,verify=False)
        if respone.status_code == 200:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] found a dangerous file in {target+path}")
        else:
            pass
except:
    print("usage : python main.py https://example.com")