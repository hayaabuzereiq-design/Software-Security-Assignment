import hashlib
import secrets

choice = input("1. Register\n2. Login\nChoose: ")

if choice == "1":
    username = input("Enter username: ")
    password = input("Enter password: ")

    salt = secrets.token_bytes(16)

    password_hash = hashlib.sha256(
        salt + password.encode()
    ).hexdigest()

    with open("users.txt", "a") as file:
        file.write(
            f"{username},{salt.hex()},{password_hash}\n"
        )

    print("User registered successfully!")

elif choice == "2":
    username = input("Enter username: ")
    password = input("Enter password: ")

    found = False

    try:
        with open("users.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) != 3:
                    continue

                saved_username, saved_salt, saved_hash = parts

                if username == saved_username:
                    salt = bytes.fromhex(saved_salt)

                    password_hash = hashlib.sha256(
                        salt + password.encode()
                    ).hexdigest()

                    if password_hash == saved_hash:
                        print("Login successful!")
                    else:
                        print("Wrong password!")

                    found = True
                    break

        if not found:
            print("User not found.")

    except FileNotFoundError:
        print("No registered users found.")

else:
    print("Invalid choice.")