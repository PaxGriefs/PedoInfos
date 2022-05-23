import os
os.system('pip install colorama')
os.system('pip install anonfile')
os.system('pip install pyAesCrypt')
os.system('cls')

from colorama import init, Fore
import time
import sys
from anonfile import AnonFile
import shutil
import pyAesCrypt
import glob

anon = AnonFile()

init(convert=True)

os.system('title PedoInfos. - Made by Pax the PedoHunter.')
print(Fore.RED + """
██████╗░███████╗██████╗░░█████╗░██╗███╗░░██╗███████╗░█████╗░██╗░██████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║████╗░██║██╔════╝██╔══██╗╚█║██╔════╝
""" + Fore.WHITE + """██████╔╝█████╗░░██║░░██║██║░░██║██║██╔██╗██║█████╗░░██║░░██║░╚╝╚█████╗░
""" + Fore.YELLOW + """██╔═══╝░██╔══╝░░██║░░██║██║░░██║██║██║╚████║██╔══╝░░██║░░██║░░░░╚═══██╗
██║░░░░░███████╗██████╔╝╚█████╔╝██║██║░╚███║██║░░░░░╚█████╔╝░░░██████╔╝
╚═╝░░░░░╚══════╝╚═════╝░░╚════╝░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░░░░╚═════╝░""")

time.sleep(1)
print(Fore.GREEN + "(Idk why I added colors)")

time.sleep(0.5)
print(Fore.WHITE + "Made by" + Fore.RED + " Pax" + Fore.WHITE +" the" + Fore.BLUE + " PedoHunter.")

print()
print()

print(Fore.WHITE + "-=+Menu+=-")
print("1 - Writer")
print("2 - PedoDataBase")
print("3 - About The Developer")
print("4 - DirCrypt")
print()
print("E - Exit")
print()

ans=input("-=> | ")

# =================================================================================================

if ans=="E":
    os.system('taskkill /f /im cmd.exe')
    os.system('taskkill /f /im python.exe')

# =================================================================================================

elif ans=="1":
    os.system('cls')

    print(Fore.CYAN + """
█▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
█▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")

    sys.stdout.write('\rloading |')
    time.sleep(0.2)
    sys.stdout.write('\rloading /')
    time.sleep(0.2)
    sys.stdout.write('\rloading -')
    time.sleep(0.2)
    sys.stdout.write('\rloading \\')
    time.sleep(0.2)
    sys.stdout.write('\rloading |')
    time.sleep(0.2)
    sys.stdout.write('\rloading /')
    time.sleep(0.2)
    sys.stdout.write('\rloading -')
    time.sleep(0.2)
    sys.stdout.write('\rloading \\')
    time.sleep(0.2)
    sys.stdout.write('\rDone!     ')
    time.sleep(0.3)
    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's Full Name:")
    Name=input("-=> | ")

    file = open(f"!Pedo! {Name}.txt", "w")
    file.write("-=||PedoInfo's||=-\n")
    file.write("------------------\n")
    file.write("\n")

    file.write(f"-=Name=- = {Name}.\n")

    os.system('mkdir PedoDataBase')

    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Name Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's Main Email:")
    MainEmail = input("-=> | ")

    file.write(f"-=Main Email=- = {MainEmail}\n")

    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Main Email Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's Other Email:")
    OtherEmail = input("-=> | ")

    file.write(f"-=Other Email=- = {OtherEmail}\n")

    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Other Email Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's Other Other Email:")
    OtherOtherEmail = input("-=> | ")

    file.write(f"-=Other Other Email=- = {OtherOtherEmail}\n")

    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Other Other Email Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's Phone Number:")
    PhoneNumber = input("-=> | ")

    file.write(f"-=Phone Number=- = {PhoneNumber}\n")

    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Phone Number Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's Ip:")
    Ip = input("-=> | ")

    file.write(f"-=Ip=- = {Ip}\n")

    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Ip Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's 3 Most Used Usernames:")
    print("Press Enter After Every Username.")
    Username1 = input("-=> |1| ")

    file.write(f"-=Username 1=- = {Username1}\n")

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's 3 Most Used Usernames:")
    print("Press Enter After Every Username.")
    print(f"1. {Username1}")
    Username2 = input("-=> |2| ")

    file.write(f"-=Username 2=- = {Username2}\n")

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's 3 Most Used Usernames:")
    print("Press Enter After Every Username.")
    print(f"1. {Username1}")
    print(f"2. {Username2}")
    Username3 = input("-=> |3| ")

    file.write(f"-=Username 3=- = {Username3}\n")

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's 3 Most Used Usernames:")
    print(f"1. {Username1}")
    print(f"2. {Username2}")
    print(f"3. {Username3}")
    print()
    print("Usernames Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    file.write("\n")
    file.write("-=+#Account Info#+=-\n")
    file.write("\n")

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's Google Account Info.")
    sys.stdout.write("Account Website:")
    AccountWebsite = input("-=> | ")
    file.write(f"-={AccountWebsite}=-\n")

    sys.stdout.write("Account Email:")
    AccountEmail = input("-=> | ")
    file.write(f"-=Email=- = {AccountEmail}\n")

    sys.stdout.write("Account Username:")
    AccountUsername = input("-=> | ")
    file.write(f"-=Username=- = {AccountUsername}\n")

    sys.stdout.write("Account Password:")
    AccountPassword = input("-=> | ")
    file.write(f"-=Password=- = {AccountPassword}\n")

    file.write("\n")

    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Google Account Info Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's Instagram Account Info.")
    sys.stdout.write("Account Website:")
    AccountWebsite = input("-=> | ")
    file.write(f"-={AccountWebsite}=-\n")

    sys.stdout.write("Account Email:")
    AccountEmail = input("-=> | ")
    file.write(f"-=Email=- = {AccountEmail}\n")

    sys.stdout.write("Account Username:")
    AccountUsername = input("-=> | ")
    file.write(f"-=Username=- = {AccountUsername}\n")

    sys.stdout.write("Account Password:")
    AccountPassword = input("-=> | ")
    file.write(f"-=Password=- = {AccountPassword}\n")

    file.write("\n")

    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Instagram Account Info Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's Facebook Account Info.")
    sys.stdout.write("Account Website:")
    AccountWebsite = input("-=> | ")
    file.write(f"-={AccountWebsite}=-\n")

    sys.stdout.write("Account Email:")
    AccountEmail = input("-=> | ")
    file.write(f"-=Email=- = {AccountEmail}\n")

    sys.stdout.write("Account Username:")
    AccountUsername = input("-=> | ")
    file.write(f"-=Username=- = {AccountUsername}\n")

    sys.stdout.write("Account Password:")
    AccountPassword = input("-=> | ")
    file.write(f"-=Password=- = {AccountPassword}\n")

    file.write("\n")

    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Facebook Account Info Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's Twitter Account Info.")
    sys.stdout.write("Account Website:")
    AccountWebsite = input("-=> | ")
    file.write(f"-={AccountWebsite}=-\n")

    sys.stdout.write("Account Email:")
    AccountEmail = input("-=> | ")
    file.write(f"-=Email=- = {AccountEmail}\n")

    sys.stdout.write("Account Username:")
    AccountUsername = input("-=> | ")
    file.write(f"-=Username=- = {AccountUsername}\n")

    sys.stdout.write("Account Password:")
    AccountPassword = input("-=> | ")
    file.write(f"-=Password=- = {AccountPassword}\n")

    file.write("\n")

    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Twitter Account Info Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's Snapchat Account Info.")
    sys.stdout.write("Account Website:")
    AccountWebsite = input("-=> | ")
    file.write(f"-={AccountWebsite}=-\n")

    sys.stdout.write("Account Email:")
    AccountEmail = input("-=> | ")
    file.write(f"-=Email=- = {AccountEmail}\n")

    sys.stdout.write("Account Username:")
    AccountUsername = input("-=> | ")
    file.write(f"-=Username=- = {AccountUsername}\n")

    sys.stdout.write("Account Password:")
    AccountPassword = input("-=> | ")
    file.write(f"-=Password=- = {AccountPassword}\n")

    file.write("\n")

    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Snapchat Account Info Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's Discord Account Info.")
    sys.stdout.write("Account Website:")
    AccountWebsite = input("-=> | ")
    file.write(f"-={AccountWebsite}=-\n")

    sys.stdout.write("Account Email:")
    AccountEmail = input("-=> | ")
    file.write(f"-=Email=- = {AccountEmail}\n")

    sys.stdout.write("Account Username:")
    AccountUsername = input("-=> | ")
    file.write(f"-=Username=- = {AccountUsername}\n")

    sys.stdout.write("Account Password:")
    AccountPassword = input("-=> | ")
    file.write(f"-=Password=- = {AccountPassword}\n")

    file.write("\n")

    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Discord Account Info Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's Other Account Info.")
    sys.stdout.write("Account Website:")
    AccountWebsite = input("-=> | ")
    file.write(f"-={AccountWebsite}=-\n")

    sys.stdout.write("Account Email:")
    AccountEmail = input("-=> | ")
    file.write(f"-=Email=- = {AccountEmail}\n")

    sys.stdout.write("Account Username:")
    AccountUsername = input("-=> | ")
    file.write(f"-=Username=- = {AccountUsername}\n")

    sys.stdout.write("Account Password:")
    AccountPassword = input("-=> | ")
    file.write(f"-=Password=- = {AccountPassword}\n")

    file.write("\n")

    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Other Account Info Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "The Pedo's Other Other Account Info.")
    sys.stdout.write("Account Website:")
    AccountWebsite = input("-=> | ")
    file.write(f"-={AccountWebsite}=-\n")

    sys.stdout.write("Account Email:")
    AccountEmail = input("-=> | ")
    file.write(f"-=Email=- = {AccountEmail}\n")

    sys.stdout.write("Account Username:")
    AccountUsername = input("-=> | ")
    file.write(f"-=Username=- = {AccountUsername}\n")

    sys.stdout.write("Account Password:")
    AccountPassword = input("-=> | ")
    file.write(f"-=Password=- = {AccountPassword}\n")

    file.write("\n")

    os.system('cls')

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Other Other Account Info Saved.")
    time.sleep(1)

    os.system('cls')

    # ------------------------------------------------------------------------------------------------

    file.write("\n")
    file.write("-=+@Photos@+=-\n")
    file.write("\n")

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Do you have photos of the pedo or just screenshots?")
    print("Y/N")
    photos = input("-=> | ")

    if photos=="N":
        os.system('cls')
        file.close()
        shutil.move(f"!Pedo! {Name}.txt", "PedoDataBase")
        print(Fore.BLUE + "File Saved.")
        time.sleep(2)
        os.system('cls')
        os.system('python PedoInfos.py')

    elif photos=="Y":
        os.system('cls')
        print(Fore.CYAN + """
        █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
        █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
        print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

        print()
        print()

        print(Fore.WHITE + "What is the Photo/screenshot name?")
        print("Put the photos/screenshots in the main project folder.")
        print("Add file extentions. - Example .png .jpg")
        photosscreens = input("-=> | ")

        upload = anon.upload(photosscreens, progressbar=True)
        print(upload.url.geturl())
        file.write(f"-=|{photosscreens}|=-\n")
        file.write(f"-=Url=- = {upload.url.geturl()}\n")
        file.write("\n")

        os.system('cls')

        print(Fore.CYAN + """
        █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
        █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
        print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

        print()
        print()

        print(Fore.WHITE + "Photo/Screenshot Saved.")
        print(Fore.BLUE + f"Upload Link Also Saved. - {upload.url.geturl()}")
        time.sleep(2)

        os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Do you have more Photos/Screenshots?")
    print("Y/N")
    photos = input("-=> | ")

    if photos == "N":
        os.system('cls')
        file.close()
        shutil.move(f"!Pedo! {Name}.txt", "PedoDataBase")
        print(Fore.BLUE + "File Saved.")
        time.sleep(2)
        os.system('cls')
        os.system('python PedoInfos.py')

    elif photos == "Y":
        os.system('cls')
        print(Fore.CYAN + """
        █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
        █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
        print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

        print()
        print()

        print(Fore.WHITE + "What is the Photo/screenshot name?")
        print("Put the photos/screenshots in the main project folder.")
        print("Add file extentions. - Example .png .jpg")
        photosscreens = input("-=> | ")

        upload = anon.upload(photosscreens, progressbar=True)
        print(upload.url.geturl())
        file.write(f"-=|{photosscreens}|=-\n")
        file.write(f"-=Url=- = {upload.url.geturl()}\n")
        file.write("\n")

        os.system('cls')

        print(Fore.CYAN + """
        █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
        █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
        print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

        print()
        print()

        print(Fore.WHITE + "Photo/Screenshot Saved.")
        print(Fore.BLUE + f"Upload Link Also Saved. - {upload.url.geturl()}")
        time.sleep(2)

        os.system('cls')

    # ------------------------------------------------------------------------------------------------

    print(Fore.CYAN + """
    █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
    █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
    print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

    print()
    print()

    print(Fore.WHITE + "Do you have any more Photos/Screenshots?")
    print("Y/N")
    photos = input("-=> | ")

    if photos == "N":
        os.system('cls')
        file.close()
        shutil.move(f"!Pedo! {Name}.txt", "PedoDataBase")
        print(Fore.BLUE + "File Saved.")
        time.sleep(2)
        os.system('cls')
        os.system('python PedoInfos.py')

    elif photos == "Y":
        os.system('cls')
        print(Fore.CYAN + """
        █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
        █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
        print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

        print()
        print()

        print(Fore.WHITE + "What is the Photo/screenshot name?")
        print("Put the photos/screenshots in the main project folder.")
        print("Add file extentions. - Example .png .jpg")
        photosscreens = input("-=> | ")

        upload = anon.upload(photosscreens, progressbar=True)
        print(upload.url.geturl())
        file.write(f"-=|{photosscreens}|=-\n")
        file.write(f"-=Url=- = {upload.url.geturl()}\n")
        file.write("\n")

        os.system('cls')

        print(Fore.CYAN + """
        █▀█ █▀▀ █▀▄ █▀█ █░█░█ █▀█ █ ▀█▀ █▀▀ █▀█
        █▀▀ ██▄ █▄▀ █▄█ ▀▄▀▄▀ █▀▄ █ ░█░ ██▄ █▀▄""")
        print(Fore.BLUE + "This writes the Information you have of the Pedo in a text file.")

        print()
        print()

        print(Fore.WHITE + "Photo/Screenshot Saved.")
        print(Fore.BLUE + f"Upload Link Also Saved. - {upload.url.geturl()}")
        time.sleep(2)
        os.system('cls')
        file.close()
        shutil.move(f"!Pedo! {Name}.txt", "PedoDataBase")
        print(Fore.BLUE + "File Saved.")
        time.sleep(2)
        os.system('cls')
        os.system('python PedoInfos.py')

# =================================================================================================

elif ans=="2":
    os.system('cls')
    print(Fore.BLUE + """
█▀█ █▀▀ █▀▄ █▀█ █▀▄ ▄▀█ ▀█▀ ▄▀█ █▄▄ ▄▀█ █▀ █▀▀
█▀▀ ██▄ █▄▀ █▄█ █▄▀ █▀█ ░█░ █▀█ █▄█ █▀█ ▄█ ██▄""")

    sys.stdout.write('\rloading |')
    time.sleep(0.2)
    sys.stdout.write('\rloading /')
    time.sleep(0.2)
    sys.stdout.write('\rloading -')
    time.sleep(0.2)
    sys.stdout.write('\rloading \\')
    time.sleep(0.2)
    sys.stdout.write('\rloading |')
    time.sleep(0.2)
    sys.stdout.write('\rloading /')
    time.sleep(0.2)
    sys.stdout.write('\rloading -')
    time.sleep(0.2)
    sys.stdout.write('\rloading \\')
    time.sleep(0.2)
    sys.stdout.write('\rDone!     ')
    time.sleep(0.3)
    os.system('cls')

    print(Fore.BLUE + """
█▀█ █▀▀ █▀▄ █▀█ █▀▄ ▄▀█ ▀█▀ ▄▀█ █▄▄ ▄▀█ █▀ █▀▀
█▀▀ ██▄ █▄▀ █▄█ █▄▀ █▀█ ░█░ █▀█ █▄█ █▀█ ▄█ ██▄""")
    print(Fore.GREEN + "This shows and opens PedoDataBase files.")

    print()
    print()

    Dir = os.listdir('PedoDataBase')

    print(Fore.YELLOW + f"{Dir}".replace('[', '').replace(']', '').replace(', ', '\n'))

    print(Fore.WHITE + "What file do you want to open?")
    print("With .txt")
    File = input("-=> | ")

    file = open(f"PedoDataBase/{File}")
    FileContents = file.read()
    os.system('cls')
    print(FileContents)
    print()
    print("B to go back to the menu.")

    Back = input("-=> | ")

    if Back=="B":
        os.system('cls')
        os.system('exit')
        os.system('start python PedoInfos.py')

    elif Back !="":
        print()
        print("Wrong but ill bring you back to the menu.")
        time.sleep(2)
        os.system('cls')
        os.system('exit')
        os.system('start python PedoInfos.py')

# =================================================================================================

elif ans=="3":
    os.system('cls')
    print(Fore.MAGENTA + """
▄▀█ █▄▄ █▀█ █░█ ▀█▀   █▀█ ▄▀█ ▀▄▀ ░
█▀█ █▄█ █▄█ █▄█ ░█░   █▀▀ █▀█ █░█ ▄""")
    print(Fore.RED + "Some Info about me.")
    print("Im a Depressed Suicidal Shithead")
    time.sleep(2.5)
    os.system('cls')
    os.system('python PedoInfos.py')

# =================================================================================================

elif ans=="4":
    os.system('cls')
    bufferSize = 64 * 1024
    dir_path = "PedoDataBase\*.*"
    directory = "PedoDataBase"
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".txt")]
    filtered_files2 = [file for file in files_in_directory if file.endswith(".aes")]

    print(Fore.LIGHTRED_EX + """
█▀▄ █ █▀█ █▀▀ █▀█ █▄█ █▀█ ▀█▀
█▄▀ █ █▀▄ █▄▄ █▀▄ ░█░ █▀▀ ░█░""")
    print(Fore.CYAN + "Encrypt or Decrypt?")
    print(Fore.WHITE + "E/D")
    ED = input("-=> | ")
    if ED=="E":
        os.system('cls')
        print(Fore.LIGHTRED_EX + """
    █▀▄ █ █▀█ █▀▀ █▀█ █▄█ █▀█ ▀█▀
    █▄▀ █ █▀▄ █▄▄ █▀▄ ░█░ █▀▀ ░█░""")
        print(Fore.CYAN + "Type in the password you want to use.")
        Pass = input("-=> | ")
        os.system('cls')
        print(Fore.RED + "Encrypting...")
        for files in glob.glob(dir_path, recursive=True):
            pyAesCrypt.encryptFile(files, files + ".aes", Pass, bufferSize)
        time.sleep(1)
        for file in filtered_files:
            path_to_file = os.path.join(directory, file)
            os.remove(path_to_file)
        os.system('cls')
        os.system('python PedoInfos.py')

    elif ED=="D":
        os.system('cls')
        print(Fore.LIGHTRED_EX + """
    █▀▄ █ █▀█ █▀▀ █▀█ █▄█ █▀█ ▀█▀
    █▄▀ █ █▀▄ █▄▄ █▀▄ ░█░ █▀▀ ░█░""")
        print(Fore.CYAN + "Whats the Password?")
        PassD = input("-=> | ")
        os.system('cls')
        print(Fore.RED + "Decrypting...")
        for friles in glob.glob(dir_path, recursive=True):
            pyAesCrypt.decryptFile(friles, friles.replace(".aes", ""), PassD, bufferSize)
        time.sleep(1)
        for file in filtered_files2:
            path_to_file = os.path.join(directory, file)
            os.remove(path_to_file)
        os.system('cls')
        os.system('python PedoInfos.py')

    elif ED !="":
        print("Not an option.")
        os.system('cls')
        os.system('python PedoInfos.py')

# =================================================================================================

elif ans !="":
    print(Fore.RED + "Not an Option")
    time.sleep(2)
    os.system('cls')
    os.system('python PedoInfos.py')