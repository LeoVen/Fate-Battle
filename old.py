def battleInfoOld(ally, enemy):
    print('''
\t\t\t\t\t<< Battle Summary >>
<<<<<---------------------------:-------------------------------------------------------:--------------->>>>>
<<\t\t<< PLAYER >>\t:\t\t\t\t\t<< ENEMY >>\t:
<<\tClass\t\t\t: {}\t\t\tClass\t\t\t: {}
<<\tName\t\t\t: {}\t\tName\t\t\t: {}
<<\tHit Points\t\t: {}\t\t{}%\t\tHit Points\t\t: {}\t\t\t{}%
<<\tMana\t\t\t: {}\t\t{}%\t\tMana\t\t\t: {}\t\t\t{}%
<<\tHealth Regen\t\t: {}%\t\t{}%\t\tHealth Regen\t\t: {}%\t\t\t{}%
<<\tMana Regen\t\t: {}%\t\t{}%\t\tMana Regen\t\t: {}%\t\t\t{}%
<<\tPhysical Attack\t\t: {}\t\t{}%\t\tPhysical Attack\t\t: {}\t\t\t{}%
<<\tMagical Attack\t\t: {}\t\t{}%\t\tMagical Attack\t\t: {}\t\t\t{}%
<<\tPhysical Defense\t: {}%\t\t{}%\t\tPhysical Defense\t: {}%\t\t\t{}%
<<\tMagical Defense\t\t: {}%\t\t{}%\t\tMagical Defense\t\t: {}%\t\t\t{}%
<<\tSpeed\t\t\t: {}\t\t{}%\t\tSpeed\t\t\t: {}\t\t\t{}%
<<\tCritical Hit\t\t: {}%\t\t{}%\t\tCritical Hit\t\t: {}%\t\t\t{}%
<<<<<---------------------------:-------------------------------------------------------:--------------->>>>>
    '''.format( ally.CNAME,	enemy.CNAME,
    			ally.NAME,	enemy.NAME,
    			int(ally.HP),	int(ally.bHP - 100), 	int(enemy.HP),    int(enemy.bHP - 100),
    			int(ally.MN),	int(ally.bMN - 100), 	int(enemy.MN),    int(enemy.bMN - 100),
    			int(ally.HR),	int(ally.bHR - 100), 	int(enemy.HR),    int(enemy.bHR - 100),
    			int(ally.MR),	int(ally.bMR - 100), 	int(enemy.MR),    int(enemy.bMR - 100),
    			int(ally.PA),	int(ally.bPA - 100),	int(enemy.PA),    int(enemy.bPA - 100),
    			int(ally.MA),	int(ally.bMA - 100),	int(enemy.MA),    int(enemy.bMA - 100),
    			int(ally.PD),	int(ally.bPD - 100),	int(enemy.PD),    int(enemy.bPD - 100),
    			int(ally.MD),	int(ally.bMD - 100),	int(enemy.MD),    int(enemy.bMD - 100),
    			int(ally.SP),	int(ally.bSP - 100),	int(enemy.SP),    int(enemy.bSP - 100),
    			int(ally.CR),	int(ally.bCR - 100),	int(enemy.CR),    int(enemy.bCR - 100)
                ))


def smallMenu(ally, enemy):
    print('''
<<<<<--------------------------------------------------------------------------------------------------->>>>>
<<\tPLAYER\t\t\t\t\t\t\tENEMY
<<\tHero Class : {}\t\t\t\t\tHero Class : {}
<<\tHit Points : {} {}\t\tHit Points : {} {}
<<\tTotal Mana : {} {}\t\tTotal Mana : {} {}
<<<<<--------------------------------------------------------------------------------------------------->>>>>
        '''.format( ally.CNAME, enemy.CNAME,
                    ally.HP,    ally.hpBar(),
                    enemy.HP,   enemy.hpBar(),
                    ally.MN,    ally.manaBar(),
                    enemy.MN,   enemy.manaBar()
                    ))



def printPossibleAttacksOld(sk1, sk2, sk3, sk4, sk5, sk6, sk7, sk8, sk9, sk10):
    print('''
        Attack Hotkeys.
        [Hotkey][Detail]
<<<<<--------------------------------------------------------------------------------------------------->>>>>
<<\t[A, a]   Physical Attack
<<\t[M, m]   Magical Attack
<<\t[][R, r] Return
<<\t[0][0.?] Skill {}
<<\t[1][1.?] Skill {} 
<<\t[2][2.?] Skill {}
<<\t[3][3.?] Skill {}
<<\t[4][4.?] Skill {}
<<\t[5][5.?] Skill {}
<<\t[6][6.?] Skill {}
<<\t[7][7.?] Skill {}
<<\t[8][8.?] Skill {}
<<\t[9][9.?] Skill {}
<<<<<--------------------------------------------------------------------------------------------------->>>>>
        '''.format( sk1.NAME, sk2.NAME, sk3.NAME, sk4.NAME, sk5.NAME,
                    sk6.NAME, sk7.NAME, sk8.NAME, sk9.NAME, sk10.NAME))
    while True:
        n = input("<<")
        if n == 'r' or n == 'R':
            break
        elif n == '0.?':
            listSkill(sk1)
        elif n == '1.?':
            listSkill(sk2)
        elif n == '2.?':
            listSkill(sk3)
        elif n == '3.?':
            listSkill(sk4)
        elif n == '4.?':
            listSkill(sk5)
        elif n == '5.?':
            listSkill(sk6)
        elif n == '6.?':
            listSkill(sk7)
        elif n == '7.?':
            listSkill(sk8)
        elif n == '8.?':
            listSkill(sk9)
        elif n == '9.?':
            listSkill(sk10)



def commandMenuOld():
    print('''
<<<<<--------------------------------------------------------------------------------------------------->>>>>
<< [Command Menu] Here are your options:
<<\t0 - Exit
<<\t[Listing Options]
<<\tb (B) - Show your hero's buffs
<<\tk (K) - Shows Complete Menu
<<\tl (L) - List your hero's skills
<<\tm (M) - Shows Minimal Stats Menu
<<\tc (C) - Show Character's Detail
<<\t[Misc Options]
<<\t? - Shows this help menu
<<\t1 - 
<<\t2 - 
<<\t[Combat Options]
<<\ta (A) - Perform an attack
<<\t\t# li (LI) - Lists possible attacks
<<\t\t# h (H)   - Uses an Hability
<<\t\t# r (R)   - Return

<<\tp (P) - Pass turn
<<<<<--------------------------------------------------------------------------------------------------->>>>>
        ''')


def listSkill(sk):
    print('''
        Skill Name : {}
<<<<<--------------------------------------------------------------------------------------------------->>>>>
<<\t{}
<<\t< Cost                        : {}
<<\t< Physical Damage             : {}
<<\t< Magic Damage                : {}
<<\t<< Buffs >>
<<\t╔═══════════════════════════════════════════════════════════════════════════════════════════╗
<<\t║\t< HP >\t< MN >\t< HR >\t< MR >\t< PA >\t< MA >\t< PD >\t< MD >\t< SP >\t< CR >  \t║
<<\t║\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t  {}\t\t║
<<\t╚═══════════════════════════════════════════════════════════════════════════════════════════╝
<<\t< Extra Attacks               : {}
<<\t< Disables Attack After Use   : {}
<<\t< Disables Defense After Use  : {}
<<\t< Disables Skills After Use   : {}
<<\t< Turns of Effect             : {}
<<\t< Ignores Enemy's Speed       : {}
<<<<<--------------------------------------------------------------------------------------------------->>>>>
        '''.format( sk.NAME,    sk.DESC,    sk.COST,    sk.DMG,
                    sk.MAG,     sk.B_HP,    sk.B_MN,    sk.B_HR,
                    sk.B_MR,    sk.B_PA,    sk.B_MA,    sk.B_PD,
                    sk.B_MD,    sk.B_SP,    sk.B_CR,    sk.EXTRA,
                    sk.DA,      sk.DD,      sk.DS,      sk.TURNS,   sk.IGSP))



def listSkills(sk1, sk2, sk3, sk4, sk5, sk6, sk7, sk8, sk9, sk10):
    arr = [sk1, sk2, sk3, sk4, sk5, sk6, sk7, sk8, sk9, sk10]
    for i in range(len(arr)):
        print('''
            Skill :{}
<<<<<--------------------------------------------------------------------------------------------------->>>>>
<<\t{}
<<\tCost                        : {}
<<\tPhysical Damage             : {}
<<\tMagic Damage                : {}
<<\tHit Points Buff             : {}
<<\tMana Buff                   : {}
<<\tHealth Regen Buff           : {}
<<\tMana Regen Buff             : {}
<<\tPhysical Attack Buff        : {}
<<\tMagical Attack  Buff        : {}
<<\tPhysical Defense Buff       : {}
<<\tMagical Defense Buff        : {}
<<\tSpeed Buff                  : {}
<<\tCritical Chance Buff        : {}
<<\tExtra Attacks               : {}
<<\tDisables Attack After Use   : {}
<<\tDisables Defense After Use  : {}
<<\tDisables Skills After Use   : {}
<<\tTurns of Effect             : {}
<<\tIgnores Enemy's Speed       : {}
<<<<<--------------------------------------------------------------------------------------------------->>>>>
        '''.format( arr[i].NAME,    arr[i].DESC,
                    arr[i].COST,    arr[i].DMG,
                    arr[i].MAG,     arr[i].B_HP,
                    arr[i].B_MN,    arr[i].B_HR,
                    arr[i].B_MR,    arr[i].B_PA,
                    arr[i].B_MA,    arr[i].B_PD,
                    arr[i].B_MD,    arr[i].B_SP,
                    arr[i].B_CR,    arr[i].EXTRA,
                    arr[i].DA,      arr[i].DD,
                    arr[i].DS,      arr[i].TURNS,
                    arr[i].IGSP))