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
# Define a function named calculate_area that calculates the area of a rectangle.
# Define a function named calculate_area that calculates the area of a rectangle.
# Define a function named multiply_string that repeats a message n times.
def multiply_string(kenken, n):
    result = ""
    for i in range(n):
        result += kenken
    return result

# Calling the multiply_string function with 'Python!' and 4 as parameters.
if __name__ == '__main__':
    result = multiply_string('Ken!', 6)
    print(result)