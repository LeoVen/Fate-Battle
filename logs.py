from texts import *
from support import *

def intro():
    clear()
    print('''
                                                        |ZZzzz
                                                        |
                                                        |
                                           |ZZzzz      /^\            |ZZzzz
                                           |          |~~~|           |
                                           |        |^^^^^^^|        / \ 
                                          /^\       |[]+    |       |~~~|
                                       |^^^^^^^|    |    +[]|       |   |
                                       |    +[]|/\/\/\/\^/\/\/\/\/|^^^^^^^|
                                       |+[]+   |~~~~~~~~~~~~~~~~~~|    +[]|
                                       |       |  []   /^\   []   |+[]+   |
                                       |   +[]+|  []  || ||  []   |   +[]+|
                                       |[]+    |      || ||       |[]+    |
                                       |_______|------------------|_______|

╔═════════════════════════════╦════════════════════════════════════════════════════╦════════════════════════════╗
║                             ║                                                    ║                            ║
║                             ║ Hello and Welcome to the Battle of the Great Graal ║                            ║
║              ║              ║ Your objective is to kill the opposing enemy       ║              ║             ║
║              ║              ║ Your final objective is to get the Great Grall     ║              ║             ║
║              ║              ║ And all your wishes will be fulfilled              ║              ║             ║
║              ║              ║ Here you'll face many great challenges!            ║              ║             ║
║              ║              ║ A hero will be summoned to serve your needs...     ║              ║             ║
║              ║              ║ And others will be summoned to serve your enemies  ║              ║             ║
║           ═══╬═══           ║                                                    ║           ═══╬═══          ║
║              ║              ║ There are seven heroes:                            ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║           Enter to continue or 0 to skip           ║                            ║
╚═════════════════════════════╩════════════════════════════════════════════════════╩════════════════════════════╝
    ''')
    nan = input("<<")
    clear()
    if nan == '0':
        return
    print('''
╔═════════════════════════════╦════════════════════════════════════════════════════╦════════════════════════════╗
║                             ║ Hero Class: Saber                                  ║                            ║
║                             ║                                                    ║                            ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║           ═══╬═══           ║ {} ║           ═══╬═══          ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║                             ║                                                    ║                            ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║     Pros:                                          ║                            ║
║                             ║ < High Physical Damage                             ║                            ║
║              ║              ║ < High Physical Defense                            ║              ║             ║
║              ║              ║ < High Hit Points Regeneration                     ║              ║             ║
║              ║              ║ <                                                  ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║     Cons:                                          ║              ║             ║
║              ║              ║ < Low Speed                                        ║              ║             ║
║           ═══╬═══           ║ < Low Magic Defense                                ║           ═══╬═══          ║
║              ║              ║ < Average Skill Set                                ║              ║             ║
║              ║              ║ < Low Critical Chance                              ║              ║             ║
║                             ║                                                    ║                            ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║           Enter to continue or 0 to skip           ║                            ║
╚═════════════════════════════╩════════════════════════════════════════════════════╩════════════════════════════╝
    '''.format( txt(saberTxt, 50, 1), txt(saberTxt, 50, 2),
                txt(saberTxt, 50, 3), txt(saberTxt, 50, 4),
                txt(saberTxt, 50, 5), txt(saberTxt, 50, 6),
                txt(saberTxt, 50, 7), txt(saberTxt, 50, 8),
                txt(saberTxt, 50, 9), txt(saberTxt, 50, 10) ))
    nan = input("<<")
    clear()
    if nan == '0':
        return
    print('''
╔═════════════════════════════╦════════════════════════════════════════════════════╦════════════════════════════╗
║                             ║ Hero Class: Archer                                 ║                            ║
║                             ║                                                    ║                            ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║           ═══╬═══           ║ {} ║           ═══╬═══          ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║                             ║                                                    ║                            ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║     Pros:                                          ║                            ║
║                             ║ < High Physical Damage                             ║                            ║
║              ║              ║ < High Critical Chance                             ║              ║             ║
║              ║              ║ < Good Skill Set                                   ║              ║             ║
║              ║              ║ < Medium Speed                                     ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║     Cons:                                          ║              ║             ║
║              ║              ║ < Low Hit Points                                   ║              ║             ║
║           ═══╬═══           ║ < Low Magic Defense                                ║           ═══╬═══          ║
║              ║              ║ < Low Physical Defense                             ║              ║             ║
║              ║              ║ <                                                  ║              ║             ║
║                             ║                                                    ║                            ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║           Enter to continue or 0 to skip           ║                            ║
╚═════════════════════════════╩════════════════════════════════════════════════════╩════════════════════════════╝
    '''.format( txt(archerTxt, 50, 1), txt(archerTxt, 50, 2),
                txt(archerTxt, 50, 3), txt(archerTxt, 50, 4),
                txt(archerTxt, 50, 5), txt(archerTxt, 50, 6),
                txt(archerTxt, 50, 7), txt(archerTxt, 50, 8),
                txt(archerTxt, 50, 9), txt(archerTxt, 50, 10) ))
    nan = input("<<")
    clear()
    if nan == '0':
        return
    print('''
╔═════════════════════════════╦════════════════════════════════════════════════════╦════════════════════════════╗
║                             ║ Hero Class: Rider                                  ║                            ║
║                             ║                                                    ║                            ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║           ═══╬═══           ║ {} ║           ═══╬═══          ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║                             ║                                                    ║                            ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║     Pros:                                          ║                            ║
║                             ║ < High Physical Defense                            ║                            ║
║              ║              ║ < High Magic Defense                               ║              ║             ║
║              ║              ║ < High Speed                                       ║              ║             ║
║              ║              ║ <                                                  ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║     Cons:                                          ║              ║             ║
║              ║              ║ < Average Attack                                   ║              ║             ║
║           ═══╬═══           ║ < Low Maana                                        ║           ═══╬═══          ║
║              ║              ║ < Low Mana Regeneration                            ║              ║             ║
║              ║              ║ < Low Critical Chance                              ║              ║             ║
║                             ║                                                    ║                            ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║           Enter to continue or 0 to skip           ║                            ║
╚═════════════════════════════╩════════════════════════════════════════════════════╩════════════════════════════╝
    '''.format( txt(riderTxt, 50, 1), txt(riderTxt, 50, 2),
                txt(riderTxt, 50, 3), txt(riderTxt, 50, 4),
                txt(riderTxt, 50, 5), txt(riderTxt, 50, 6),
                txt(riderTxt, 50, 7), txt(riderTxt, 50, 8),
                txt(riderTxt, 50, 9), txt(riderTxt, 50, 10) ))
    nan = input("<<")
    clear()
    if nan == '0':
        return
    print('''
╔═════════════════════════════╦════════════════════════════════════════════════════╦════════════════════════════╗
║                             ║ Hero Class: Lancer                                 ║                            ║
║                             ║                                                    ║                            ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║           ═══╬═══           ║ {} ║           ═══╬═══          ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║                             ║                                                    ║                            ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║     Pros:                                          ║                            ║
║                             ║ < High Physical Defense                            ║                            ║
║              ║              ║ < High Magic Defense                               ║              ║             ║
║              ║              ║ < High Speed                                       ║              ║             ║
║              ║              ║ <                                                  ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║     Cons:                                          ║              ║             ║
║              ║              ║ < Average Attack                                   ║              ║             ║
║           ═══╬═══           ║ < Low Maana                                        ║           ═══╬═══          ║
║              ║              ║ < Low Mana Regeneration                            ║              ║             ║
║              ║              ║ < Low Critical Chance                              ║              ║             ║
║                             ║                                                    ║                            ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║           Enter to continue or 0 to skip           ║                            ║
╚═════════════════════════════╩════════════════════════════════════════════════════╩════════════════════════════╝
    '''.format( txt(lancerTxt, 50, 1), txt(lancerTxt, 50, 2),
                txt(lancerTxt, 50, 3), txt(lancerTxt, 50, 4),
                txt(lancerTxt, 50, 5), txt(lancerTxt, 50, 6),
                txt(lancerTxt, 50, 7), txt(lancerTxt, 50, 8),
                txt(lancerTxt, 50, 9), txt(lancerTxt, 50, 10) ))
    nan = input("<<")
    clear()
    if nan == '0':
        return
    print('''
╔═════════════════════════════╦════════════════════════════════════════════════════╦════════════════════════════╗
║                             ║ Hero Class: Caster                                 ║                            ║
║                             ║                                                    ║                            ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║           ═══╬═══           ║ {} ║           ═══╬═══          ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║                             ║                                                    ║                            ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║     Pros:                                          ║                            ║
║                             ║ < High Physical Defense                            ║                            ║
║              ║              ║ < High Magic Defense                               ║              ║             ║
║              ║              ║ < High Speed                                       ║              ║             ║
║              ║              ║ <                                                  ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║     Cons:                                          ║              ║             ║
║              ║              ║ < Average Attack                                   ║              ║             ║
║           ═══╬═══           ║ < Low Maana                                        ║           ═══╬═══          ║
║              ║              ║ < Low Mana Regeneration                            ║              ║             ║
║              ║              ║ < Low Critical Chance                              ║              ║             ║
║                             ║                                                    ║                            ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║           Enter to continue or 0 to skip           ║                            ║
╚═════════════════════════════╩════════════════════════════════════════════════════╩════════════════════════════╝
    '''.format( txt(casterTxt, 50, 1), txt(casterTxt, 50, 2),
                txt(casterTxt, 50, 3), txt(casterTxt, 50, 4),
                txt(casterTxt, 50, 5), txt(casterTxt, 50, 6),
                txt(casterTxt, 50, 7), txt(casterTxt, 50, 8),
                txt(casterTxt, 50, 9), txt(casterTxt, 50, 10) ))
    nan = input("<<")
    clear()
    if nan == '0':
        return
    print('''
╔═════════════════════════════╦════════════════════════════════════════════════════╦════════════════════════════╗
║                             ║ Hero Class: Berserker                              ║                            ║
║                             ║                                                    ║                            ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║           ═══╬═══           ║ {} ║           ═══╬═══          ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║                             ║                                                    ║                            ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║     Pros:                                          ║                            ║
║                             ║ < High Physical Defense                            ║                            ║
║              ║              ║ < High Magic Defense                               ║              ║             ║
║              ║              ║ < High Speed                                       ║              ║             ║
║              ║              ║ <                                                  ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║     Cons:                                          ║              ║             ║
║              ║              ║ < Average Attack                                   ║              ║             ║
║           ═══╬═══           ║ < Low Maana                                        ║           ═══╬═══          ║
║              ║              ║ < Low Mana Regeneration                            ║              ║             ║
║              ║              ║ < Low Critical Chance                              ║              ║             ║
║                             ║                                                    ║                            ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║           Enter to continue or 0 to skip           ║                            ║
╚═════════════════════════════╩════════════════════════════════════════════════════╩════════════════════════════╝
    '''.format( txt(berserkerTxt, 50, 1), txt(berserkerTxt, 50, 2),
                txt(berserkerTxt, 50, 3), txt(berserkerTxt, 50, 4),
                txt(berserkerTxt, 50, 5), txt(berserkerTxt, 50, 6),
                txt(berserkerTxt, 50, 7), txt(berserkerTxt, 50, 8),
                txt(berserkerTxt, 50, 9), txt(berserkerTxt, 50, 10) ))
    nan = input("<<")
    clear()
    if nan == '0':
        return
    print('''
╔═════════════════════════════╦════════════════════════════════════════════════════╦════════════════════════════╗
║                             ║ Hero Class: Assassin                               ║                            ║
║                             ║                                                    ║                            ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║           ═══╬═══           ║ {} ║           ═══╬═══          ║
║              ║              ║ {} ║              ║             ║
║              ║              ║ {} ║              ║             ║
║                             ║                                                    ║                            ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║     Pros:                                          ║                            ║
║                             ║ < High Physical Defense                            ║                            ║
║              ║              ║ < High Magic Defense                               ║              ║             ║
║              ║              ║ < High Speed                                       ║              ║             ║
║              ║              ║ <                                                  ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║     Cons:                                          ║              ║             ║
║              ║              ║ < Average Attack                                   ║              ║             ║
║           ═══╬═══           ║ < Low Maana                                        ║           ═══╬═══          ║
║              ║              ║ < Low Mana Regeneration                            ║              ║             ║
║              ║              ║ < Low Critical Chance                              ║              ║             ║
║                             ║                                                    ║                            ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║           Enter to continue or 0 to skip           ║                            ║
╚═════════════════════════════╩════════════════════════════════════════════════════╩════════════════════════════╝
    '''.format( txt(assassinTxt, 50, 1), txt(assassinTxt, 50, 2),
                txt(assassinTxt, 50, 3), txt(assassinTxt, 50, 4),
                txt(assassinTxt, 50, 5), txt(assassinTxt, 50, 6),
                txt(assassinTxt, 50, 7), txt(assassinTxt, 50, 8),
                txt(assassinTxt, 50, 9), txt(assassinTxt, 50, 10) ))
    nan = input("<<")
    clear()
    if nan == '0':
        return
    print('''
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                               ║
║                   .______________________________________________________|_._._._._._._._._._.                ║
║                    \_____________________________________________________|_|_|_|_|_|_|_|_|_|_|                ║
║                                                                          l                                    ║
║                                                                                                               ║
║                                  One hero will be choosen to fight for you...                                 ║
║                                     And another will fight against you!                                       ║
║                                                 GET READY!                                                    ║
║                                                                                                               ║
║                   ._._._._._._._._._|__________________________________________________________.              ║
║                   |_|_|_|_|_|_|_|_|_|_________________________________________________________/               ║
║                                     l                                                                         ║
║                                                                                                               ║
╠═════════════════════════════╦════════════════════════════════════════════════════╦════════════════════════════╣
║ /\/\/\/\/\/\/\/\/\/\/\/\/\/ ║                Enter to continue ...               ║ \/\/\/\/\/\/\/\/\/\/\/\/\/ ║
╚═════════════════════════════╩════════════════════════════════════════════════════╩════════════════════════════╝
    ''')
    input("<<")
    clear()



def help():
    print('''
╔═════════════════════════════╦════════════════════════════════════════════════════╦════════════════════════════╗
║                             ║ Help Menu                                          ║                            ║
║                             ║                                                    ║                            ║
║              ║              ║ In every screen, if you enter ? it should appear   ║              ║             ║
║              ║              ║ a help menu. The characters are probably not       ║              ║             ║
║              ║              ║ balanced. If you have any questions about Fate     ║              ║             ║
║              ║              ║ simply watch it. Or if you have o lot of spare     ║              ║             ║
║              ║              ║ time then make sure you read the original visual   ║              ║             ║
║              ║              ║ novels! Any questions about how I made this game,  ║              ║             ║
║           ═══╬═══           ║ please contact me.                                 ║           ═══╬═══          ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║                  lvenk26@gmail.com                 ║              ║             ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║           Enter ? for help or 0 to quit            ║                            ║
╚═════════════════════════════╩════════════════════════════════════════════════════╩════════════════════════════╝
[Help Menu] :
Hello and welcome to my very first game I've ever made.
This game tries to simulate the Battle for the Graal.
This battle shows up in the Fate Series.
If you haven't watched it then now is your chance!

Press enter to continue...
    ''')
    input()

def menu():
    print('''
╔═════════════════════════════╦════════════════════════════════════════════════════╦════════════════════════════╗
║                             ║ Main Menu                                          ║                            ║
║                             ║                                                    ║                            ║
║              ║              ║ a (A) About this game                              ║              ║             ║
║              ║              ║ c (C) Credits                                      ║              ║             ║
║              ║              ║ r (R) Release Notes                                ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║ [Game Modes]                                       ║              ║             ║
║              ║              ║ 1 - Single Combat                                  ║              ║             ║
║           ═══╬═══           ║ 2 - Story Mode                                     ║           ═══╬═══          ║
║              ║              ║ 3 - Sandbox Mode                                   ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║                 Enter 0 to quit ...                ║                            ║
╚═════════════════════════════╩════════════════════════════════════════════════════╩════════════════════════════╝
    ''')


def credits():
    print('''
╔═════════════════════════════╦════════════════════════════════════════════════════╦════════════════════════════╗
║                             ║ Credits                                            ║                            ║
║                             ║                                                    ║                            ║
║              ║              ║ Swords : http://ascii.co.uk/art/swords             ║              ║             ║
║              ║              ║ Castle : http://ascii.co.uk/art/castles            ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║           ═══╬═══           ║                                                    ║           ═══╬═══          ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║               Enter to continue ...                ║                            ║
╚═════════════════════════════╩════════════════════════════════════════════════════╩════════════════════════════╝
        ''')


def about():
    print('''
╔═════════════════════════════╦════════════════════════════════════════════════════╦════════════════════════════╗
║                             ║ About Menu                                         ║                            ║
║                             ║                                                    ║                            ║
║              ║              ║ Hello and welcome to my very first game I've ever  ║              ║             ║
║              ║              ║ made! This game tries to simulate the Battle for   ║              ║             ║
║              ║              ║ the Graal. This battle shows up in the Fate Series ║              ║             ║
║              ║              ║ If you haven't watched it then now is your chance! ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║ This game is under development. Any sugestions     ║              ║             ║
║           ═══╬═══           ║ please contact me! I'm very new to game making...  ║           ═══╬═══          ║
║              ║              ║                                                    ║              ║             ║
║              ║              ║                                                    ║              ║             ║
║                             ╠════════════════════════════════════════════════════╣                            ║
║                             ║               Enter to continue ...                ║                            ║
╚═════════════════════════════╩════════════════════════════════════════════════════╩════════════════════════════╝
        ''')



def releaseNotes():
    print('''
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ Release Notes                                                                                                 ║
║                                                                                                               ║
║ 27/12/2017                                                                                                    ║
║ New Layout added to the game                                                                                  ║
║ Simple Animations added to the game                                                                           ║
║                                                                                                               ║
║ 26/12/2017                                                                                                    ║
║ < Beginning of game development                                                                               ║
║                                                                                                               ║
╠═════════════════════════════╦════════════════════════════════════════════════════╦════════════════════════════╣
║ /\/\/\/\/\/\/\/\/\/\/\/\/\/ ║               Enter to continue ...                ║ \/\/\/\/\/\/\/\/\/\/\/\/\/ ║
╚═════════════════════════════╩════════════════════════════════════════════════════╩════════════════════════════╝
        ''')










            
