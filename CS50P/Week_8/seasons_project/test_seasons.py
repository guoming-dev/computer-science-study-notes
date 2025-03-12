import pytest
from seasons import Person

def test_is_leap_year():
    p = Person("2000-01-01")
    assert p.is_leap_year(2000) == True
    assert p.is_leap_year(1900) == False
    assert p.is_leap_year(2024) == True
    assert p.is_leap_year(2023) == False

def test_get_minutes_since_birth():
    p = Person("2000-01-01")
    assert p.get_minutes_since_birth() > 0  # Should return a positive number

def test_get_minutes_in_words():
    p = Person("2000-01-01")
    assert isinstance(p.get_minutes_in_words(), str)  # Should return a string

def test_invalid_date_format():
    """Ensure that an invalid date format raises SystemExit with 'Invalid date'."""
    invalid_dates = ["2025-13-40", "12-31-2020", "2025/02/30", "Hello-World"]

    for date_str in invalid_dates:
        with pytest.raises(SystemExit) as exc_info:
            Person(date_str)

        # Check if the exception message is exactly "Invalid date"
        assert str(exc_info.value) == "Invalid date"
