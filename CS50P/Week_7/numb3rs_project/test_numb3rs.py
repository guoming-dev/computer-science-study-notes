from numb3rs import validate  # Import the function from numb3rs.py

# ✅ Test valid IPv4 addresses
def test_valid_ips():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("10.0.0.1") == True
    assert validate("172.16.254.1") == True

# ❌ Test invalid IPv4 addresses (incorrect formats)
def test_invalid_formats():
    assert validate("256.100.50.25") == False  # Out of range (256 > 255)
    assert validate("192.168.1") == False  # Missing an octet
    assert validate("192.168.1.1.5") == False  # Extra octet (5 parts)
    assert validate("192.168..1") == False  # Double dots
    assert validate("abc.def.ghi.jkl") == False  # Non-numeric characters
    assert validate("192.168.1.-1") == False  # Negative octet
    assert validate("192.168.1.300") == False  # Last octet out of range
