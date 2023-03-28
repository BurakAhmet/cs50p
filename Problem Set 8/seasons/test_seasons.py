from seasons import validate
import pytest

def test_invalid():
    with pytest.raises(SystemExit):
        validate("July 3, 1978")
        validate("cat")
