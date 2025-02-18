def main():
    # Prompts user for input and prints the shortened version.
    user_input = input("Enter your text: ")
    print(shorten(user_input))

def shorten(word):
    # Removes vowels (A, E, I, O, U) from the given word.
    vowels = "AEIOUaeiou"
    return "".join(char for char in word if char not in vowels)

if __name__ == "__main__":
    main()
