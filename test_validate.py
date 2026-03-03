import pytest
from validator import (
    validate_email,
    validate_age,
    validate_user,
    InvalidEmailError,
    InvalidAgeError,
    EmptyFieldError,
)


# Email Tests
def test_valid_email():
    assert validate_email("test@example.com") is True


def test_invalid_email():
    with pytest.raises(InvalidEmailError):
        validate_email("invalid-email")


def test_empty_email():
    with pytest.raises(EmptyFieldError):
        validate_email("")


#  Age Tests
def test_valid_age():
    assert validate_age(25) is True


def test_invalid_age_negative():
    with pytest.raises(InvalidAgeError):
        validate_age(-5)


def test_invalid_age_too_high():
    with pytest.raises(InvalidAgeError):
        validate_age(200)


def test_empty_age():
    with pytest.raises(EmptyFieldError):
        validate_age(None)


def test_valid_user():
    assert validate_user("user@test.com", 30) is True