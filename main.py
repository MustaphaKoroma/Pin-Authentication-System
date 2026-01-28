# Application entry point
from auth import hash_pin, authenticate_user

def main():
    # Example PIN: 1234
    stored_pin_hash = hash_pin("1234")
    authenticate_user(stored_pin_hash)

if __name__ == "__main__":
    main()
