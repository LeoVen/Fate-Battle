skills = [
	[
		0,					#ID
		"Noble Phantasm",	#Skill Name
		"A devastating blast of pure energy that comes out of the sword. Also boosts all stats.",	#Description
		1000,				#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		5,	5,	5,	5,	5,	5,	5,	5,	5,	5,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		5,	5,	5,	5,	5,	5,	5,	5,	5,	5,
		500,				#Physical Damage
		1500,				#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		True,				#Disables User's Attack
		True,				#Disables User's Skills
		True,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		2,					#Turns of Effect
		True				#Ignores Speed
	],
	[
		1,					#ID
		"Armor Upgrade",	#Skill Name
		"Boosts Physical Defense and Hit Points but decreases speed",		#Description
		1000,				#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		10,	0,	0,	0,	0,	0,	55,	0,	15,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,				#Physical Damage
		0,				#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		2,					#ID
		"Blessings",					#Skill Name
		"A blessing that increases mana regen, magic attack and magic defense",	#Description
		500,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	20,	0,	30,	0,	30,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		3,					#ID
		"Rally",					#Skill Name
		"Boost your heart and soul! Increases stats but decreases health regen",	#Description
		800,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		20,	0, -10,	0,	20,	0,	0,	0,	5,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,  -5,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		4,					#ID
		"Hack & Slash",		#Skill Name
		"A double strike with increased damage",	#Description
		500,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	20,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		2,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		True,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		1,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		5,					#ID
		"Mighty Valour",	#Skill Name
		"Decreases all enemy's stats and deals some damage",		#Description
		400,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		2,	2,	2,	2,	2,	2,	2,	2,	2,	2,
		200,					#Physical Damage
		200,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		6,					#ID
		"Piercing Strike",					#Skill Name
		"Attacks with the point of the sword are deadly! Increases critical chance and deals damage", #Description
		500,				#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	10,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		600,				#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		7,					#ID
		"Rest",					#Skill Name
		"Increases Mana and Health Regeneration",		#Description
		600,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	20,	20,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		8,					#ID
		"Crushing Strike",					#Skill Name
		"An all-in strike! Deals a lot of damage but decreases speed and lowers enemy's armor",	#Description
		600,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	1,	0,	1,	0,	-10,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	2,	0,	0,	0,
		800,					#Physical Damage
		100,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		9,					#ID
		"Rush",					#Skill Name
		"Drops of parts of the armor to become faster!",			#Description
		300,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0, -20,	0,	20,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		1,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		10,					#ID
		"Noble Phantasm",					#Skill Name
		"A shot of incredibly high energy. Deals a lot of damage but has many side-effects",	#Description
		1000,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,	-1,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		2,	0,	2,	0,	0,	0,	1,	0,	1,	0,
		2000,				#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		True,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		11,					#ID
		"Concentration",					#Skill Name
		"Regains Concentration increasing Critical Chance and Speed",					#Description
		400,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	20,	20,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	2,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		12,					#ID
		"Triple Shot",					#Skill Name
		"Three successive Physical Attacks! Skills Disabled. Increases physical attack!",	#Description
		800,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	10,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		3,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		True,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		1,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		13,					#ID
		"Dead Eye",					#Skill Name
		"One Shot, One Kill. Increases Physical Attack but attacks are disabled for some time",	#Description
		800,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	80,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		True,				#Disables User's Attack
		True,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		3,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		14,					#ID
		"Deft Legs",					#Skill Name
		"Increases speed",					#Description
		500,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	20,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	5,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		15,					#ID
		"Poisonous Shot",					#Skill Name
		"Inflicts some damage but enemy gets poisoned decreasing its health regen and mana regen",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	20,	20,	0,	0,	0,	0,	0,	0,
		400,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		16,					#ID
		"Armor Breaker",					#Skill Name
		"Disables enemy's armor",					#Description
		400,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	20,	0,	0,	0,
		600,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		True,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		2,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		17,					#ID
		"String Shot",					#Skill Name
		"Ties up the enemy loosing efficiency in its attacks",					#Description
		400,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	20,	0,	0,	0,	0,	0,
		400,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		18,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		19,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		20,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		21,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		22,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		23,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		24,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		25,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		26,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		27,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		28,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		29,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		30,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		31,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		32,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		33,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		34,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		35,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		36,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		37,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		38,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		39,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		40,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		41,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		42,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		43,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		44,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		45,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		46,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		47,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		48,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		49,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		50,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		51,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		52,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		53,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		54,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		55,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		56,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		57,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		58,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		59,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		60,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		61,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		62,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		63,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		64,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		65,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		66,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		67,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		68,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
	[
		69,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0,					#Turns of Effect
		False				#Ignores Speed
	],
]

'''
	[
		0,					#ID
		"",					#Skill Name
		"",					#Description
		0,					#Cost
		#Buffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		#Debuffs
		#HP	MN	HR	MR	PA	MA	PD	MD	SP	CR
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
		0,					#Physical Damage
		0,					#Magic Damage
		0,					#Extra Attacks
		False,				#Disables User's Defense
		False,				#Disables User's Attack
		False,				#Disables User's Skills
		False,				#Disables Enemy's Defense
		False,				#Disables Enemy's Attack
		False,				#Disables Enemy's Skills
		0					#Turns of Effect
	]
'''