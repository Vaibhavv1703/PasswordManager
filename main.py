import re
import os
import pickle
import urllib.request
import math

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

def calculate_entropy(password):
    char_sets = {
        'lowercase': 26,
        'uppercase': 26,
        'digits': 10,
        'special_chars': 32
    }

    char_set_size = 0
    if re.search(r"[a-z]", password):
        char_set_size += char_sets['lowercase']
    if re.search(r"[A-Z]", password):
        char_set_size += char_sets['uppercase']
    if re.search(r"\d", password):
        char_set_size += char_sets['digits']
    if re.search(r"[!@#$%^&*()-_=+/,.?\":{}|<>]", password):
        char_set_size += char_sets['special_chars']

    entropy = len(password) * math.log2(char_set_size)
    return entropy

def estimate_cracking_time(password):
    guesses_per_second = 10**9      #### Brute force assuming 1 billion guesses per second
    
    entropy = calculate_entropy(password)
    
    cracking_time_seconds = 2**entropy / guesses_per_second
    if cracking_time_seconds < 60:
        return f"{cracking_time_seconds:.2f} seconds"
    elif cracking_time_seconds < 3600:
        return f"{cracking_time_seconds / 60:.2f} minutes"
    elif cracking_time_seconds < 86400:
        return f"{cracking_time_seconds / 3600:.2f} hours"
    elif cracking_time_seconds < (365 * 24 * 3600):  ### 1 year in seconds (365 * 24 * 3600)
        return f"{cracking_time_seconds / 86400:.2f} days"
    elif cracking_time_seconds < (50 * 365 * 24 * 3600):  ### 50 years in seconds (50 * 365 * 24 * 3600)
        return f"{cracking_time_seconds / 31536000:.2f} years"
    else:
        return "> 50 years"

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

strength = check_password_strength(password)
entropy = calculate_entropy(password)
cracking_time = estimate_cracking_time(password)

print("Strength:", strength)
print(f"Entropy: {entropy:.2f} bits")
print(f"Estimated cracking time: {cracking_time}")