import pytest
from working import convert

def main():
    test_wrong_format()
    test_time()
    test_wrong_hour()
    test_wrong_minute()

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")

def test_time():
    assert convert("9 AM to 9 PM") == "09:00 to 21:00"
    assert convert("11:00 AM to 3 PM") == "11:00 to 15:00"
    assert convert("10:30 AM to 12 PM") == "10:30 to 12:00"
    assert convert("12 AM to 4 PM") == "00:00 to 16:00"

def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("9 AM to 17 PM")

def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("9 AM to 11:60 PM")