from numb3rs import validate


def test_string():
    assert validate("cat") == False
    assert validate("") == False
    assert validate("...") == False


def test_bigger_numbers():
    assert validate("256.1.11.12") == False
    assert validate("1.256.20.3") == False
    assert validate("10.2.256.4") == False
    assert validate("1.99.0.256") == False
    assert validate("1111.255.255.255") == False

def test_longer():
    assert validate("1.1.1.1.1") == False
    assert validate("1.2.3.4.5") == False


def test_missing():
    assert validate("1.2.3") == False
    assert validate("1.2") == False
    assert validate("1") == False

def test_diffirent_shape():
    assert validate("1.2.3.4.") == False
    assert validate(".1.2.3.4") == False
    assert validate("1 2 3 4") == False
    assert validate(".1.2.3.4.") == False

def test_valid():
    assert validate("1.2.3.4") == True
    assert validate("99.99.99.99") == True
    assert validate("255.255.255.255") == True
    assert validate("10.20.30.40") == True
    assert validate("1.10.100.255") == True
    assert validate("127.0.0.1") == True
    assert validate("140.247.235.144") == True
    assert validate("0.0.0.0") == True

def tes_negative():
    assert validate("-1.1.1.1") == False
    assert validate("1.-1.1.1") == False
    assert validate("1.1.-1.1") == False
    assert validate("1.1.1.-1") == False
