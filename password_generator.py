"""
Password Generator
Made by Nayan Bhattarai
Website: https://nayanbhattarai.info.np
"""

import random
import string
import argparse

def generate_password(length=12, use_upper=True, use_numbers=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    return ''.join(random.choice(chars) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Secure Password Generator")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")
    parser.add_argument("-u", "--upper", action="store_true", help="Include uppercase letters")
    parser.add_argument("-n", "--numbers", action="store_true", help="Include numbers")
    parser.add_argument("-s", "--symbols", action="store_true", help="Include symbols")

    args = parser.parse_args()
    pwd = generate_password(args.length, args.upper, args.numbers, args.symbols)
    print(f"Generated Password: {pwd}")

if __name__ == "__main__":
    main()
