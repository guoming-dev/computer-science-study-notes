from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello, good morning") == 0

def test_20():
    assert value("Hi there!") == 20
    assert value("hELp me") == 20

def test_100():
    assert value("Goodbye") == 100
    assert value("howdy partner") == 20
    assert value("guoming") == 100
