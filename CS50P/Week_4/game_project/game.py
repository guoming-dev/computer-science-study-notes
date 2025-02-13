# Import the random module
import random

# Prompt the user for a number and store it in 'level'
# - Keep prompting until the user enters a positive integer(n > 0)
while True:
    try:
        level = int(input("Level: "))   # Convert input to an integer
        if level > 0:
            break   # Exit loop if input is a valid positive integer
    except ValueError:
        pass    # Ignore errors and re-prompt.

# Generate a random integer between 1 and 'level'
# - Store this number in 'target_number'
target_number = random.randint(1, level)

# Keep prompting the user to guess the number
# - If the guess is not an integer, prompt again
# - If the guess is greater than 'target_number': print "Too large!"
# - If the guess is smaller than 'target_number': print "Too small!"
# - If the guess matches 'target_number': print "Just right!" and exit the program
while True:
    try:
        guess = int(input("Guess: "))   # Convert input to an integer
        if guess > target_number:
            print("Too large!")
        elif guess < target_number:
            print("Too small!")
        else:
            print("Just right!")
            break   # Exit the loop when the guess is correct
    except ValueError:
        pass    # Ignore errors and re-prompt.
