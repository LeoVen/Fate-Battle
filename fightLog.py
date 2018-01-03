from support import *
from time import sleep



def noMana():
    print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\t║\t\t\t\t\tNot Enough Mana\t\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
        ''')
    enterToContinue()


def enterToContinue():
    print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\t║\t\t\t\tPress Enter to Continue ...\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
        ''')
    input("<<")



def invalidOption():
	clear()
	error()
	print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗  
\t║\t\t\t\tChoice not Available!\t\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
            ''')
	enterToContinue()


def skillMissed():
    print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗  
\t║\t\t\t\tSkill Missed\t\t\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
            ''')
    enterToContinue()


def attackMissed():
    print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\t║\t\t\t\t\tAttack Missed\t\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
        ''')
    enterToContinue()



def skillsDisabled(n):
    print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\t║\t\t\t\tSkills Disabled for {} turn(s)\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
        '''.format(n))
    enterToContinue()



def attacksDisabled(n):
    print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\t║\t\t\t\tAttacks Disabled for {} turn(s)\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
        '''.format(n))
    enterToContinue()



def criticalHit():
    print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\t║\t\t\t\t\tCritical Hit!\t\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
        ''')
    sleep(1)



def attackSummary():
    print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\t║\t\t\t\t\tCritical Hit!\t\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
        ''')
    enterToContinue()