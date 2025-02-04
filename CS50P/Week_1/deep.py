# Step 1: Prompt the user for their input regarding the Great Question
# of Life
# - Use a function to get the user's input
def get_user_input():
    return input(
        "What is the Answer to the Great Question of Life,"
        "the Universe, and Everything? "
    )

# Step 2: Normalize the user's input for consistent comparison
# - Convert the input to lowercase
# - Strip any leading or trailing whitespace
def check_answer(answer):
    normalized_answer = answer.strip().lower()
    # Step 3: Check if the normalized input matches any of the following:
    # - "42"
    # - "forty-two"
    # - "forty two"
    match normalized_answer:
        # Step 4: If a match is found:
        # - Print "Yes"
        case "42" | "forty-two" | "forty two":
            return "Yes"
        # Step 5: Otherwise:
        # - Print "No"
        case _:
            return "No"

# Main logic
user_answer = get_user_input()
result = check_answer(user_answer)
print(result)