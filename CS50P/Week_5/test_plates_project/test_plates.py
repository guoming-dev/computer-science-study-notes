from plates import is_valid


def test_length():
    # Valid lengths
    assert is_valid("CS50") == True
    assert is_valid("AA") == True
    assert is_valid("AAAAAA") == True

    # Invalid lengths
    assert is_valid("A") == False  # Too short
    assert is_valid("OUTATIME") == False  # Too long
    assert is_valid("") == False  # Empty string


def test_starts_with_two_letter():
    # Valid cases
    assert is_valid("GM168") == True
    assert is_valid("AB123") == True

    # Invalid cases
    assert is_valid("168GM") == False  # Starts with digits
    assert is_valid("1A1234") == False  # Starts with one digit, one letter
    assert is_valid("A1234") == False   # Only one starting letter
    assert is_valid("@A123") == False   # Starts with special character
    assert is_valid("A@123") == False   # Letter followed by special character
    assert is_valid("AB@123") == False  # Special character after two letters


def test_number_placement():
    # Valid placements
    assert is_valid("GM21") == True
    assert is_valid("AA123") == True

    # Invalid placements
    assert is_valid("GO210K") == False  # Letters after numbers
    assert is_valid("AB12C3") == False  # Letters after digits


def test_alnum():
    # Valid alphanumeric
    assert is_valid("GM1695") == True
    assert is_valid("AB123") == True

    # Invalid characters
    assert is_valid("GM@123") == False  # Special character
    assert is_valid("AA!123") == False  # Another special character
    assert is_valid("A B123") == False  # Space in string
    assert is_valid("AA-123") == False  # Hyphen


def test_first_num_not_zero():
    # Valid numbers
    assert is_valid("GM106") == True
    assert is_valid("AB1234") == True

    # Invalid leading zeros
    assert is_valid("GM0106") == False
    assert is_valid("AB0123") == False


def test_combined_invalid_cases():
    # Multiple invalidities in one plate
    assert is_valid("1A@34") == False  # Starts with digit, special char
    # Special char and letters after numbers
    assert is_valid("AA!12B") == False
    assert is_valid("AB C123") == False  # Space
    assert is_valid("@A123") == False  # Starts with special character
