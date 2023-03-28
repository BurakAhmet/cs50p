from twttr import shorten

def test_shorten():
    assert shorten("David") == "Dvd"
    assert shorten("Harvard") == "Hrvrd"

def test_shorten_lower():
    assert shorten("thisiscs50") == "thsscs50"
    assert shorten("testtwitter") == "tsttwttr"


def test_shorten_upper():
    assert shorten("HELLOWORD") == "HLLWRD"
    assert shorten("THISISCS50") == "THSSCS50"

def test_shorten_numeric():
    assert shorten("Da1vid2") == "D1vd2"
    assert shorten("Ha2R0V2ar76D") == "H2R0V2r76D"

def test_shorten_punctuation():
    assert shorten("Da!vid;") == "D!vd;"
    assert shorten("Ha:R/V(ar)+D") == "H:R/V(r)+D"
