def main():
    # Continuously prompt user for input until valid
    while True:
        try:
            # Get input and split it into numerator and denominator
            fraction = input("Fraction: ")
            X, Y = fraction.split("/")
            
            # Convert input values to integers
            X = int(X)
            Y = int(Y)
            
            # Validate that the fraction is proper
            if X > Y:
                raise ValueError
            
            # Calculate the percentage
            percentage = (X / Y) * 100
            
            # Determine the appropriate output
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{round(percentage)}%")
            
            # Exit the loop once a valid fraction is processed
            break
        
        except (ValueError, ZeroDivisionError):
            # If invalid input, re-prompt the user
            pass

if __name__ == "__main__":
    main()