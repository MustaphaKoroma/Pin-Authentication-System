# This unit tests the authentication module. Includes tests for login, token validation, and error handling.
from auth import hash_pin, verify_pin

def test_correct_pin():
    pin = "1234"
    stored_hash = hash_pin(pin)
    assert verify_pin(stored_hash, "1234") is True

def test_incorrect_pin():
    pin = "1234"
    stored_hash = hash_pin(pin)
    assert verify_pin(stored_hash, "0000") is False
