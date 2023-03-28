from bank import value

def test_value():
    assert value("Hello, World") == 0
    assert value("Hi, World") == 20

def test_value_numeric():
    assert value("H3ll0, W0rld") == 20
    assert value("Hello123!") == 0

def test_value_upper():
    assert value("HELLOWORLD") == 0
    assert value("HI!") == 20

def test_value_lower():
    assert value("hello, world") == 0
    assert value("hi!!") == 20
