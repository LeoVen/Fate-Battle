from support import *



def attackMode():
    print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\t║                                                                                               ║
\t║\t\t\t\t\tAttack Mode\t\t\t\t\t\t║
\t║                                                                                               ║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
\t    Choose your attack. Enter ? for help. Enter 0 to return
                    ''')


def playersTurn():
    print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\t║\t\t\t\t\tPlayer's Turn\t\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
        ''')

def enemysTurn():
    print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\t║\t\t\t\t\tEnemy's Turn\t\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
        ''')


def printPossibleAttacks(sk1, sk2, sk3, sk4, sk5, sk6, sk7, sk8, sk9, sk10):
    while True:
        clear()
        print('''
            [Hotkey][Detail]        Attack Hotkeys.
\t╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
\t║\t\t\t\t\t\t\t\t\t\t\t\t\t\t║
\t║\t[A, a]   Physical Attack\t\t\t\t\t\t\t\t\t\t║
\t║\t[M, m]   Magical Attack\t\t\t\t\t\t\t\t\t\t\t║
\t║\t[][R, r] Return\t\t\t\t\t\t\t\t\t\t\t\t║
\t║\t[0][0.?] Skill {}\t\t\t\t\t\t\t\t\t║
\t║\t[1][1.?] Skill {}\t\t\t\t\t\t\t\t\t║
\t║\t[2][2.?] Skill {}\t\t\t\t\t\t\t\t\t║
\t║\t[3][3.?] Skill {}\t\t\t\t\t\t\t\t\t║
\t║\t[4][4.?] Skill {}\t\t\t\t\t\t\t\t\t║
\t║\t[5][5.?] Skill {}\t\t\t\t\t\t\t\t\t║
\t║\t[6][6.?] Skill {}\t\t\t\t\t\t\t\t\t║
\t║\t[7][7.?] Skill {}\t\t\t\t\t\t\t\t\t║
\t║\t[8][8.?] Skill {}\t\t\t\t\t\t\t\t\t║
\t║\t[9][9.?] Skill {}\t\t\t\t\t\t\t\t\t║
\t║\t\t\t\t\t\t\t\t\t\t\t\t\t\t║
\t╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
            '''.format( strP(sk1.NAME, 20), strP(sk2.NAME, 20), strP(sk3.NAME, 20),
                        strP(sk4.NAME, 20), strP(sk5.NAME, 20), strP(sk6.NAME, 20),
                        strP(sk7.NAME, 20), strP(sk8.NAME, 20), strP(sk9.NAME, 20),
                        strP(sk10.NAME, 20)))

        n = input("<<")
        if n == 'r' or n == 'R':
            break
        elif n == '0.?':
            clear()
            listSkill(sk1)
        elif n == '1.?':
            clear()
            listSkill(sk2)
        elif n == '2.?':
            clear()
            listSkill(sk3)
        elif n == '3.?':
            clear()
            listSkill(sk4)
        elif n == '4.?':
            clear()
            listSkill(sk5)
        elif n == '5.?':
            clear()
            listSkill(sk6)
        elif n == '6.?':
            clear()
            listSkill(sk7)
        elif n == '7.?':
            clear()
            listSkill(sk8)
        elif n == '8.?':
            clear()
            listSkill(sk9)
        elif n == '9.?':
            clear()
            listSkill(sk10)
        enterToContinue()







def smallMenu(ally, enemy):
	print('''
╔═══════════════════════════════════════════════════════╦═══════════════════════════════════════════════════════╗
║\t\t\t\t\t\t\t║\t\t\t\t\t\t\t║
║\tPLAYER\t\t\t\t\t\t║\tENEMY\t\t\t\t\t\t║
║\tHero Class : {}\t\t\t\t║\tHero Class : {}\t\t\t\t║
║\tHit Points : {} {}\t║\tHit Points : {} {}\t║
║\tTotal Mana : {} {}\t║\tTotal Mana : {} {}\t║
║\t\t\t\t\t\t\t║\t\t\t\t\t\t\t║
╚═══════════════════════════════════════════════════════╩═══════════════════════════════════════════════════════╝
		'''.format(	ally.CNAME,	    enemy.CNAME,
					int(ally.HP),	ally.hpBar(),
					int(enemy.HP),	enemy.hpBar(),
					int(ally.MN),	ally.manaBar(),
					int(enemy.MN),	enemy.manaBar()
					))



def commandMenu():
    clear()
    print('''
        Command Menu
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                               ║
║ Here are your options:                                                                                        ║
║                                                                                                               ║
║   0 - Return to Main Menu                                                                                     ║
║                                                                                                               ║
║   [Listing Options]                     [Misc Options]                [Combat Options]                        ║
║   k (K) - Battle Summary                ? - Shows this help menu      a (A) - Attack Mode                     ║
║   m (M) - Shows Comparison Menu                                          ├─ l (L) - Lists possible attacks    ║
║   l (L) - List your hero's skills                                        ├─ s (S) - Uses a Character's Skill  ║
║   c (C) - Show Character's Details                                       ├─ r (R) - Return                    ║
║   e (E) - Show Enemy's Details                                           ├─ p (P) - Physical Attack           ║
║   b (B) - Show your hero's buffs                                         └─ m (M) - Magical Attack            ║
║   d (D) - Show your hero's debuffs                                                                            ║
║                                                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        ''')
    enterToContinue()



def heroInfo(ally):
    clear()
    print('''
        Hero Info
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                               ║
║\tClass            : {}\t\t\t\t\t\t\t\t\t║
║\tName             : {}\t\t\t\t\t\t\t\t\t║
║\tHit Points       : {}\t\t\t\t\t\t\t\t\t║
║\tMana             : {}\t\t\t\t\t\t\t\t\t║
║\tHealth Regen     : {}\t\t\t\t\t\t\t\t\t║
║\tMana Regen       : {}\t\t\t\t\t\t\t\t\t║
║\tPhysical Attack  : {}\t\t\t\t\t\t\t\t\t║
║\tMagical Attack   : {}\t\t\t\t\t\t\t\t\t║
║\tPhysical Defense : {}\t\t\t\t\t\t\t\t\t║
║\tMagical Defense  : {}\t\t\t\t\t\t\t\t\t║
║\tSpeed            : {}\t\t\t\t\t\t\t\t\t║
║\tCritical Chance  : {}\t\t\t\t\t\t\t\t\t║
║                                                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    '''.format( strP(ally.CNAME, 20), strP(ally.NAME, 20),
                strP(ally.HP, 20),    strP(ally.MN, 20),
                strP(ally.HR, 20),    strP(ally.MR, 20),
                strP(ally.PA, 20),    strP(ally.MA, 20),
                strP(ally.PD, 20),    strP(ally.MD, 20),
                strP(ally.SP, 20),    strP(ally.CR, 20)))
    enterToContinue()


def showBuffs(ally):
    clear()
    print('''
\t\tBuffs
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\t║\t< HP >\t< MN >\t< HR >\t< MR >\t< PA >\t< MA >\t< PD >\t< MD >\t< SP >\t< CR >\t\t║
\t║\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
\t  Note: 100 means that your Hero's skills are 100%, that is, no buffs or debuffs
    '''.format( ally.bHP,    ally.bMN,
                ally.bHR,    ally.bMR,
                ally.bPA,    ally.bMA,
                ally.bPD,    ally.bMD,
                ally.bSP,     ally.bCR))
    enterToContinue()



def showDebuffs(ally):
    clear()
    print('''
\t\tDebuffs
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\t║\t< HP >\t< MN >\t< HR >\t< MR >\t< PA >\t< MA >\t< PD >\t< MD >\t< SP >\t< CR >\t\t║
\t║\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
\t  Note: 0 means that your Hero's skills are 100%, that is, no buffs or debuffs
    '''.format( ally.dHP,    ally.dMN,
                ally.dHR,    ally.dMR,
                ally.dPA,    ally.dMA,
                ally.dPD,    ally.dMD,
                ally.dSP,     ally.dCR))
    enterToContinue()



def listSkills(sk1, sk2, sk3, sk4, sk5, sk6, sk7, sk8, sk9, sk10):
    clear()
    arr = [sk1, sk2, sk3, sk4, sk5, sk6, sk7, sk8, sk9, sk10]
    for i in range(len(arr)):
        listSkill(arr[i])
    enterToContinue()


def listSkill(sk):
    print('''
\t\tSkill Name : {}\tID : {}
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║\t\t\t\t\t\t\t\t\t\t\t\t\t\t║
║\t{}\t\t║
║\t\t\t\t\t\t\t\t\t\t\t\t\t\t║
║\t< Cost                        : {}\t\t\t\t\t\t\t\t║
║\t< Physical Damage             : {}\t\t\t\t\t\t\t\t║
║\t< Magic Damage                : {}\t\t\t\t\t\t\t\t║
║\t\t\t\t\t\t\t\t\t\t\t\t\t\t║
║\t  Buffs\t\t\t\t\t\t\t\t\t\t\t\t\t║
║\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗\t║
║\t║\t< HP >\t< MN >\t< HR >\t< MR >\t< PA >\t< MA >\t< PD >\t< MD >\t< SP >\t< CR >  \t║\t║
║\t║\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t\t║\t║
║\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝\t║
║\t\t\t\t\t\t\t\t\t\t\t\t\t\t║
║\t  Debuffs\t\t\t\t\t\t\t\t\t\t\t\t║
║\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗\t║
║\t║\t< HP >\t< MN >\t< HR >\t< MR >\t< PA >\t< MA >\t< PD >\t< MD >\t< SP >\t< CR >  \t║\t║
║\t║\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t\t║\t║
║\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝\t║
║\t\t\t\t\t\t\t\t\t\t\t\t\t\t║
║\t< Extra Attacks               : {}\t\t\t\t\t\t\t\t║
║\t< Disables Attack After Use   : {}\t\t\t\t\t\t\t\t║
║\t< Disables Defense After Use  : {}\t\t\t\t\t\t\t\t║
║\t< Disables Skills After Use   : {}\t\t\t\t\t\t\t\t║
║\t< Turns of Effect             : {}\t\t\t\t\t\t\t\t║
║\t< Ignores Enemy's Speed       : {}\t\t\t\t\t\t\t\t║
║\t\t\t\t\t\t\t\t\t\t\t\t\t\t║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        '''.format( strP(sk.NAME, 20),  sk.ID,              strP(sk.DESC, 90),  strP(sk.COST, 10),
                    strP(sk.DMG, 10),   strP(sk.MAG, 10),   sk.B_HP,            sk.B_MN,
                    sk.B_HR,            sk.B_MR,            sk.B_PA,            sk.B_MA,            sk.B_PD,
                    sk.B_MD,            sk.B_SP,            sk.B_CR,            sk.D_HP,            sk.D_MN,
                    sk.D_HR,            sk.D_MR,            sk.D_PA,            sk.D_MA,            sk.D_PD,
                    sk.D_MD,            sk.D_SP,            sk.D_CR,            strP(sk.EXTRA, 10),
                    strP(sk.DA, 10),    strP(sk.DD, 10),    strP(sk.DS, 10),    strP(sk.TURNS, 10),
                    strP(sk.IGSP, 10)))


def battleInfo(ally, enemy):
    clear()
    d = 100
    print('''
\t\tBattle Summary
╔═══════════════════════════════════════════════════════╦═══════════════════════════════════════════════════════╗
║\t\t\t\t\t\t\t║\t\t\t\t\t\t\t║
║ \t\t<< PLAYER >>\t \t\t\t║\t\t<< ENEMY >>\t \t\t\t║
║ \tClass\t\t\t: {}\t\t║\tClass\t\t\t: {}\t\t║
║ \tName\t\t\t: {}\t║\tName\t\t\t: {}\t║
║ \tHit Points\t\t: {}\t\t{}%\t║\tHit Points\t\t: {}\t\t{}%\t║
║ \tMana\t\t\t: {}\t\t{}%\t║\tMana\t\t\t: {}\t\t{}%\t║
║ \tHealth Regen\t\t: {}%\t\t{}%\t║\tHealth Regen\t\t: {}%\t\t{}%\t║
║ \tMana Regen\t\t: {}%\t\t{}%\t║\tMana Regen\t\t: {}%\t\t{}%\t║
║ \tPhysical Attack\t\t: {}\t\t{}%\t║\tPhysical Attack\t\t: {}\t\t{}%\t║
║ \tMagical Attack\t\t: {}\t\t{}%\t║\tMagical Attack\t\t: {}\t\t{}%\t║
║ \tPhysical Defense\t: {}%\t\t{}%\t║\tPhysical Defense\t: {}%\t\t{}%\t║
║ \tMagical Defense\t\t: {}%\t\t{}%\t║\tMagical Defense\t\t: {}%\t\t{}%\t║
║ \tSpeed\t\t\t: {}\t\t{}%\t║\tSpeed\t\t\t: {}\t\t{}%\t║
║ \tCritical Hit\t\t: {}%\t\t{}%\t║\tCritical Hit\t\t: {}%\t\t{}%\t║
║\t\t\t\t\t\t\t║\t\t\t\t\t\t\t║
╚═══════════════════════════════════════════════════════╩═══════════════════════════════════════════════════════╝
    '''.format(ally.CNAME, enemy.CNAME,
               ally.NAME,  enemy.NAME,
               int(ally.HP),   int(ally.bHP - ally.dHP - d),    int(enemy.HP),    int(enemy.bHP - enemy.dHP - d),
               int(ally.MN),   int(ally.bMN - ally.dMN - d),    int(enemy.MN),    int(enemy.bMN - enemy.dMN - d),
               int(ally.HR),   int(ally.bHR - ally.dHR - d),    int(enemy.HR),    int(enemy.bHR - enemy.dHR - d),
               int(ally.MR),   int(ally.bMR - ally.dMR - d),    int(enemy.MR),    int(enemy.bMR - enemy.dMR - d),
               int(ally.PA),   int(ally.bPA - ally.dPA - d),    int(enemy.PA),    int(enemy.bPA - enemy.dPA - d),
               int(ally.MA),   int(ally.bMA - ally.dMA - d),    int(enemy.MA),    int(enemy.bMA - enemy.dMA - d),
               int(ally.PD),   int(ally.bPD - ally.dPD - d),    int(enemy.PD),    int(enemy.bPD - enemy.dPD - d),
               int(ally.MD),   int(ally.bMD - ally.dMD - d),    int(enemy.MD),    int(enemy.bMD - enemy.dMD - d),
               int(ally.SP),   int(ally.bSP - ally.dSP - d),    int(enemy.SP),    int(enemy.bSP - enemy.dSP - d),
               int(ally.CR),   int(ally.bCR - ally.dCR - d),    int(enemy.CR),    int(enemy.bCR - enemy.dCR - d)
               ))
    enterToContinue()



def comparisonMenu(ally, enemy):
    clear()
    print('''
\t\t\t < HP >\t < MN >\t < HR >\t < MR >\t < PA >\t < MA >\t < PD >\t < MD >\t < SP >\t < CR >
\t\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\tAlly\t║\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t\t║
\t\t╠═══════════════════════════════════════════════════════════════════════════════════════════════╣
\tEnemy\t║\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t\t║
\t\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
        '''.format(
                int(ally.HP), int(ally.MN), int(ally.HR), int(ally.MR), int(ally.PA),
                int(ally.MA), int(ally.PD), int(ally.MD), int(ally.SP), int(ally.CR),
                int(enemy.HP), int(enemy.MN), int(enemy.HR), int(enemy.MR), int(enemy.PA),
                int(enemy.MA), int(enemy.PD), int(enemy.MD), int(enemy.SP), int(enemy.CR),))
    enterToContinue()


def enterToContinue():
    print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\t║\t\t\t\tPress Enter to Continue ...\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
        ''')
    input("<<")


def chooseSkill(sk1, sk2, sk3, sk4, sk5, sk6, sk7, sk8, sk9, sk10):
    clear()
    print('''
\t╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
\t║\t\t\t\tChoose a Skill ...\t\t\t\t\t\t║
\t╚═══════════════════════════════════════════════════════════════════════════════════════════════╝
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║\t\t\t\t\t\t\t\t\t\t\t\t\t\t║
║\t[Choose]\t\t\t\t\t\t\t\t\t\t\t\t║
║\t[R, r] Return\t\t\t\t\t\t\t\t\t\t\t\t║
║\t[0] Skill {}\t: {}\t\t\t\t\t\t\t\t║
║\t[1] Skill {}\t: {}\t\t\t\t\t\t\t\t║
║\t[2] Skill {}\t: {}\t\t\t\t\t\t\t\t║
║\t[3] Skill {}\t: {}\t\t\t\t\t\t\t\t║
║\t[4] Skill {}\t: {}\t\t\t\t\t\t\t\t║
║\t[5] Skill {}\t: {}\t\t\t\t\t\t\t\t║
║\t[6] Skill {}\t: {}\t\t\t\t\t\t\t\t║
║\t[7] Skill {}\t: {}\t\t\t\t\t\t\t\t║
║\t[8] Skill {}\t: {}\t\t\t\t\t\t\t\t║
║\t[9] Skill {}\t: {}\t\t\t\t\t\t\t\t║
║\t\t\t\t\t\t\t\t\t\t\t\t\t\t║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
        '''.format( strP(sk1.NAME, 20),  strP(sk1.COST, 7),  strP(sk2.NAME, 20),  strP(sk2.COST, 7),
                    strP(sk3.NAME, 20),  strP(sk3.COST, 7),  strP(sk4.NAME, 20),  strP(sk4.COST, 7),
                    strP(sk5.NAME, 20),  strP(sk5.COST, 7),  strP(sk6.NAME, 20),  strP(sk6.COST, 7),
                    strP(sk7.NAME, 20),  strP(sk7.COST, 7),  strP(sk8.NAME, 20),  strP(sk8.COST, 7),
                    strP(sk9.NAME, 20),  strP(sk9.COST, 7),  strP(sk10.NAME, 20), strP(sk10.COST, 7)))
    c = input("<<")
    return c