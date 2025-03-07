import re

def convert(s):
    # Use named groups in regex for better readabilty
    match = re.fullmatch(
        r"(?P<h1>\d{1,2})(?::(?P<m1>\d{2}))? (?P<period1>AM|PM) to (?P<h2>\d{1,2})(?::(?P<m2>\d{2}))? (?P<period2>AM|PM)",
        s
    )

    if not match:
        raise ValueError("Invalid time format")

    # Extract values using named groups
    h1 = int(match.group("h1"))
    # Defaults to 00 if minutes are missing
    m1 = int(match.group("m1")) if match.group("m1") else 0
    period1 = match.group("period1")

    h2 = int(match.group("h2"))
    # Defaults to 00 if minutes are missing
    m2 = int(match.group("m2")) if match.group("m2") else 0
    period2 = match.group("period2")

    if not (0 <= m1 < 60 and 0 <= m2 < 60):
        raise ValueError("Invalid minute format")

    # Convert to 24_hour format
    h1 = convert_to_24_hour(h1, period1)
    h2 = convert_to_24_hour(h2, period2)

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

def convert_to_24_hour(hour, period):
    # Convert 12-hour format to 24-hour format.
    if hour < 1 or hour > 12:
        raise ValueError("Invalid hour value")  # Ensure hours are between 1-12
    if period == "AM":
        return 0 if hour == 12 else hour
    else:
        return 12 if hour == 12 else hour + 12

def main():
    print(convert(input("Hours: ")))

if __name__ == "__main__":
    main()
