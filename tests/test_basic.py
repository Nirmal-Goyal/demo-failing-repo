from src.utils import add
from src.validator import is_valid

def test_add():
    assert add(1, 2) == 3

def test_validator():
    assert is_valid(5) is True
