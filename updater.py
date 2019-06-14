from colorama import Fore, init
import requests


init()


def checker():

    try:
        link_update = "http://52.211.14.150/updater.html"
        version = requests.get(link_update).text
        print("[+] New Update Found: " + version)

        new_version = "http://52.211.14.150/updates/" + version
        with open('checker.py', 'w') as checker:
            nv = requests.get(new_version).text
            checker.write(nv)
            checker.close()
        print("[!] Checker succesfully Updated!")

    except Exception:
        print("[-] No Updates Now")

if __name__ == "__main__":
    print(Fore.YELLOW + "[*]" + Fore.RESET + " Checking if Update is avaiable...")
    checker()
