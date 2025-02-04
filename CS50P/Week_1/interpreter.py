import sys # To use sys.exit()

# Step 2.2: Split the input into exactly 3 parts (x, y, z).
def split_expression(expression):
    try:
        # Split the input into x, y, z and validate the format.
        x, y, z = expression.split()
        return x, y, z
    except ValueError:
        print("Invalid expression format! Use 'x y z' (e.g., '1 + 2').")
        sys.exit()

# Step 2.3: Verify that "y" is a valid operator (+, -, *, /).
def validate_operator(y):
    # Check if the operator is valid
    if y not in ["+", "-", "*", "/"]:
        print(f"Invalid operator '{y}'. Use one of +, -, *, /.")
        sys.exit()

# Step 2.4 and Step 3: Convert and Validate Numbers
def validate_numbers(x, z):
    # Convert x and z to integers and handle errors.
    try:
        # Step 2.4: Convert "x" and "z" to integers
        x = int(x)
        z = int(z)
        return x, z
    except ValueError:
        print("x and z must be integers.")
        sys.exit()

# Step 4: Perform Calculation
def calculate(x, y, z):
    # Perform the calculation based on the operator.
    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            # Step 2.5: If "y" is "/" (division), ensure "z" is not zero.
            if z == 0:
                print("Error: Division by zero is not allowed.")
                sys.exit()
            return x / z

# Main Function to Orchestrate the Program
def main():
    # Step 1: Prompt the user to enter an arithmetic expression in the format "x y z".
    expression = input("Expression: ")

    # Step 2: Validate the input:
    # - Step 2.1: Ensure the input is not empty.
    if not expression.strip():
        print("Invalid expression!")
        sys.exit()

    # - Step 2.2: Split the input into exactly 3 parts (x, y, z).
    x, y, z = split_expression(expression)

    # - Step 2.3: Verify that "y" is a valid operator (+, -, *, /).
    validate_operator(y)

    # - Step 2.4: Ensure "x" and "z" are integers.
    # Step 3: Parse the input
    x, z = validate_numbers(x, z)

    # Step 4: Perform the calculation based on "y":
    #   - If "y" is "+", compute x + z.
    #   - If "y" is "-", compute x - z.
    #   - If "y" is "*", compute x * y.
    #   - If "y" is "/", compute x / z.
    #   - Step 2.5: If "y" is "/" (division), ensure "z" is not zero.
    result = calculate(x, y, z)

    # Step 5: Display the result rounded to one decimal place.
    print(f"{result:.1f}")

# Program Entry Point
if __name__ == "__main__":
    main()