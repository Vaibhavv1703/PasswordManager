# Password Checker
A terminal-based **Password Checker Tool** that helps users evaluate password strength, estimate cracking time, and calculate entropy. Built with simplicity and cybersecurity in mind.

## Features
- Password Strength Checker  
- Entropy Calculation  
- Estimated Cracking Time  
- Common password detection using the `rockyou.txt` dataset (pickled)  
- Clean terminal interface with menu navigation


# Password Manager
A terminal-based **Password Managing Tool** that helps users save, view, update, delete their passwords in a encrypted format.

## Features
- Users can set a Master Password for their vault
- The vault will be encrypted according to the Master Password using Fernet
- Passwords are saved locally in `vault.enc`

## Requirements
- Python 3.x

## Usage
1. Clone the repository:
      ```bash
      git clone https://github.com/Vaibhavv1703/PasswordChecker.git
      ```
2. Navigate to working directory:
      ```bash
      cd PasswordChecker
      ```
3. Run `main.py`
      ```bash
      py main.py
      ```
! Will take time when running for first time depending upon your internet speed.
## Future Scope
- **Password Generator**: Plans to add functionality for generating strong, secure passwords based on user preferences.
- **Integration with Password Managers**: Future versions may allow importing them from password managers.
- **Advanced Strength Metrics**: Plans to introduce more sophisticated metrics and validation checks to make password strength analysis more robust.
- **Deployment**: Plans to deploy this app online for easy access.
