# Pin-Authentication-System
This is a simple Python-based console application that authenticates users using a PIN code.  
The project was created to practice Python fundamentals, including conditional logic, user input handling, and clean code organisation.

It demonstrates how to:
- Validate user input
- Compare input to a stored PIN securely
- Provide feedback on authentication success or failure
- Structure a small Python project clearly

## Project Goal
The goal of this project is to build a secure, console-based PIN authentication system in Python that demonstrates clean code structure, basic security awareness, and testable design using core Python features.

## Overview
This project simulates a real-world PIN-based authentication flow similar to those used in ATM machines, mobile money applications, and access-controlled systems.

The system limits login attempts, hides sensitive input, and verifies credentials securely using hashing.

## Features
- Secure PIN verification using SHA-256 hashing
- Hidden PIN input via `getpass`
- Limited login attempts
- Account lock after repeated failures
- Modular and testable code structure

## Programming Language Used
- Python 3
- Python Standard Library

## Project Structure
Pin-Authentication-System/

├── auth.py

├── main.py

├── tests/
│ └── test_auth.py

└── README.md

## Learning Focus
The project helps users learn the following:

• Python fundamentals

• Modular code design

• Secure input handling

• Basic authentication logic

• Writing testable code

Notes
This project is for educational purposes and demonstrates authentication concepts using core Python.

## License
Open-source and available for learning and educational use.

