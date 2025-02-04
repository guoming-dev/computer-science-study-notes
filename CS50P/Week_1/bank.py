import sys # Importing sys to use sys.exit()

# Step 1: Get user's greeting message
# - Prompt the user for input
user_greeting = input("Greeting: ")

# Step 2: Validate user's input
# - If input is empty or only spaces, print "Invalid greeting!" and exit
if not user_greeting.strip():  # - Remove leading/trailing whitespaces
    print("Invalid greeting!")
    sys.exit() # Terminate the program early if the input is invalid.

# Step 3: Normalize user's greeting message
# - Convert to lowercase
def check_greeting(greeting):
    normalized_greeting = greeting.strip().lower()
    return normalized_greeting

# Step 4: Check if the greeting message meets the requirement
# - If the message starts with "hello", print "$0"
# - Else if the message starts with "h", print "$20"
# - Else, print "Your reward is $100"
def reward(normalized_greeting):
    if normalized_greeting.startswith("hello"):
        return "$0"
    elif normalized_greeting.startswith("h"):
        return "$20"
    else:
        return "$100"

# Main program logic
normalized_greeting = check_greeting(user_greeting)
print(reward(normalized_greeting))