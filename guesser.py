#!/usr/bin/env python
"""
guresser.py ,by Live Liu , 2016-06-18
This program has the user guess a number between 1 and 100.
"""
import random

def main():
	# Initialize the program
	print "Guess a number between 1 and 100."
	# randomNumber = 35 for debugging only
	# Initialize guess counts
	count = 0
	randomNumber = random.randint(1,100)
	# randomNumber = 77
	found = False		# flag variable to see
						# if they guessed it 
	# Run through the guessing process
	while not found:
		userGuess = input("Your guess: ")
		if userGuess == randomNumber:
			print "You got it! yes. The number is :" + str(randomNumber)
			found = True
		elif userGuess > randomNumber:
			print "Guess lower!"
			count = count +1 	# if guess to higher count add once
		else:
			print "Guess higher!"
			count = count +1 	# if guess to lower count add once

	# Print contratulations and goodbye
	print "Thanks for play our Guess game."
	# Print times you guessed
	print "You guess "+str(count+1)+" times"

if __name__ == '__main__':
	main()