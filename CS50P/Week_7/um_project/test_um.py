from um import count

def test_single_um():
    assert count("um") == 1

def test_multiple_um():
    assert count("um, um") == 2

def test_case_insensitivity():
    assert count("Um UM uM") == 3

def test_no_um():
    assert count("yummy") == 0

def test_um_in_words():
    assert count("album, yummy, plumb") == 0
