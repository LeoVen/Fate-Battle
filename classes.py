from random import randint
from skills import *
from stats import classNameArr, charNameArr
from support import *
from fightLog import *

class Hero:
	
	def __init__(self, i_d, hp, mana, hpReg, manaReg, pattack, mattack, pdefense, mdefense, speed, crit):

		#PROTOTYPES -/ Original Values
		self.pHP = hp
		self.pMN = mana
		self.pHR = hpReg
		self.pMR = manaReg
		self.pPA = pattack
		self.pMA = mattack
		self.pPD = pdefense
		self.pMD = mdefense
		self.pSP = speed
		self.pCR = crit

		#variáveis do personagem
		self.ID = i_d
		self.HP = hp
		self.MN = mana
		self.HR = hpReg
		self.MR = manaReg
		self.PA = pattack
		self.MA = mattack
		self.PD = pdefense
		self.MD = mdefense
		self.SP = speed
		self.CR = crit
		self.CNAME = classNameArr[self.ID]
		self.NAME = charNameArr[self.ID][randint(1, 6)]

		#Buffs ou debuffs
		self.bHP = 100
		self.bMN = 100
		self.bHR = 100
		self.bMR = 100
		self.bPA = 100
		self.bMA = 100
		self.bPD = 100
		self.bMD = 100
		self.bSP = 100
		self.bCR = 100

		#Total damage received or debuffs
		self.dHP = 0
		self.dMN = 0
		self.dHR = 0
		self.dMR = 0
		self.dPA = 0
		self.dMA = 0
		self.dPD = 0
		self.dMD = 0
		self.dSP = 0
		self.dCR = 0

		#Control Variables
		self.TURN = 1
		self.DAMAGE = 0
		self.MANA = 0
		self.ATTACK = 0
		self.DEFENSE = 0
		self.SKILL = 0

		#Defining Skills
		#Creating Array of skills to make it easier
		i = 0
		self.SK = [i for i in range(10)]
		for j in range(self.ID * 10, self.ID * 10 + 10):
			self.SK[i] = Skill(	skills[j][0],  skills[j][1],  skills[j][2],  skills[j][3],
								skills[j][4],  skills[j][5],  skills[j][6],  skills[j][7],
								skills[j][8],  skills[j][9],  skills[j][10], skills[j][11],
								skills[j][12], skills[j][13], skills[j][14], skills[j][15],
								skills[j][16], skills[j][17], skills[j][18], skills[j][19],
								skills[j][20], skills[j][21], skills[j][22], skills[j][23],
								skills[j][24], skills[j][25], skills[j][26], skills[j][27],
								skills[j][28], skills[j][29], skills[j][30], skills[j][31],
								skills[j][32], skills[j][33], skills[j][34])
			i += 1


	def refresh(self):
		self.TURN = 1
		#self.DAMAGE -= int(self.pHP * self.HR / 100)
		self.DAMAGE -= self.HR
		if self.DAMAGE < 0:
			self.DAMAGE = 0
		#self.MANA -= int(self.pMN * self.MR / 100)
		self.MANA -= self.MR
		if self.MANA < 0:
			self.MANA = 0
		#self.reajustLimits()

		if self.ATTACK > 0:
			self.ATTACK -= 1
		if self.DEFENSE > 0:
			self.DEFENSE -= 1
		if self.SKILL > 0:
			self.SKILL -= 1
		if self.ATTACK < 0 or self.DEFENSE < 0 or self.SKILL < 0:
			error()
			print("Variable Error. Attack, Defense or Skill < 0 A{} D{} S{}".format(
					self.ATTACK, self.DEFENSE, self.SKILL))
			enterToContinue()
		self.updateStats()


	def hpBar(self):
		i = 0
		string = ""
		if self.HP > 5000:
			return "####################>   "
		while i < self.HP:
			string += "#"
			i += 250
		while len(string) < 25:
			string += " "
		return string


	def manaBar(self):
		i = 0
		string = ""
		if self.MN > 5000:
			return "####################>   "
		while i < self.MN:
			string += "#"
			i += 250
		while len(string) < 25:
			string += " "
		return string


	def addBuffs(self, skill):
		self.bHP += skill.B_HP
		self.bMN += skill.B_MN
		self.bHR += skill.B_HR
		self.bMR += skill.B_MR
		self.bPA += skill.B_PA
		self.bMA += skill.B_MA
		self.bPD += skill.B_PD
		self.bMD += skill.B_MD
		self.bSP += skill.B_SP
		self.bCR += skill.B_CR
		

	def addDebuffs(self, skill):
		self.dHP += skill.D_HP
		self.dMN += skill.D_MN
		self.dHR += skill.D_HR
		self.dMR += skill.D_MR
		self.dPA += skill.D_PA
		self.dMA += skill.D_MA
		self.dPD += skill.D_PD
		self.dMD += skill.D_MD
		self.dSP += skill.D_SP
		self.dCR += skill.D_CR


	def updateStats(self):
		self.HP = ( self.pHP * (self.bHP - self.dHP)  / 100 ) - self.DAMAGE
		self.MN = ( self.pMN * (self.bMN - self.dMN)  / 100 ) - self.MANA
		self.HR = self.pHR * (self.bHR - self.dHR)  / 100
		self.MR = self.pMR * (self.bMR - self.dMR)  / 100
		self.PA = self.pPA * (self.bPA - self.dPA)  / 100
		self.MA = self.pMA * (self.bMA - self.dMA)  / 100
		self.PD = self.pPD * (self.bPD - self.dPD)  / 100
		self.MD = self.pMD * (self.bMD - self.dMD)  / 100
		self.SP = self.pSP * (self.bSP - self.dSP)  / 100
		self.CR = self.pCR * (self.bCR - self.dCR)  / 100


	def updateDisables(self, skill, w):
		if w == 'u' or w == 'U':
			#User
			if skill.DuA:
				self.ATTACK += skill.TOEFF
			if skill.DuD:
				self.DEFENSE += skill.TOEFF
			if skill.DuS:
				self.SKILL += skill.TOEFF
		elif w == 'e' or w == 'E':
			#Enemy
			if skill.DeA:
				self.ATTACK += skill.TOEFF
			if skill.DeD:
				self.DEFENSE += skill.TOEFF
			if skill.DeS:
				self.SKILL += skill.TOEFF





class Skill:

	def __init__(	self, i_d, name, desc, cost, hp, mn, hr, mr, pa, ma, pd, 
					md, sp, cr, dhp, dmn, dhr, dmr, dpa, dma, dpd, dmd, dsp,
					dcr, phydmg, magdmg, exatt, dd, da, ds, dd_e, da_e, ds_e, eff, ig):
		self.ID = i_d
		self.NAME = name
		self.DESC = desc
		self.COST = cost
		self.B_HP = hp
		self.B_MN = mn
		self.B_HR = hr
		self.B_MR = mr
		self.B_PA = pa
		self.B_MA = ma
		self.B_PD = pd
		self.B_MD = md
		self.B_SP = sp
		self.B_CR = cr
		self.D_HP = dhp
		self.D_MN = dmn
		self.D_HR = dhr
		self.D_MR = dmr
		self.D_PA = dpa
		self.D_MA = dma
		self.D_PD = dpd
		self.D_MD = dmd
		self.D_SP = dsp
		self.D_CR = dcr
		self.DMG = phydmg
		self.MAG = magdmg
		self.EXTRA = exatt
		self.DuD = dd 		#Disables User
		self.DuA = da 		#Disables User
		self.DuS = ds 		#Disables User
		self.DeD = dd_e 	#Disables enemy
		self.DeA = da_e 	#Disables enemy
		self.DeS = ds_e 	#Disables enemy
		self.TOEFF = eff
		self.IGSP = ig