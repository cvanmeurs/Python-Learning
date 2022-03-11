# pig latin translator

# outline:
# get sentence from user
# split sentence into words
# loop through the words, convert to pig latin
# stick words back together into sentence
# output the final string



# get sentence from user
original = input("Please enter your sentence: ").strip().lower()

# split sentence into words
words = original.split()  # separates all words in the string into a list of words

# loop through the words, convert to pig latin
new_words = []

# if it starts with a vowel, just add "yay"
# otherwise move first consonant cluster to the end, and add "ay"

for word in words:  # "word" can be anything, such as x, as long as it's used consistently below
	#print(word) # prints each word of the entered sentence on its own line
	if word[0] in "aeiou": # if first letter is a vowel
		new_word = word + "yay"
		new_words.append(new_word)  # add the newly translated word to the new_words list
	else:
		vowel_pos = 0
		for letter in word:
			if letter not in "aeiou":
				vowel_pos = vowel_pos + 1 # if the letter isn't a vowel, increment first vowel position
			else:  # if it IS a vowel
				break # breaks out of the loop and returns to 'else' statement (previous indent)   BREAK!!!
				# could also use the command "continue" which redirects back to the top of the loop, skipping the rest of the loop
		cons = word[:vowel_pos]	# consonants are the word all the way up to the vowel position	
		the_rest = word[vowel_pos:] # the rest of the word is everythign from the vowel position to the end
		new_word = the_rest + cons + "ay" # reconstruct the word in pig latin
		new_words.append(new_word)

#print(new_words) # It's working!  Prints a list of the translated words.

# stick words back together into sentence

output = " ".join(new_words) # join the words together but put a space inbetween

# output the final string

print(output.capitalize() + ".")