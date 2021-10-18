import time
from colorama import init, Fore
import webbrowser
import os
import hashlib
from audioplayer import AudioPlayer
import ctypes
import json
from pypresence import Presence
import info

init(autoreset=True)
ctypes.windll.kernel32.SetConsoleTitleW("IGrux")

with open('Setting.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

def haslo(a):
    b = a.encode()
    c = hashlib.sha256(b)
    if c.hexdigest() == str(obj['Password']): #'cea3c47b60ba56576b156f9bd5c87aaa3e319334e8fd0c2ba47c3e1640fcec4a': #Koliw
        time.sleep(3)
        os.system('cls')
        print(Fore.GREEN + 'DOSTĘP PRZYZNANO')
        dostep()
    else:
        os.system('cls')
        print(Fore.RED + 'ODMOWA DOSTĘPU')
        print(Fore.CYAN + 'Podaj Hasło:')
        Pass = input('>')
        haslo(Pass)

def dostep():
    print(Fore.CYAN + '1 - Web\n2 - Gry\n3 - Produkty w Sklepie u MrEsxej`a\n4 - Notatki\n5 - Play Audio\n6 - Piwnica\n7 - Autorzy\n8 - Waluty\n9 - Ustawienia\n10 - Exit')
    button = input('>')
    if button == '1':
        os.system('cls')
        print(Fore.CYAN + 'Wpisz URL lub napisz quit aby wyjść:')
        url = input('>')
        if url == 'quit':
            os.system('cls')
            dostep()
        else:
            webbrowser.open(url)
            Back()
    elif button == '2':
        os.system('cls')
        print(Fore.CYAN + 'Gry:')
        path = 'Games/'

        files = os.listdir(path)

        for f in files:
            print(f)
        game_path = input('>')
        try:
            os.startfile(f'Games\{game_path}')
        except:
            print(Fore.RED + "Plik nie dostępny! sprawdź  nazwę i uprawnienia.")
        Back()
    elif button == '3':
        os.system('cls')
        print(Fore.CYAN + info.sklep)
        Back()
    elif button == '4':
        os.system('cls')
        print(Fore.CYAN + 'Notatki:')
        path = 'Notes/'

        files = os.listdir(path)

        for f in files:
            print(f)
        file = input('>')
        try:
            ofile = open('Notes/' + file, 'r')
            print(ofile.read())
            ofile.close()
        except:
            print(Fore.RED + "Plik nie dostępny! sprawdź  nazwę i uprawnienia.")

        #ofile = open('Notes/' + file, 'w')
        #write = input('>')
        #ofile.write(write)

        Back()
    elif button == '5':
        os.system('cls')
        print(Fore.CYAN + 'audio:')
        path = 'Audio/'
        files = os.listdir(path)
        for f in files:
            print(f)
        sound = input('>')
        try:
            AudioPlayer('Audio/' + sound).play(block=False)
        except:
            print(Fore.RED + "Plik nie dostępny! sprawdź  nazwę i uprawnienia.")
        Back()
    elif button == '6':
        os.system('cls')
        print('Zapraszamy!')
        webbrowser.open('https://discord.gg/2wWh8ygKMb')
        Back()
    elif button == '7':
        os.system('cls')
        print(Fore.CYAN + info.autors)
        Back()
    elif button == '8':
        os.system('cls')
        print(Fore.CYAN + '100 tynkcoin = 1 Marek\n100 Marków = 1 Super-Matek\n100 Super-Marków = 1 Ultra-Marek\n100 Ultra-Marków = 1 Super-Ultra-Marek\n100 Super-Ultra-Marków = 1 Super-Duper-Ultra-Marek')
        Back()
    elif button == '9':
        os.system('cls')
        print(Fore.CYAN + '1 - Wyjdź\n2 - Zmień Hasło\n3 - Resetuj Ustawienia')
        num = input('>')
        if num == '1':
            dostep()
        elif num == '2':
            os.system('cls')
            print(Fore.CYAN + 'Wpisz nowe Hasło')
            new = input('>')
            newa = new.encode()
            newb = hashlib.sha256(newa)
            new_json = '{\n    "Password": "' + newb.hexdigest() + '"\n}'

            with open('Setting.json', 'w') as myfile:
                myfile.write(new_json)
        elif num == '3':
            os.system('cls')
            print(Fore.CYAN + 'Wpisz hasło:')
            has = input('>')
            b = has.encode()
            c = hashlib.sha256(b)
            if c.hexdigest() == str(obj['Password']):
                print(Fore.RED + 'Ustawienia Zresetowane')
                resetjson = '{\n    "Password": "cea3c47b60ba56576b156f9bd5c87aaa3e319334e8fd0c2ba47c3e1640fcec4a"\n}'
                with open('Setting.json', 'w') as myfile:
                 myfile.write(resetjson)
        else:
            os.system('cls')
            print(Fore.RED + 'ERROR')
            Back()
    elif button == '10':
        print(Fore.RED + 'DOWIDZENIA!')
        time.sleep(1)
        exit()
    else:
        os.system('cls')
        print(Fore.RED + 'ERROR')
        dostep()

def Back():
    print(Fore.CYAN + '\n1 - Wyjdź')
    backo = input('>')
    if backo == '1':
        os.system('cls')
        dostep()
    else:
        os.system('cls')
        print(Fore.RED + 'ERROR')
        Back()

def Animation():
    Frame=""
    for char in 'IGrux\nLoading... ':
        os.system('cls')
        if char==" ":
            Frame='IGrux\nLoaded!'
        else:
            Frame+=char
        print(Fore.GREEN + f'========================\n{Frame}\n========================')
        time.sleep(1)

client_id = str(obj['DiscordRP']['id'])
RPC = Presence(client_id)
RPC.connect()

print(RPC.update(state=str(obj['DiscordRP']['state']), buttons=[{"label":str(obj['DiscordRP']['Buttons']['Download']['label']), "url":str(obj['DiscordRP']['Buttons']['Download']['url'])}]))  # Set the presence

Animation()
print(Fore.CYAN + 'Podaj Hasło:')
Pass = input('>')
haslo(Pass)