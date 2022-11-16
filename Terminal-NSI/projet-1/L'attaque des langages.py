import os
from colorama import Fore, Style
from urllib.request import urlopen
import sys

print('\n'*100)  #Clear la console (si la ligne d'après ne marche pas)
os.system('cls') #Clear la console

print(f"{Fore.GREEN}==================================================================================================================================================================================================")
print("Bienvenue sur :")
print("")
print(" /$$ /$$               /$$     /$$                                                         /$$                           /$$                                                                      ")
print("| $$| $/              | $$    | $$                                                        | $$                          | $$                                                                      ")
print("| $$|_/     /$$$$$$  /$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$         /$$$$$$$  /$$$$$$   /$$$$$$$      | $$  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$")
print("| $$       |____  $$|_  $$_/|_  $$_/   |____  $$ /$$__  $$| $$  | $$ /$$__  $$       /$$__  $$ /$$__  $$ /$$_____/      | $$ |____  $$| $$__  $$ /$$__  $$ |____  $$ /$$__  $$ /$$__  $$ /$$_____/")
print("| $$        /$$$$$$$  | $$    | $$      /$$$$$$$| $$  \ $$| $$  | $$| $$$$$$$$      | $$  | $$| $$$$$$$$|  $$$$$$       | $$  /$$$$$$$| $$  \ $$| $$  \ $$  /$$$$$$$| $$  \ $$| $$$$$$$$|  $$$$$$ ")
print("| $$       /$$__  $$  | $$ /$$| $$ /$$ /$$__  $$| $$  | $$| $$  | $$| $$_____/      | $$  | $$| $$_____/ \____  $$      | $$ /$$__  $$| $$  | $$| $$  | $$ /$$__  $$| $$  | $$| $$_____/ \____  $$")
print("| $$$$$$$$|  $$$$$$$  |  $$$$/|  $$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$/|  $$$$$$$      |  $$$$$$$|  $$$$$$$ /$$$$$$$/      | $$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$$$$$$/")
print("|________/ \_______/   \___/   \___/   \_______/ \____  $$ \______/  \_______/       \_______/ \_______/|_______/       |__/ \_______/|__/  |__/ \____  $$ \_______/ \____  $$ \_______/|_______/ ")
print("                                                      | $$                                                                                       /$$  \ $$           /$$  \ $$                    ")
print("                                                      | $$                                                                                      |  $$$$$$/          |  $$$$$$/                    ")
print("                                                      |__/                                                                                       \______/            \______/                     ")
print("Créer par : TORO Nicolas TG09 | Version : 1.0")
print(f"=================================================================================================================================================================================================={Style.RESET_ALL}")
print("(Si le texte est mal affiché, alors veuillez agrandir la fenêtre ou la dézoomer)\n")


with urlopen("https://pastebin.com/raw/GzQzU2kU") as file:
    version = file.read().decode()
if version != "1.0":
    print(f"{Fore.RED}Une mise à jour est disponible ! Téléchargez-la ici : https://github.com/nt-games-ytb/language-attack/releases/tag/" + version + f"{Style.RESET_ALL}\n")

#Lance le jeu :
#execfile('attaque-des-langages/jeu.py')
os.system('python attaque-des-langages/jeu.py') 
#import jeu.jeu