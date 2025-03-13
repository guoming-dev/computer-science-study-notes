from jar import Jar

def test_init():
    # Test initializing the Jar class.
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    # Test string representation of the Jar.
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    # Test depositing cookies into the Jar.
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    try:
        jar.deposit(10) # Should exceed capacity
    except ValueError:
        assert jar.size == 5    # Ensure size remains unchanged

def test_withdraw():
    # Test withdrawing cookies from the Jar.
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    try:
        jar.withdraw(10)    # Should raise an error
    except ValueError:
        assert jar.size == 3    # Ensure size remains unchanged
