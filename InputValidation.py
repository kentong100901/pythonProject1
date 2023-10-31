# ***************************************************************
# Name : Input Validation
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

def calculate_square_feet():

    try:
        length = float(input("Enter the length of the house in feet: "))
        width = float(input("Enter the width of the house in feet: "))

        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative.")

        square_feet = length * width

    except ValueError as e:
        print(f"Error: {e}. Please enter valid positive numbers.")

    else:
        print(f"The square footage of the house is {square_feet:.2f} square feet.")

    finally:
        print("Thank you!")

if __name__ == "__main__":
    calculate_square_feet()
