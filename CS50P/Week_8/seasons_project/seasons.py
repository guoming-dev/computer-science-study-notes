import calendar
from datetime import date
import sys
import inflect

class Person:
    def __init__(self, birthdate: str):
        # Initialize with a birthdate in YYYY-MM-DD format.
        try:
            self.birthdate = date.fromisoformat(birthdate)
        except ValueError:
            sys.exit("Invalid date")

    def is_leap_year(self, year: int) -> bool:
        # Return True if the given year is a leap year.
        return calendar.isleap(year)


    def get_minutes_since_birth(self) -> int:
        """Calculate the minutes since birth, correctly handling leap years."""
        today = date.today()
        total_minutes = 0

        # Add days from the birth date to the end of the birth year
        end_of_birth_year = date(self.birthdate.year, 12, 31)
        # Include birthdate itself
        days_birth_year = (end_of_birth_year - self.birthdate).days + 1
        total_minutes += days_birth_year * 24 * 60

        # Add minutes for full years in between
        for year in range(self.birthdate.year + 1, today.year):
            if self.is_leap_year(year):
                total_minutes += 366 * 24 * 60
            else:
                total_minutes += 365 * 24 * 60

        # Add days from the start of this year to today
        start_of_this_year = date(today.year, 1, 1)
        days_this_year = (today - start_of_this_year).days
        total_minutes += days_this_year * 24 * 60

        return total_minutes

    def get_minutes_in_words(self) -> str:
        # Convert minutes to words using inflect.
        p = inflect.engine()
        minutes = self.get_minutes_since_birth()
        return p.number_to_words(minutes, andword="").capitalize()

def main():
    birthdate = input("Date of Birth: ")
    person = Person(birthdate)
    print(f"{person.get_minutes_in_words()} minutes")

if __name__ == "__main__":
    main()
