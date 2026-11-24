# Week 5 Assignment - Password Generator

import random
import string

# This function creates a random password.
def make_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


# Create two passwords with different lengths.
p1 = make_password()
p2 = make_password(12)

# Display the passwords and their lengths.
print("Password:", p1)
print("Length:", len(p1))

print("Password:", p2)
print("Length:", len(p2))
