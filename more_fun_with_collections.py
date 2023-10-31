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
# set_membership.py

def in_set(input_set, value):

    return value in input_set

def main():
    # Initialize a set called test_set
    test_set = {'banana', 'apple', 'cherry'}

    # Initialize a value called test_value
    test_value1 = 'apple'
    test_value2 = '5'

    # Call in_set() with appropriate values and print messages
    if in_set(test_set, test_value1):
        print(f"The value '{test_value1}' is in the set {test_set}")
    else:
        print(f"The value '{test_value1}' is not in the set {test_set}")

    if in_set(test_set, test_value2):
        print(f"The value '{test_value2}' is in the set {test_set}")
    else:
        print(f"The value '{test_value2}' is not in the set {test_set}")

if __name__ == "__main__":
    main()
