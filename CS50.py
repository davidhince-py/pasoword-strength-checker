#Harvard CS50 Python Course Notes/Tasks

#Name interaction
import re

weak_passwords = ["password", "123456", "qwerty", "abc123", "password123"]

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Weak password list
    if password.lower() in weak_passwords:
        score = 0
        feedback.append("This password is very common and easy to guess.")

    return score, feedback


while True:
    password = input("\nEnter a password to test (or type 'exit'): ")

    if password.lower() == "exit":
        print("Goodbye!")
        break

    score, feedback = check_password_strength(password)

    print("\nPassword Score:", score, "/ 5")

    if score == 5:
        print("Strong password! 🔒")
    elif score >= 3:
        print("Moderate password.")
    else:
        print("Weak password.")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("-", item)

