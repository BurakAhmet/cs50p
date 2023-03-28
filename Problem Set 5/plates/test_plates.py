from plates import is_valid


def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False

def test_is_valid_length():
    assert is_valid("") == False
    assert is_valid("A") == False
    assert is_valid("AAA") == True
    assert is_valid("CS123456") == False

def test_is_valid_beginning():
    assert is_valid("AA22") == True
    assert is_valid("A22") == False
    assert is_valid("22A") == False

def test_is_valid_number():
    assert is_valid("22AA") == False
    assert is_valid("AA2A22") == False
    assert is_valid("AAA222") == True

def test_is_valid_alphanumeric():
    assert is_valid("AA!'22") == False
    assert is_valid("CS 50") == False
    assert is_valid("   Har  vard") == False

def test_is_valid_zero():
    assert is_valid("CS05") == False
    assert is_valid("AA20") == True
