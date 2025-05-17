# Password Management Tool

A terminal-based suite for password security and management, featuring a **Password Strength Checker** and a secure **Password Manager**. Built with simplicity and cybersecurity in mind.

---

## Password Checker

Evaluate password strength, estimate cracking time, and calculate entropy directly from your terminal.

### Features

- **Password Strength Checker**: Rates your password as Very Weak, Weak, Medium, Strong, or Very Strong.
- **Entropy Calculation**: Calculates the entropy (in bits) of your password.
- **Estimated Cracking Time**: Estimates how long it would take to brute-force your password.
- **Common Password Detection**: Checks if your password is among the most common passwords using the `rockyou.txt` dataset (pickled, downloaded automatically).
- **Clean Terminal Interface**: Easy-to-use menu navigation.

---

## Password Manager

A secure, terminal-based tool to save, view, update, and delete your passwords in an encrypted vault.

### Features

- **Master Password**: Set a master password to protect your vault.
- **Encryption**: Vault is encrypted using Fernet (AES) with your master password.
- **Local Storage**: Passwords are stored locally in `vault.enc`.
- **Password Operations**: Add, view, update, delete, and search passwords with ease.

---

## Requirements

- Python 3.x
- `cryptography` Python package (install via `pip install cryptography`)

---

## Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Vaibhavv1703/passwordTool.git
    ```
2. **Navigate to the working directory:**
    ```bash
    cd passwordTool
    ```
3. **Run the application:**
    ```bash
    py main.py
    ```
    > **Note:** The first run may take some time as the common password dataset is downloaded.

---

## Project Structure

- [`main.py`](main.py): Main menu and entry point.
- [`checker.py`](checker.py): Password strength checker logic.
- [`manager.py`](manager.py): Password manager logic.

---

## Future Scope

- **Password Generator**: Generate strong, secure passwords based on user preferences.
- **Integration with Password Managers**: Import/export from other password managers.
- **Advanced Strength Metrics**: More sophisticated password analysis.
- **Deployment**: Plans to deploy this app online for easy access.
