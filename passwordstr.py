import re

def check_password_length(password):
    """Check if the password is at least 8 characters long."""
    return len(password) >= 8

def check_password_complexity(password):
    """Check if the password contains at least one digit, one lowercase letter,
    one uppercase letter, and one special character.
    """
    if re.search(r'\d', password) is None:
        return False
    if re.search(r'[a-z]', password) is None:
        return False
    if re.search(r'[A-Z]', password) is None:
        return False
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is None:
        return False
    return True

def check_password_repetition(password):
    """Check if the password contains repetitive sequences of characters."""
    for i in range(3, len(password) // 2 + 1):
        for j in range(len(password) - i + 1):
            if password[j:j + i] * (len(password) // i + 1) == password:
                return False
    return True

def password_strength(password):
    """Evaluate the strength of the password."""
    if not check_password_length(password):
        return "Weak (too short)"
    if not check_password_complexity(password):
        return "Weak (not complex enough)"
    if not check_password_repetition(password):
        return "Medium (contains repetitive sequences)"
    return "Strong"

def main():
    """Get the user's password and print its strength."""
    while True:
        try:
            password = input("Enter your password: ")
            break
        except KeyboardInterrupt:
            print("\nExiting...")
            return
    strength = password_strength(password)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()