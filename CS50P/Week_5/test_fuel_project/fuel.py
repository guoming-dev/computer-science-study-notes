def main():
    # Continuously prompt user for input until valid
    while True:
        try:
            # Get input and split it into numerator and denominator
            fraction = input("Fraction: ")
            percentage = gauge(convert(fraction))
            print(f"{percentage}")
            # Exit the loop once a valid fraction is processed
            break

        except (ValueError, ZeroDivisionError):
            # If invalid input, re-prompt the user
            pass

def convert(fraction):
    if not isinstance(fraction, str):
        raise ValueError

    X, Y = fraction.split("/")

    # Convert input values to integers
    X = int(X)
    Y = int(Y)

    if Y == 0:
        raise ZeroDivisionError

    # Validate that the fraction is proper
    if X > Y:
        raise ValueError

    return round((X / Y) * 100)

def gauge(percentage):
    # Round the percentage first
    rounded_percentage = round(percentage)
    # Determine the appropriate output
    if rounded_percentage <= 1:
        return "E"
    elif rounded_percentage >= 99:
        return "F"
    else:
        return f"{rounded_percentage}%"

if __name__ == "__main__":
    main()
