# MATH BATTLE GAME

import time
import random
import math

enemies = "mathEnemies.txt"

def pause(seconds):
    time.sleep(seconds)

# STARTING PLAYER STATS
playerHealth = 20
playerLevel = 1
playerXP = 0
playerAttack = 0
playerAttackMax = 5
playerAttackMin = playerAttackMax - 2
playerAttackCrit = math.ceil(playerAttackMax * 1.5)  # Round up to nearest whole number (ceiling)

encounterNum = 1
gameIsOver = False

# GREET PLAYER AND ENTER NAME
def greetPlayer():
	global playerName
	print("Welcome to Math Battle!")
	pause(.5)
	playerName = input("Please enter your name: ")

# CONFIRM NAME
def confirmName(): #How is this done without the global variable?
	global playerName
	print("You have entered", playerName)
	pause(.5)
	nameCorrect = input("Is this correct? (y/n)")
	while nameCorrect == "n":
		pause(1)
		playerName = input("Please enter your name again: ")
		pause(1)
		print("You have entered", playerName)
		nameCorrect = input("Is this correct? (y/n)")
	if nameCorrect == "y":
		pause(1)
		print("Hello", playerName + "!")
"""	elif nameCorrect != "y" or nameCorrect != "n":
		print("Please enter a valid response.")""" #this is not correct; needs to happen first

# SHOW CURRENT PLAYER STATS
def showCurrentPlayerStats():
	global playerHealth
	global playerLevel
	global playerXP
	global playerAttackMax
	print()
	print("Your Health is:", playerHealth)
	pause(.5)
	print("Your Level is:", playerLevel)
	pause(.5)
	print("Your Attack (max) is", playerAttackMax)
	pause(.5)
	print("Your Total XP is:", playerXP)
	print()

# ENCOUNTER
def encounter():
	global encounterNum
	print("Get ready for encounter #", encounterNum, "!")
	print()
	pause(2)
	chooseEnemy()

# READ ENEMIES FROM TEXT FILE AND ASSIGN STATS
def chooseEnemy():
	global enemyName
	global enemyHealth
	global enemyAttack
	global enemyAttackChance
	global enemyXP
	with open(enemies) as f:
		lines = f.readlines()
		# TODO: This next line can be modified by the player level to choose a set of enemies (ie lines 6-10)
		randomEnemyIndex = random.randint(2, len(lines)-1) # Skip the first two lines of the file
		enemyLine = lines[randomEnemyIndex]
		enemyInfo = enemyLine.split(" ")
		enemyName = enemyInfo[0]
		enemyHealth = int(enemyInfo[1])
		enemyAttack = int(enemyInfo[2])
		enemyAttackChance = int(enemyInfo[3])
		enemyXP = int(enemyInfo[4])
		pause(1)
		print("You have encountered", enemyName,  "!")
		pause(1)
		print(enemyName, "has", enemyHealth, "HP,", enemyAttack, "attack power and grants", enemyXP, "XP when defeated.")
		pause(2)

# MATH PROBLEM GENERATION
def mathProblem(playerLevel):
	global enemyHealth
	if playerLevel <= 2:
		#a = random.randint(0,10)
		#b = random.randint(0,10)
		a = random.randint(1, 10 * playerLevel)
		b = random.randint(1, 10 * playerLevel)	
		if gameIsOver == False:
			if enemyHealth > 0:	
				correctAnswer = a + b 
				print()
				print(a, "+", b, "= ?")
				playerInput = input("Please enter your answer and press Enter: ")
				playerAnswer = int(playerInput) #convert the typed-in response to an integer; fails if not done
				if playerAnswer == correctAnswer:
					pause(1)
					print()
					print("Correct!!!")
					pause(1)
					computeDamageToEnemy()
				elif playerAnswer != correctAnswer:
					pause(1)
					print()
					print("MISS!!!1")
					pause(.5)
					print(correctAnswer, "was the correct answer.")
	elif playerLevel > 2:
		print("Whoa your level is so high dude!")  # <---- Need higher level encounters. But this might not be the way to do it...

# AFTER BATTLE SUMMARY
def showBattleSummary():
	global playerXP
	global enemyXP
	global encounterNum
	global enemyName
	pause(1)
	print("Nice job!  You defeated the", enemyName, "!")
	pause(2)
	playerXP = playerXP + enemyXP
	print("You have gained", enemyXP, "XP!")
	pause(1)
	print("Your new XP total is", playerXP,"!")
	encounterNum = encounterNum + 1
	checkLevelUp()  # check to see if the player leveled up as a result of the XP gain

# PLAYER LEVEL UP
# TODO:  Player level up keeps occurring over and over after each battle (after XP reaches 20). FIX!
def checkLevelUp():
	global playerXP
	global playerHealth
	global playerLevel
	global playerAttackMax
	if playerXP >= 20:
		playerLevel = 2
		print("You have reached level 2!")
		pause(1)
		playerAttackMax = playerAttackMax + 1
		print("Your maximum attack value has increased by 1 to", playerAttackMax, "!")
		pause(1)
		playerHealth = 20
		print("Your health has been restored to 20!")
		pause(1)

# ENEMY TURN
def enemyTurn():
	global playerHealth
	global enemyAttack
	global enemyAttackChance
	global gameIsOver
	pause(1)
	print()
	print("Enemy turn...")
	pause(2)
	enemyHit = random.randint(0,100)
	#if gameIsOver == False   #<--- this seems to get the enemy attack stuck in a constant loop; maybe IF?  If doesn't work either.
	# need "IsEnemyTurn" boolean...?
	if enemyHit <= enemyAttackChance:
		playerHealth = playerHealth - enemyAttack
		print("The enemy attacked you for", enemyAttack, "damage!")
		pause(1)
		# Don't show the player health as a negative number
		if playerHealth < 0: 
			print("Your health is now 0!")
		elif playerHealth >= 0:
			print("Your health is now", playerHealth, "!")
		pause(1)
		determineDead()
	elif enemyHit > enemyAttackChance:
		print("The enemy attack missed!")
		pause(1)
	#elif gameIsOver == True:
		#determineDead()

# DETERMINE DEAD OR NOT
def determineDead():
	global playerHealth
	global gameIsOver
	if playerHealth <= 0:
		print("You have died.  The game is over.") 
		gameIsOver = True

# COMPUTE DAMAGE TO ENEMY
def computeDamageToEnemy():
	global enemyHealth
	global playerAttackMin
	global playerAttackMax
	global playerAttack
	# determine player attack based on their max attack and min attack
	playerAttack = random.randint(int(playerAttackMin),int(playerAttackMax))
	enemyHealth = enemyHealth - playerAttack
	print("You did", playerAttack, "damage to the enemy!")
	pause(1)
	# Don't show enemy health as a negative number.
	if enemyHealth > 0:
		print ("Enemy health is now at", enemyHealth)
	elif enemyHealth <= 0:
		print ("Enemy health is now at 0.")
	pause(1)


# ========== START GAME ========== #

pause(1)

greetPlayer()

pause(1)

confirmName()

pause(2)

showCurrentPlayerStats() # <--- Works with "global" variable declarations
#showCurrentPlayerStats(playerHealth, playerLevel, playerXP)  <--- This also works; is it better?

pause(2)

while playerHealth > 0:
	encounter()
	while enemyHealth > 0:
		mathProblem(playerLevel)
		if enemyHealth > 0:  # I had to add this or the enemy would take an additional turn even after its health was 0.
			enemyTurn() # enemy takes their turn until dead
			determineDead()  # TESTING TO SEE IF THIS WORKS HERE
	showBattleSummary()
	pause(2)
	print()
	showCurrentPlayerStats()

"""if playerHealth <= 0:
	print("The game is over.  Thanks for playing.")
	Show score leaderboard"""

