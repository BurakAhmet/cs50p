from project import validate_name, validate_password, validate_title


def test_validate_name():
    assert validate_name("ahmet burak") == True
    assert validate_name("ahmet  burak") == False
    assert validate_name("ahmet burak bicer") == True
    assert validate_name(" ahmet") == False
    assert validate_name("ahmet ") == False
    assert validate_name("dog") == True
    assert validate_name("CAT") == True
    assert validate_name("AhMeT") == True
    assert validate_name("bUrAk") == True
    assert validate_name("ahmet1") == False
    assert validate_name("2ahmet") == False
    assert validate_name("ahm3et") == False
    assert validate_name("ahmet 4 burak") == False
    assert validate_name("ahmet_burak") == False
    assert validate_name("?ahmet") == False
    assert validate_name("ahmet*") == False


def test_validate_password():
    assert validate_password("1234") == False
    assert validate_password("") == False
    assert validate_password("abc") == False
    assert validate_password("a") == False
    assert validate_password("abcde") == False
    assert validate_password("_a_a_") == False
    assert validate_password("12345") == False
    assert validate_password("_1_1_") == False
    assert validate_password("1abcd") == True
    assert validate_password("12345a") == True
    assert validate_password("a1b2c3d4e5") == True
    assert validate_password(".?*\\][ (/&%$+'1abc") == True


def test_validate_title():
    assert validate_title("pr") == False
    assert validate_title("prof") == True
    assert validate_title("prof_") == False
    assert validate_title("1doc") == False
    assert validate_title("doc") == True
    assert validate_title("DOC") == True
    assert validate_title("professor") == False
    assert validate_title("do c") == False
    assert validate_title("") == False
