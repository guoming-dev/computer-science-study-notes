def main():
    """
    Main function to handle user input and determine meal time.
    """
    # Step 1: Prompt the user for the time
    # - Input should be stored in a variable called 'time'
    # - Example format: "7:30" or "12:00"
    time = input(
        "Please enter the time in 24-hour format (e.g., 7:30 or 12:00): ")

    # Step 2: Validate the input format
    # - Check if the input contains a colon (":").
    # - Split the input into 'hours' and 'minutes'.
    # - Ensure both parts are numeric.
    try:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)

        # Step 3: Check for out-of-range values
        # - Ensure 'hours' is between 0 and 23.
        # - Ensure 'minutes' is between 0 and 59.
        if not (0 <= hours <= 23 and 0 <= minutes <= 59):
            print("Invalid time. Please enter a valid 24-hour time.")
            return
    except ValueError:
        # Handle invalid formats (e.g., no colon, non-numeric input)
        print("Invalid format. Please use the format HH:MM.")
        return

    # Step 4: Clean and convert input to a float
    # - Use the 'convert' function to transform time into a float
    # - Example: "7:30" → 7.5
    float_time = convert(time)

    # Step 5: Determine meal time
    # - Compare the converted time (float_time) to meal ranges:
    if 7.0 <= float_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= float_time <= 13.0:
        print("lunch time")
    elif 18.0 <= float_time <= 19.0:
        print("dinner time")
    else:
        # Print nothing if it's not meal time
        pass


def convert(time):
    """
    Convert 'hours:minutes' to a float.
    Example: "7:30" → 7.5
    """
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60


if __name__ == "__main__":
    main()