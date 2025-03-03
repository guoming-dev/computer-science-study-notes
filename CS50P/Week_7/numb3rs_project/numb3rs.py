import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    """
    Function to validate an IPv4 address using regular expressions.
    Returns True if valid, otherwise False.
    """

    # Step 1: Immediately reject empty input
    if ip == "":
        return False

    # Step 2: Define regex pattern for a valid IPv4 address
    pattern = r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$'

    # Step 3: Match input IP against the regex pattern
    match = re.match(pattern, ip)
    if not match:
        return False  # Return False if IP does not match pattern

    # Step 4: Extract the four octets from the match
    octets = match.groups()

    for octet in octets:
        # Step 5: Convert octet to integer and check range
        if not 0 <= int(octet) <= 255:
            return False  # Out of valid range

        # Step 6: Ensure no leading zeros unless it's exactly "0"
        if octet != "0" and octet.startswith("0"):
            return False  # Invalid leading zero

    return True  # If all checks pass, return True

if __name__ == "__main__":
    main()
