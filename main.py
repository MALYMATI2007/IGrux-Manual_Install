import time
import info
from colorama import init, Fore
import webbrowser
import os
import hashlib
from audioplayer import AudioPlayer
import ctypes

init(autoreset=True)
ctypes.windll.kernel32.SetConsoleTitleW("IGrux")

def haslo(a):
    b = a.encode()
    c = hashlib.sha256(b)
    if c.hexdigest() == 'cea3c47b60ba56576b156f9bd5c87aaa3e319334e8fd0c2ba47c3e1640fcec4a': #Koliw
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
    print(Fore.CYAN + '1 - Web\n2 - Gry\n3 - Produkty w Sklepie u MrEsxej`a\n4 - Notatki\n5 - Play Audio\n6 - Piwnica\n7 - Autorzy\n8 - Ustawienia\n9 - Exit')
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
        os.startfile(f'Games\{game_path}')
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
        except:
            print("Plik nie dostępny! sprawdź  nazwę i uprawnienia.")
        print(ofile.read())
        ofile.close()

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
            AudioPlayer('Audio/' + sound).play(block=True)
        except:
            print("Plik nie dostępny! sprawdź  nazwę i uprawnienia.")
        Back()
    elif button == '6':
        os.system('cls')
        print('Zapraszamy!')
        webbrowser.open('https://discord.gg/uhAQgTF')
        Back()
    elif button == '7':
        os.system('cls')
        print(Fore.CYAN + info.autors)
        Back()
    elif button == '8':
        os.system('cls')
        print('COMMING SOON')
        Back()
    elif button == '9':
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

#client_id = "834734074014203905"
#RPC = Presence(client_id)
#RPC.connect()

#print(RPC.update(state="GitHub", buttons=[{"label":"IGruX", "url":"https://github.com/MALYMATI2007/IGrux-git_install/blob/main/main.py"}]))  # Set the presence

Animation()
print(Fore.CYAN + 'Podaj Hasło:')
Pass = input('>')
haslo(Pass)
