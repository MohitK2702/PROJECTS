import re
import os
import argparse
import sys

# Function to load compromised passwords from multiple directories
def load_compromised_passwords(directories):
    compromised = set()
    if not directories:
        print("No password list directories specified. Proceeding without compromised password check.")
        return compromised

    for directory_path in directories:
        if not os.path.isdir(directory_path):
            print(f"Directory '{directory_path}' not found. Skipping this directory.")
            continue

        # Iterate through all files in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        # Add each password to the set, converting to lowercase for case-insensitive comparison
                        initial_count = len(compromised)
                        compromised.update(line.strip().lower() for line in file if line.strip())
                        added = len(compromised) - initial_count
                        print(f"Loaded '{filename}' with {added} new compromised passwords.")
                except Exception as e:
                    print(f"Error reading '{file_path}': {e}")
    print(f"Total compromised passwords loaded: {len(compromised)}\n")
    return compromised

# Function to check if the password has repeated patterns
def has_repeated_patterns(password):
    length = len(password)
    for i in range(length):
        for j in range(i + 2, length + 1):
            substring = password[i:j]
            if substring and substring in password[j:]:
                return True
    return False

# Function to check if password contains keyboard patterns
def has_keyboard_patterns(password):
    keyboard_patterns = ["qwerty", "asdfgh", "zxcvbn", "123456", "098765"]
    for pattern in keyboard_patterns:
        if pattern in password.lower():
            return True
    return False

# Function to check if password is compromised
def is_compromised(password, compromised_set):
    return password.lower() in compromised_set

# Function to calculate password strength
def check_password_strength(password, compromised_set):
    strength = 0
    feedback = []

    # Check if password is compromised
    if is_compromised(password, compromised_set):
        feedback.append("This password is already compromised or commonly used. Please choose a different one.")
        return "Compromised", feedback

    # Length check
    length = len(password)
    if length >= 12:
        strength += 2
    elif length >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Character variety check
    lowercase_criteria = re.search(r'[a-z]', password)
    uppercase_criteria = re.search(r'[A-Z]', password)
    digit_criteria = re.search(r'\d', password)
    special_char_criteria = re.search(r'[@$!%*?&#]', password)

    if lowercase_criteria:
        strength += 1
    else:
        feedback.append("Add lowercase letters.")

    if uppercase_criteria:
        strength += 1
    else:
        feedback.append("Add uppercase letters.")

    if digit_criteria:
        strength += 1
    else:
        feedback.append("Add digits.")

    if special_char_criteria:
        strength += 1
    else:
        feedback.append("Add special characters (@, $, !, etc.).")

    # Check for repeated patterns
    if has_repeated_patterns(password):
        feedback.append("Avoid repeated patterns or sequences.")
    else:
        strength += 1

    # Check for keyboard patterns
    if has_keyboard_patterns(password):
        feedback.append("Avoid keyboard patterns like 'qwerty' or '12345'.")
    else:
        strength += 1

    # Final strength evaluation
    if strength >= 8:
        return "Very Strong", feedback
    elif strength >= 6:
        return "Strong", feedback
    elif strength >= 4:
        return "Medium", feedback
    else:
        return "Weak", feedback

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Advanced Password Strength Checker with Dynamic Password Lists',
        epilog='Example usage: python password_checker.py --lists-dir path/to/dir1 path/to/dir2'
    )
    parser.add_argument(
        '--lists-dir',
        nargs='*',
        default=['password_lists'],
        help='One or more directories containing password list files. Default is "password_lists".'
    )
    args = parser.parse_args()

    # Load compromised passwords from specified directories
    compromised_passwords = load_compromised_passwords(args.lists_dir)

    while True:
        # Get user input
        try:
            password = input("Enter your password (or type 'exit' to quit): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting the password checker. Stay safe!")
            break

        if password.lower() == 'exit':
            print("Exiting the password checker. Stay safe!")
            break

        if not password:
            print("Please enter a valid password.\n")
            continue

        # Check password strength
        strength, feedback = check_password_strength(password, compromised_passwords)

        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Feedback:")
            for msg in feedback:
                print(f"- {msg}")
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
