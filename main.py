import time
import colorama
from colorama import init, Fore
import webbrowser
import os
import hashlib
from audioplayer import AudioPlayer

init(autoreset=True)

def haslo(a):
    b = a.encode()
    c = hashlib.sha256(b)
    if c.hexdigest() == 'ea3a03b4971eeb62730e1de238225cc4e6145f0eb50ad28b1379f2a2ee71e16e':
        time.sleep(3)
        print(Fore.GREEN + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDOSTĘP PRZYZNANO')
        dostep()
    else:
        print(Fore.RED + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nODMOWA DOSTĘPU')
        print(Fore.CYAN + 'Podaj Hasło:')
        Pass = input('>')
        haslo(Pass)

def dostep():
    print(Fore.CYAN + '1 - Web\n2 - Gry\n3 - Passwords\n4 - Notatki\n5 - Play Audio\n6 - Exit')
    button = input('>')
    if button == '1':
        print(Fore.CYAN + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWpisz URL lub napisz quit aby wyjść:')
        url = input('>')
        if url == 'quit':
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            dostep()
        else:
            webbrowser.open(url)
            Back()
    elif button == '2':
        print(Fore.CYAN + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n0 Gier')
        Back()
    elif button == '3':
        print(Fore.CYAN + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHasła:\nABC\n1234567\nQASDER')
        Back()
    elif button == '4':
        print(Fore.CYAN + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNotatki:')
        path = 'Notes/'

        files = os.listdir(path)

        for f in files:
            print(f)
        file = input('>')

        ofile = open('Notes/' + file, 'r')
        print(ofile.read())
        ofile.close()

        #ofile = open('Notes/' + file, 'w')
        #write = input('>')
        #ofile.write(write)

        Back()
    elif button == '5':
        print(Fore.CYAN + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\naudio:')
        path = 'Audio/'
        files = os.listdir(path)
        for f in files:
            print(f)
        sound = input('>')
        AudioPlayer('Audio/' + sound).play(block=True)
        Back()
    elif button == '6':
        print(Fore.RED + 'DOWIDZENIA!')
        time.sleep(1)
        exit()
    else:
        print(Fore.RED + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nERROR')
        dostep()

def Back():
    print(Fore.CYAN + '\n1 - Wyjdź')
    backo = input('>')
    if backo == '1':
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        dostep()
    else:
        print(Fore.RED + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nERROR')
        Back()

def Animation():
    a = Fore.GREEN
    space = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
    print(space + a + '========================\nI\n\n========================')
    time.sleep(1)
    print(space + a + '========================\nIG\n\n========================')
    time.sleep(1)
    print(space + a + '========================\nIGr\n\n========================')
    time.sleep(1)
    print(space + a + '========================\nIGru\n\n========================')
    time.sleep(1)
    print(space + a + '========================\nIGrux\n\n========================')
    time.sleep(1)
    print(space + a + '========================\nIGrux\nLoading\n========================')
    time.sleep(1)
    print(space + a + '========================\nIGrux\nLoading.\n========================')
    time.sleep(1)
    print(space + a + '========================\nIGrux\nLoading..\n========================')
    time.sleep(1)
    print(space + a + '========================\nIGrux\nLoading...\n========================')
    time.sleep(1)
    print(space + a + '========================\nIGrux\nLoaded!\n========================')

Animation()
print(Fore.CYAN + 'Podaj Hasło:')
Pass = input('>')
haslo(Pass)