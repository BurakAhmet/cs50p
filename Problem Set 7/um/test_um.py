from um import count


def test_count():
    assert count("um") == 1
    assert count("um...") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks for the album.") == 1
    assert count("yummy") == 0
    assert count("column") == 0
    assert count("umm") == 0
    assert count("..um..") == 1


def test_count_case():
    assert count("UM, THANKS, UM...") == 2
    assert count("UM, THANKS FOR THE ALBUM.") == 1
    assert count("CoLumN") == 0
    assert count("uM...") == 1


def test_count_numeric():
    assert count("1um") == 0
    assert count("um...11") == 1
    assert count("1um1") == 0
