"""
Password Generator
Made by Nayan Bhattarai.
Website: https://www.nayanbhattarai.info.np/
"""

import random
import string

def generate_password(length, min_upper, min_numbers, min_symbols):
    if length < min_upper + min_numbers + min_symbols:
        raise ValueError("Password length is too short for the specified minimum requirements.")

    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    number_chars = string.digits
    symbol_chars = string.punctuation

    password_chars = []

    for _ in range(min_upper):
        password_chars.append(random.choice(upper_chars))

    for _ in range(min_numbers):
        password_chars.append(random.choice(number_chars))

    for _ in range(min_symbols):
        password_chars.append(random.choice(symbol_chars))

    all_chars = lower_chars + upper_chars + number_chars + symbol_chars
    remaining_length = length - len(password_chars)
    password_chars += [random.choice(all_chars) for _ in range(remaining_length)]

    random.shuffle(password_chars)
    return ''.join(password_chars)

def ask_number(prompt, default=0):
    while True:
        try:
            value = input(prompt).strip()
            if value == '':
                return default
            value = int(value)
            if value < 0:
                print("Please enter 0 or a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Welcome to the Advanced Interactive Password Generator!")
    print("Created by Nayan Bhattarai - Website: https://www.nayanbhattarai.info.np\n")

    while True:
        length = ask_number("Enter desired password length (minimum 8): ")
        if length < 8:
            print("Password length must be at least 8 characters.")
            continue
        break

    min_upper = ask_number("Minimum uppercase letters (default 1): ")
    min_numbers = ask_number("Minimum numbers (default 1): ")
    min_symbols = ask_number("Minimum symbols (default 1): ")

    try:
        password = generate_password(length, min_upper, min_numbers, min_symbols)
        print("\nGenerated Password:", password)
        print("\nThank you for using this generator! Visit my website for more tools: https://nayanbhattarai.info.np")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
