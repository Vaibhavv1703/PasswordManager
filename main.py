import re
import os
import pickle
import urllib.request

PICKLE_PATH = 'rockyou.pkl'
REMOTE_URL = 'https://www.dropbox.com/scl/fi/weorggtspmqpd0hkp0eti/rockyou.pkl?rlkey=obyodpark2be1nlwzqbscn60h&st=n5bfbze7&dl=1'

def download_pickle_file():
    print(f"{PICKLE_PATH} not found. Downloading from {REMOTE_URL}...")
    try:
        urllib.request.urlretrieve(REMOTE_URL, PICKLE_PATH)
        print("Download complete.")
    except Exception as e:
        print("Failed to download the file:", e)
        exit(1)

if not os.path.exists(PICKLE_PATH):
    download_pickle_file()

with open(PICKLE_PATH, 'rb') as f:
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