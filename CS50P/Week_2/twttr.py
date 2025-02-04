# 1. Prompt the user for a string of text
#    - Use input() to capture user input.
user_input = input("Enter your text: ")  # Step 1: Get input from user

# 2. Create a set of vowels
#    - Include both uppercase and lowercase vowels (A, E, I, O, U).
def remove_vowels(text):
    vowels = "AEIOUaeiou"  # Step 2: Define all vowels

    # 3. Initialize an empty string for the result
    #    - This will hold the final string after vowels are removed.
    result = ""  # Step 3: Initialize an empty result string

    # 4. Iterate over each character in the input string
    #    - Check if the character is NOT in the set of vowels.
    for char in text:  # Step 4: Loop through each character
        if char not in vowels:  # Step 4.1: Check if not a vowel
            result += char  # Step 4.2: Append non-vowel to result

    return result  # Step 4.3: Return the modified string

# 5. Print the resulting string without vowels
#    - Ensure the output retains the order of the original text.
output = remove_vowels(user_input)  # Step 5: Call function and get result
print(f"Text without vowels: {output}")  # Step 5.1: Display result