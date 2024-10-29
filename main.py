import random

# Guess the Dice Roll Game 
# roll = random.randint(1,6)
# guess = int(input("Guess the dice roll\n"))

# if guess == roll:
#   print("Correct! The computer rolled a " + str(roll))
# else:
#   print("Wrong! The computer rolled a " + str(roll))


# Rock, Paper, Scissors

# create variables
computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input("Do you want rock, paper, or scissors?")

# Check to see if computer choice is working properly
print('Computer choice: ', computer_choice)
