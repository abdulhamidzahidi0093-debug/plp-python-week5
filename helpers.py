# Week 5 Assignment - My Own Module

import math

# Calculate how many tables are needed.
def tables_needed(people, seats):
    return math.ceil(people / seats)


# Welcome someone to PLP.
def welcome(name):
    return "Welcome to PLP, " + name + "!"


# Run this part only when helpers.py is executed directly.
if __name__ == "__main__":
    print(tables_needed(10, 4))
