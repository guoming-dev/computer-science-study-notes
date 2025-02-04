def main():
    while True:
        try:
            # Prompt user for input
            date = input("Enter a date: ").strip()

            # Check if the date is numeric (MM/DD/YYYY)
            if "/" in date:
                parts = date.split("/")
                if len(parts) != 3:
                    raise ValueError("Invalid format.")
                # Ensure all parts are numeric
                if not all(part.isdigit() for part in parts):
                    raise ValueError("Invalid format.")
                month, day, year = map(int, parts)

            elif "," in date:
                # Handle textual input (Month Day, Year)
                parts = date.split(" ", 1)
                if len(parts) != 2 or "," not in parts[1]:
                    raise ValueError("Invalid format.")
                month, day_year = parts
                day, year = map(int, day_year.replace(",", "").split())
                month = convert_month_to_number(month)
                if month == -1:
                    raise ValueError("Invalid month name.")
            else:
                raise ValueError("Invalid format.")

            # Validate the components
            if not (1 <= month <= 12 and 1 <= day <= 31 and year > 0):
                raise ValueError("Invalid date.")

            # Print the valid date in ISO 8601 format
            print(f"{year:04}-{month:02}-{day:02}")
            break  # Exit the loop once valid input is provided

        except (ValueError, IndexError):
            print("Invalid input. Please try again.")


def convert_month_to_number(month):
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }
    return months.get(month.capitalize(), -1)


if __name__ == "__main__":
    main()