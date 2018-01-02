from random import *
import heroSelection
from time import sleep
from combatLog import *
from logs import *
from support import *
from animation import *
from fightLog import *


def combatMode():
	#Animating Creation...
	#swordAnimation()
	#swordAnimationEnemy()
	ally = heroSelection.select()
	enemy = heroSelection.select()
	clear()
	while ally.HP > 0 and enemy.HP > 0:
		exit = False
		while ally.TURN > 0:
			clear()
			smallMenu(ally, enemy)
			playersTurn()
			print("\tEnter ? to see the command menu. Enter 0 to exit")
			c = input("<<")
			if c == '0':
				exit = True
				break
			elif c == '?':
				commandMenu()
			elif c == 'l' or c == 'L':
				listSkills(	ally.SK[0], ally.SK[1], ally.SK[2],
							ally.SK[3], ally.SK[4], ally.SK[5],
							ally.SK[6], ally.SK[7], ally.SK[8],
							ally.SK[9])
			elif c == 'm' or c == 'M':
				comparisonMenu(ally, enemy)
			elif c == 'c' or c == 'C':
				heroInfo(ally)
			elif c == 'e' or c == 'E':
				heroInfo(enemy)
			elif c == 'b' or c == 'B':
				showBuffs(ally)
			elif c == 'd' or c == 'D':
				showDebuffs(ally)
			elif c == 'k' or c == 'K':
				battleInfo(ally, enemy)
			elif c == 'p' or c == 'P':
				break
			elif c == 'a' or c == 'A':
				clear()
				while True:
					#Attack Begins
					clear()
					smallMenu(ally, enemy)
					playersTurn()
					attackMode()
					att = input("<<")
					if att == '0':
						break
					elif att == '?':
						commandMenu()
					elif att == 'l' or att == 'L':
						printPossibleAttacks(	ally.SK[0], ally.SK[1], ally.SK[2],
												ally.SK[3], ally.SK[4], ally.SK[5],
												ally.SK[6], ally.SK[7], ally.SK[8],
												ally.SK[9])
					elif att == 's' or att == 'S':
						if ally.SKILL == 0:
							#Skills are available
							while True:
								skll = chooseSkill(	ally.SK[0], ally.SK[1], ally.SK[2], ally.SK[3],
													ally.SK[4], ally.SK[5], ally.SK[6], ally.SK[7],
													ally.SK[8], ally.SK[9])
								if (skll == '0' or skll == '1' or skll == '2' or skll == '3' or skll == '4' or
									skll == '5' or skll == '6' or skll == '7' or skll == '8' or skll == '9'):
									#Attack 	#Attack 	#Attack 	#Attack 	#Attack 	#Attack 	#Attack
									skll = int(skll)
									if ally.MN >= ally.SK[skll].COST:
										#Skill attack
										array = [ally, enemy]
										array = skillAttack(ally, enemy, ally.SK[skll])
										ally = array[0]
										enemy = array[1]
										break #-------------------------Successful Attack
									elif ally.MN < ally.SK[skll].COST:
										noMana()
									else:
										error()
								elif skll == 'r' or skll == 'R':
									break
								else:
									invalidOption()
						elif ally.SKILL > 0:
							skillsDisabled(ally.SKILL)
						else:
							error()
							print("Skill error. Skill Variable < 0")
							enterToContinue()
					elif att == 'p' or att == 'P':
						#Physical Attack
						array = [ally, enemy]
						array = normalAttack(ally, enemy, 'p')
						ally = array[0]
						enemy = array[1]
					elif att == 'm' or att == 'M':
						#Magical Attack
						array = [ally, enemy]
						array = normalAttack(ally, enemy, 'm')
						ally = array[0]
						enemy = array[1]
					else:
						invalidOption()
					if ally.TURN < 1:
						break
			else:
				invalidOption()

		while enemy.TURN > 0:
			enemysTurn()
			print("\tEnter ? to see the command menu. Enter 0 to exit")
			break
		ally.refresh()
		enemy.refresh()
		if exit:
			break




def checkSpeed(ally, enemy):
	hit = random()
	if ally >= enemy:
		return True
	else:
		if ally / enemy >= hit:
			#HIT
			return True
		else:
			return False


def checkCrit(cr):
	chance = random()
	if cr >= 100:
		return True
	else:
		if cr / 100 >= chance:
			return True
		else:
			return False



def skillAttack(ally, enemy, sk):

	#First Attacks and then adds buffs or debuffs
	#Checks hit or miss:
	#Checks if its an attack:
	if sk.DMG > 0 or sk.MAG > 0:
		#There is damage, calculate it ...
		if sk.IGSP == False:
			#Does not ignore speed, must check
			pas = checkSpeed(ally.SP, enemy.SP)
		else:
			pas = True
		if pas:
			#HIT
			#Check for critical hit
			crit = checkCrit(ally.CR)
			if crit:
				mod = 2 #Modifier goes up to 2
			else:
				mod = 1 #Modifier stays the same
			#If armor is higher than 100% then no damage is taken so that the enemy hp doesn't get increased
			if enemy.PD <= 100:
				enemy.DAMAGE += ( sk.DMG * (1 - enemy.PD / 100) ) * mod
			if enemy.MD <= 100:
				enemy.DAMAGE += ( sk.MAG * (1 - enemy.MD / 100) ) * mod
			ally.MANA += sk.COST
			ally.TURN -= 1
			ally.TURN += sk.EXTRA
		else:
			skillMissed()
			ally.MN -= sk.COST

	#Now calculates buffs and debuffs
	ally.addBuffs(sk)
	enemy.addDebuffs(sk)
	ally.updateStats()
	enemy.updateStats()
	ally.updateDisables(sk, 'u')
	enemy.updateDisables(sk, 'e')
	return [ally, enemy]



def normalAttack(ally, enemy, types):
	#Checking speed is mandatory
	pas = checkSpeed(ally.SP, enemy.SP)
	if pas:
		#HIT
		#Check if critical hit
		crit = checkCrit(ally.CR)
		if crit:
			mod = 2 #Modifier goes up to 2
		else:
			mod = 1 #Modifier stays the same
	else:
		ally.TURN -= 1
		skillMissed()
		return [ally, enemy]
	if types == 'p':
		#Physical attack
		#If armor is higher than 100% then no damage is taken so that the enemy hp doesn't get increased
		if enemy.PD <= 100:
			enemy.DAMAGE += ( ally.PA * (1 - enemy.PD / 100) ) * mod

	elif types == 'm':
		#Magical attack
		#If armor is higher than 100% then no damage is taken so that the enemy hp doesn't get increased
		if enemy.MD <= 100:
			enemy.DAMAGE += ( ally.MA * (1 - enemy.MD / 100) ) * mod

	else:
		error()
		print("Attack Type error")
		enterToContinue()

	ally.TURN -= 1

	#Updating
	ally.updateStats()
	enemy.updateStats()

	return [ally, enemy]