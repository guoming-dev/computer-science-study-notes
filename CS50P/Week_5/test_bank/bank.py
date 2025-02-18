def value(greeting):
    normalized_greeting = greeting.lower()
    if normalized_greeting.startswith("hello"):
        return 0
    elif normalized_greeting.startswith("h"):
        return 20
    else:
        return 100

def main():
    user_greeting = input("Greeting: ")
    print(value(user_greeting))

if __name__ == "__main__":
    main()
