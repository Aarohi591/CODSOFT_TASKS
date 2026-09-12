# CodSoft Python Programming Internship
# Task 3: Password Generator

import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("==============================")
print("      PASSWORD GENERATOR")
print("==============================")

while True:
    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Please enter a positive number.")
            continue

        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

        break

    except ValueError:
        print("Please enter a valid number.")
