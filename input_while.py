# ***************************************************************
# Name : input_while
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
# This script collects numbers from the user within the range of 1 to 100.
# It appends valid numbers to a list until the user inputs -1, then it prints the list.

# Initialize an empty list to store the numbers
numList = []

# Define the sentinel value for user input
sentinelValue = -1

# Prompt the user to enter a number and store it in the variable 'number'
number = int(input("Enter a number (-1 to stop): "))

# Continue the loop as long as 'number' is not equal to the sentinel value
while number != sentinelValue:
    # Continue the loop as long as 'number' is not within the range of 1 to 100
    while not (1 <= number <= 100):
        # Prompt the user to enter a number between 1 and 100 and store it in 'number'
        number = int(input("Enter a number between 1 and 100: "))

    # Add the valid number to the list
    numList.append(number)

    # Prompt the user to enter another number and update 'number'
    number = int(input("Enter a number (-1 to stop): "))

# Print the list using a for loop
for i in numList:
    print(i, end=" ")

# Test cases
# Test Case 1: Input 55, 12, 101, 3, -1
# Observed Output: 55 12 3
# Test Case 2: Input 200, 50, 75, 0, 25, -1
# Observed Output: 50 75 25
# Test Case 3: Input -1
# Observed Output: (No numbers entered)
# Test Case 4: Input 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, -1
# Observed Output: 5 10 15 20 25 30 35 40 45 50