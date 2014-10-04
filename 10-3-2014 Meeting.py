# Computers Club - Meeting October 3, 2014 Code

'''print "Hello World" 	# Print "Hello World" to the output console

# Variable declaration
x = 3					# int - intgers
y = 3.2 				# double - non-integer numbers
z = "Hi Michael" 		# string - text
a = True 				# boolean - true or false

# While Loop 			# While the condition in parenthesis is true
while (1 == 2):			# continue to loop and do what is indented
	print "Hi"

# For loop 				# The for loop will loop 25 times, incrementing
for i in range(25): 	# the integer i every time. i will start at 0
	print i 			# and end at 24
	print "hi"

# Conditional statement # If the condition in parenthesis is true, then
if (x == 5):			# execute whatever is indented
	print "X is 5"
elif (x == 4): 			# Else if the if condition is false and this
	print "X is 4" 		# condition is true, execute this
else: 					# If neither if nor elif is true, do this
	print "X is not 4 or 5"
	'''

import random 			# Import the random class, so you can use functions like random.seed() and random.randint(a,b)
random.seed() 			# Random numbers are pulled from a preprogrammed file in your computer, the seed chooses a
						# random position to start at, generating pseudo-random numbers

# 0 - rock, 1 - paper, 2 - scissors 		This is a layer of abstraction that makes it easier to program
player = 2 				# CHALLENGE: Figure out how to use the 'raw_input()' function and have the user enter Strings
computer = random.randint(0,2)

if (player == computer):
	print "Tie"
elif ((player+1)%3 == computer):  # Try to figure out how in this scenario, the computer always wins. It uses the modulus % symbol
	print "Computer wins"
else:
	print "Player wins"

print "Player:",player
print "Computer:",computer