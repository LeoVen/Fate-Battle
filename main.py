import combat
import logs
from support import *

def choice(c):
    if c == '0':
        return False
    elif c == '1':
        clear()
        combat.combatMode()
        return True
    elif c == '2':
        clear()
        print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗  
\t║\t\t\t\tStory Mode will be available soon!\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
            ''')
        input("<<")
        return True
    elif c == '3':
        clear()
        print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗  
\t║\t\t\t\tSandbox Mode will be available soon!\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
            ''')
        input("<<")
        return True
    elif c == '?':
        clear()
        logs.help()
        input("<<")
        return True
    elif c == 'c' or c == 'C':
        clear()
        logs.credits()
        input("<<")
        return True
    elif c == 'r' or c == 'R':
        clear()
        logs.releaseNotes()
        input("<<")
        return True
    elif c == 'a' or c == 'A':
        clear()
        logs.about()
        input("<<")
        return True
    else:
        clear()
        logs.error()
        print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗  
\t║\t\t\t\tChoice not Available!\t\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
            ''')
        input("<<")
        return True


def main():
    
    logs.intro()
    while True:
        clear()
        logs.menu()
        string = input("<<")
        mu = choice(string)
        if not mu:
            clear()
            break



if __name__ == "__main__":
    main()
