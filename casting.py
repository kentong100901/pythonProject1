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
#Program: cast_to_integer.py
#Author: Your Name
#Last date modified: 08/24/2023
#The purpose of this program is to accept any input,
#convert to a integer type and output the integer.

# Get user input
user_input = input("Enter a value: ")

try:
    # Convert the input to an integer
    converted_value = int(float(user_input))  # Convert to float first, then to int

    # Output the converted integer
    print("Converted to integer:", converted_value)
except ValueError:
    print("Input cannot expected")