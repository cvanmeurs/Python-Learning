import random


words = ["phase", "chase", "shaft", "tract", "horse", "purge", "sword", "chess", "lofty", "porch"]

randomWord = random.randint(0,len(words) - 1) # random number selected based on length of list (10); -1 needed for index 0

currentWord = words[randomWord].upper()  # convert all letters in words to upper case

# break the current word down into individual letters

wordLetter1 = currentWord[0]
wordLetter2 = currentWord[1]
wordLetter3 = currentWord[2]
wordLetter4 = currentWord[3]
wordLetter5 = currentWord[4]

remainingGuesses = 6

# repeatedly used things

def printWord():
	print(letter1, letter2, letter3, letter4, letter5)


#def checkLength():


# Welcome the player

playerName = input("Welcome to Wurdle!  Please enter your name: ").strip().capitalize()

print("Hello", playerName + "!")

letter1 = "-"
letter2 = "-"
letter3 = "-"
letter4 = "-"
letter5 = "-"

print("Today's 5-letter word is: ")
printWord()

print("You have", remainingGuesses, "guesses left!")

numCorrect = 0 # track the number of correctly guessed letters

while remainingGuesses > 0 and numCorrect < 5:

	guess = input("Take your next guess!: ").strip().upper()

	while len(guess) != 5:
		print("Word guesses must be 5 letters long.  Please try again.")
		guess = input("Take another guess: ").strip()

		if len(guess) == 5:
			print("You guessed", guess.upper() + ".")
			guess = guess.upper()

	guessLetter1 = guess[0]
	guessLetter2 = guess[1]
	guessLetter3 = guess[2]
	guessLetter4 = guess[3]
	guessLetter5 = guess[4]

	# LETTER 1
	if guessLetter1 in currentWord:
		#print(guessLetter1, "is in the current word!")
		#print(numCorrect) works
		letter1 = guessLetter1.lower()


		if guessLetter1 == wordLetter1:
			#print(guessLetter1, "is in the correct place too!")
			letter1 = guessLetter1.upper()
			numCorrect += 1

	#else:
		#print(guessLetter1, "is NOT in the current word!")

	# LETTER 2
	if guessLetter2 in currentWord:
		#print(guessLetter2, "is in the current word!")
		#print(numCorrect) works
		letter2 = guessLetter2.lower()

		if guessLetter2 == wordLetter2:
			#print(guessLetter2, "is in the correct place too!")
			letter2 = guessLetter2.upper()
			numCorrect += 1

	#else:
		#print(guessLetter2, "is NOT in the current word!")


	# LETTER 3
	if guessLetter3 in currentWord:
		#print(guessLetter3, "is in the current word!")
		#print(numCorrect) works
		letter3 = guessLetter3.lower()

		if guessLetter3 == wordLetter3:
			#print(guessLetter3, "is in the correct place too!")
			letter3 = guessLetter3.upper()
			numCorrect += 1			

	#else:
		#print(guessLetter3, "is NOT in the current word!")


	# LETTER 4
	if guessLetter4 in currentWord:
		#print(guessLetter4, "is in the current word!")
		#print(numCorrect) works
		letter4 = guessLetter4.lower()

		if guessLetter4 == wordLetter4:
			#print(guessLetter4, "is in the correct place too!")
			letter4 = guessLetter4.upper()
			numCorrect += 1

	#else:
		#print(guessLetter4, "is NOT in the current word!")


	# LETTER 5
	if guessLetter5 in currentWord:
		#print(guessLetter5, "is in the current word!")
		#print(numCorrect) works
		letter5 = guessLetter5.lower()

		if guessLetter5 == wordLetter5:
			#print(guessLetter5, "is in the correct place too!")
			letter5 = guessLetter5.upper()
			numCorrect += 1

	#else:
		#print(guessLetter5, "is NOT in the current word!")


	# subtrack 1 from remaining guesses
	remainingGuesses = remainingGuesses - 1

	printWord()


	if numCorrect == 5:
		print("You have won! Congratulations!")
		if remainingGuesses > 1 or remainingGuesses == 0:
			print("You won with", remainingGuesses, "guesses remaining!")
		else:
			print("You won with", remainingGuesses, "guess remaining!")
	else:
		print("You have", remainingGuesses, "guesses left!")
		numCorrect = 0


if remainingGuesses == 0:
	print("Better luck next time! Thanks for playing", playerName + "!")
	print("The correct word was", currentWord.upper() + ".")


