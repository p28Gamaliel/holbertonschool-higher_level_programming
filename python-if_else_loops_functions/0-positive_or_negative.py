#!/usr/bin/python3
import random
number = random.randint(-10, 10)

print(f"{number}", end=" ")
if number > 0:
    print(f"is positive")
elif number == 0:
    print(f"is zero")
if number < 0:
   print(f"is negative")
