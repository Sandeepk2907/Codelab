Password Security & Python Utility Scripts

A collection of beginner-friendly Python programs focused on password security, file handling, HTTP requests, and keyboard event monitoring. These scripts are useful for learning basic cybersecurity and Python automation concepts.

Features
Password strength checker
HTTP status code checker using requests
.txt file counter in a directory
Secure password generator
Common password pattern generator
Advanced password validator using regex
Keyboard key press listener
Project Structure
├── prgm01.py   # Basic password length checker
├── prgm02.py   # HTTP response status checker
├── prgm03.py   # Count .txt files in a directory
├── prgm04.py   # Secure password generator
├── prgm05.py   # Common password combination generator
├── prgm06.py   # Advanced password strength validator
├── prgm07.py   # Keyboard key press detector
└── README.md
Program Descriptions
1. Basic Password Length Checker

Checks whether the entered password contains at least 8 characters.

Concepts Used
input()
if-else
String length checking
Run
python prgm01.py
2. HTTP Status Code Checker

Sends a request to Google and prints the HTTP response status code.

Concepts Used
requests library
HTTP GET requests
Install Dependency
pip install requests
Run
python prgm02.py
3. Text File Counter

Counts the number of .txt files in a given directory.

Concepts Used
os module
Directory listing
File extension checking
Run
python prgm03.py
4. Secure Password Generator

Generates a strong random password using letters, digits, and special characters.

Concepts Used
secrets
string
Random secure password generation
Run
python prgm04.py
5. Common Password Pattern Generator

Generates predictable password combinations using user details.

Educational purpose only — demonstrates weak password patterns.

Concepts Used
Lists
String concatenation
User input handling
Run
python prgm05.py
6. Advanced Password Strength Validator

Validates password strength based on:

Uppercase letters
Lowercase letters
Numbers
Special characters
Minimum length
Concepts Used
re module (Regular Expressions)
Pattern matching
Run
python prgm06.py
7. Keyboard Key Press Listener

Detects and prints keyboard key presses in real time.

Concepts Used
Event listeners
pynput library
Install Dependency
pip install pynput
Run
python prgm07.py
Stop Program

Press:

CTRL + C
Requirements

Install required Python libraries:

pip install requests pynput
Learning Objectives

This repository helps beginners understand:

Python basics
Password security concepts
File handling
HTTP requests
Regular expressions
Event listeners
Cybersecurity fundamentals
Disclaimer

Some scripts in this repository are intended strictly for educational and ethical learning purposes. Do not misuse these programs for unauthorized activities.

Author

Developed by Sandeep

GitHub: Add your GitHub profile link here.
