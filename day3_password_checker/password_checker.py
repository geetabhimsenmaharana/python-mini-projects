def set_password(max_attempts=3):
    attempts = max_attempts

    while attempts > 0:
        try:
            password1 = input("Enter your password: ")
            password2 = input("Re-enter your password: ")

            if password1 == password2:
                print("Password verified successfully.\n")
                return password1
            else:
                attempts -= 1
                print(f"Passwords do not match. Attempts left: {attempts}")

        except KeyboardInterrupt:
            print("\nProcess interrupted by user.")
            return None

    print("Too many failed attempts. Please try again later.")
    return None


def login(stored_password, max_attempts=2):
    attempts = max_attempts

    while attempts > 0:
        try:
            user_input = input("Enter your password to login: ")

            if user_input == stored_password:
                print("Successful login!")
                return True
            else:
                attempts -= 1
                print(f"Incorrect password. Attempts left: {attempts}")

        except KeyboardInterrupt:
            print("\nLogin interrupted by user.")
            return False

    print("Too many failed login attempts.")
    return False


def main():
    password = set_password()

    if password:
        print("Login\n")
        login(password)


if __name__ == "__main__":
    main()
