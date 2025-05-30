import time
import sys
import os
import random
import webbrowser

GITHUB_URL = "https://github.com/citizennn444"  # remplace avec ton vrai lien GitHub

def slow_print(text, delay=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_hack():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = r"""
  ____ ___ _____ ___ __________ _   _ 
 / ___|_ _|_   _|_ _|__  / ____| \ | |
| |    | |  | |  | |  / /|  _| |  \| |
| |___ | |  | |  | | / /_| |___| |\  |
 \____|___| |_| |___/____|_____|_| \_|
    """
    print(banner)
    slow_print("Initialisation du terminal distant...", 0.05)
    time.sleep(1)

    targets = ["192.168.0.1", "facebook.com", "google.com", "localhost", "github.com"]
    for i in range(10):
        ip = random.choice(targets)
        slow_print(f"[*] Connecting to {ip}...", 0.02)
        time.sleep(0.3)
        slow_print(f"[+] Access granted to {ip} - Session ID: {random.randint(1000,9999)}", 0.02)

    slow_print("\nTéléchargement de modules sensibles...", 0.04)
    for i in range(3):
        slow_print(f" - module_{i}.py [OK]", 0.03)
        time.sleep(0.2)

    slow_print("\n⚠️  ERREUR CRITIQUE : divulgation détectée !", 0.07)
    time.sleep(1)
    slow_print("Redirection vers le centre de contrôle principal...", 0.05)
    time.sleep(2)

    slow_print("\n👉 Surprise ! Ce n'était qu'une simulation 😎", 0.07)
    slow_print("Si tu veux voir du vrai code (et pas du cinéma)...", 0.05)
    slow_print(f"➡️  Direction mon GitHub : {GITHUB_URL}", 0.04)
    webbrowser.open(GITHUB_URL)

if __name__ == "__main__":
    fake_hack()
