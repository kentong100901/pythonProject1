# ***************************************************************
# Name : ProgramNameTong
# Author: Than Tong
# Created : * Course: CIS189
# Version: 1.0
# OS: Windows 11
# IDE: Python
# Copyright : This is my own original work
# based onspecifications issued by our instructor
# Description :
#           Input: ADD HERE XXX
#           Ouput: ADD HERE XXX
# Academic Honesty: I attest that this is my original work.
# I have not used unauthorized source code, either modified or
# unmodified. I have not given other fellow student(s) access
# to my program.


# Describe a monkey's actions in a string
monkey_activity = "The monkey is swinging on the branches in the jungle."

# Use the capitalize method to capitalize the first letter of the string.
capitalized_monkey_activity = monkey_activity.capitalize()
print("Capitalized:", capitalized_monkey_activity)

# Use the find method to find the index of 'monkey'.
index_of_monkey = monkey_activity.find("monkey")
print("Index of 'monkey':", index_of_monkey)

# Use the index method to find the index of 'swinging'.
try:
    index_of_swinging = monkey_activity.index("swinging")
    print("Index of 'swinging':", index_of_swinging)
except ValueError as e:
    print("Substring not found:", e)

# Use the isalnum method to check if the string is alphanumeric.
is_alphanumeric = monkey_activity.isalnum()
print("Is alphanumeric:", is_alphanumeric)

# Use the isalpha method to check if the string contains only alphabetic characters.
is_alpha = monkey_activity.isalpha()
print("Is alpha:", is_alpha)

# Use the isdigit method to check if the string contains only digits.
is_digit = monkey_activity.isdigit()
print("Is digit:", is_digit)

# Use the islower method to check if all alphabetic characters are lowercase.
is_lower = monkey_activity.islower()
print("Is lowercase:", is_lower)

# Use the isupper method to check if all alphabetic characters are uppercase.
is_upper = monkey_activity.isupper()
print("Is uppercase:", is_upper)

# Use the isspace method to check if the string contains only whitespace characters.
is_space = monkey_activity.isspace()
print("Is whitespace:", is_space)

# Use the startswith method to check if the string starts with 'The'.
starts_with_the = monkey_activity.startswith("The")
print("Starts with 'The':", starts_with_the)

