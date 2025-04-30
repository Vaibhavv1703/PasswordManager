import re
import pickle

with open('rockyou.pkl', 'rb') as f:
    common_passwords = pickle.load(f)

def check_password_strength(password):
    if password in common_passwords:
        return "Very Weak (Commonly used password)"

    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*()-_=+/,.?\":{}|<>]", password) is None

    errors = [length_error, lowercase_error, uppercase_error, digit_error, special_char_error]
    strength_score = 5 - sum(errors)

    if strength_score == 5:
        return "Very Strong"
    elif strength_score >= 4:
        return "Strong"
    elif strength_score >= 3:
        return "Medium"
    else:
        return "Weak"

password = input("Enter a password to check: ")
print("Strength:", check_password_strength(password))
