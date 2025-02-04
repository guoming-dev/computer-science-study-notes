"""
Step 1: Prompt user for camel case
1. Display a prompt to the user:
   - "Enter a variable name in camelCase format:"
2. Get user input and store it in a variable (e.g., `camel_case_input`).
3. Use a loop to ensure valid input is provided:
   - If input is valid, exit the loop.
   - If input is invalid, display an error message and prompt again.
"""
def main():
    while True:
        camel_case_input = input("Enter a variable name in camelCase format: ")
        if validate_input(camel_case_input):
            break
        print("Invalid input. Please enter a valid camelCase string.")

    # Step 4: Output the result
    print(f"camelCase: {camel_case_input}")
    print(f"snake_case: {camel_to_snake_case(camel_case_input)}")

"""
Step 2: Validate the input
1. Define a function `validate_input(input_str)`:
   - Check if the input:
     - Starts with a lowercase letter.
     - Contains only alphanumeric characters (no underscores, spaces, or special characters).
   - Return `True` if valid, otherwise `False`.
"""
def validate_input(input_str):
    # Check if the string starts with a lowercase letter
    if not input_str[0].islower():
        return False

    # Check if the string contains only alphanumeric characters
    if not input_str.isalnum():
        return False

    return True

"""
Step 3: Convert to snake_case
1. Define a function `camel_to_snake_case(camel_str)`:
   - Loop through each character in the camelCase string.
   - Add an underscore before each uppercase letter.
   - Convert uppercase letters to lowercase.
   - Append all characters to form the snake_case string.
"""
def camel_to_snake_case(camel_str):
    snake_case_str = ""

    for char in camel_str:
        if char.isupper():
            snake_case_str += "_" + char.lower()
        else:
            snake_case_str += char

    return snake_case_str

"""
Step 5: Main program logic
1. Prompt the user for input and validate it.
2. If valid, convert the input to snake_case.
3. Print the original input and the converted result.
"""
if __name__ == "__main__":
    main()