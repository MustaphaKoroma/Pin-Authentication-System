# Following is the authentication logic
import hashlib
from getpass import getpass

MAX_ATTEMPTS = 3

def hash_pin(pin: str) -> str:
    """Hash a PIN using SHA-256."""
    return hashlib.sha256(pin.encode()).hexdigest()

def verify_pin(stored_hash: str, entered_pin: str) -> bool:
    """Verify entered PIN against stored hash."""
    return hash_pin(entered_pin) == stored_hash

def authenticate_user(stored_hash: str) -> bool:
    """Authenticate user with limited attempts."""
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        entered_pin = getpass("Enter your PIN: ")
        if verify_pin(stored_hash, entered_pin):
            print("Access Granted")
            return True
        else:
            attempts += 1
            print(f"Incorrect PIN. Attempts remaining: {MAX_ATTEMPTS - attempts}")
    print("Too many incorrect attempts. Account locked.")
    return False
