from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("CS50") == "CS50"
    assert shorten("AEIOU") == ""
    assert shorten("hello") == "hll"
    assert shorten("WORLD") == "WRLD"
    assert shorten("Python Programming") == "Pythn Prgrmmng"
    assert shorten("aEiOu") == ""

def test_case_sensitivity():
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("gOoGlE") == "gGl"

def test_numbers_and_symbols():
    assert shorten("CS50!") == "CS50!"
    assert shorten("1a2e3i4o5u") == "12345"
    assert shorten("1234!@#") == "1234!@#"
