def is_valid(plate):
    # Step 1: Check if the length of plate is between 2 and 6
    if not (2 <= len(plate) <= 6):
        return False

    # Step 2: Ensure the plate starts with at least two letters
    if not plate[:2].isalpha():
        return False

    # Step 3: Check if numbers are at the end
    if not check_number_placement(plate):
        return False

    # Step 4: Ensure no invalid characters (letters and numbers only)
    if not plate.isalnum():
        return False

    # Step 5: Ensure the first number is not 0
    if not validate_first_number(plate):
        return False

    return True


def check_number_placement(plate):
    """
    Helper function to ensure numbers are only at the end.
    Returns True if valid, otherwise False.
    """
    found_number = False
    for char in plate:
        if char.isdigit():
            found_number = True
        elif found_number and char.isalpha():
            return False
    return True


def validate_first_number(plate):
    """
    Helper function to ensure the first number is not 0.
    Returns True if valid, otherwise False.
    """
    for char in plate:
        if char.isdigit():
            return char != '0'
    return True


# Main program logic
def main():
    """
    Main function to prompt the user for a vanity plate and
    validate it using the is_valid function.
    """
    plate = input("Enter vanity plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()