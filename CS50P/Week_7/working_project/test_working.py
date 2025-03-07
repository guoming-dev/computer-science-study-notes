import pytest
from working import convert

def test_valid_cases():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("5 PM to 12:15 AM") == "17:00 to 00:15"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_invalid_cases():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")   # Invalid minutes
    with pytest.raises(ValueError):
        convert("14:00 PM to 16:00 AM") # Invalid hours
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  # Incorrect format
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")  # Incorrect format
    with pytest.raises(ValueError):
        convert(" to ") # Incorrect format

def test_edge_cases():
    assert convert("1 PM to 09:00 PM") == "13:00 to 21:00"
    assert convert("1 AM to 10:20 PM") == "01:00 to 22:20"

def test_spacing_issues():
    with pytest.raises(ValueError):
        convert("9:00  AM to 5:00  PM")  # Extra spaces between time and AM/PM
    with pytest.raises(ValueError):
        convert(" 9:00 AM to 5:00 PM")  # Leading space
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM ")  # Trailing space
