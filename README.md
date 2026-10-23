
# Software Security Assignment

## User Authentication System Using Python

### Project Description
This project is a simple user authentication system developed using Python.

### Features
- User registration.
- Generate a random salt for each user.
- Hash passwords using SHA-256.
- Store user information in a text file.
- Verify username and password during login.

### Technologies Used
- Python
- hashlib
- secrets

### How to Run
1. Install Python.
2. Open the project folder in the terminal.
3. Run the following command:

   python main.py

4. Choose 1 to register or 2 to login.

### Security Note
Passwords are stored as hashes with individual salts, not as plain text. SHA-256 is used for this educational project.
