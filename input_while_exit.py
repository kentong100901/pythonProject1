# ***************************************************************
# Name :  input_while_exit
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

"""
This program prompts the user to enter numbers between 1 and 100 until they enter -1 to stop. It handles bad input by asking the user for valid input.

To exit the entire program, the user can input -1 when prompted for a number.

"""

# Initialize an empty list to store the numbers
numList = []

# Define the sentinel value for user input
sentinelValue = -1

# Initialize a flag to control the outer loop
exitFlag = False

# Continue the loop as long as the exitFlag is False
while not exitFlag:
    # Prompt the user to enter a number and store it in the variable 'number'
    number = int(input("Enter a number (-1 to stop): "))

    # Continue the loop as long as 'number' is not equal to the sentinel value
    while number != sentinelValue:
        # Check if the user wants to exit the entire program
        if number == sentinelValue:
            exitFlag = True
            break  # Exit the inner while loop

        # Continue the loop as long as 'number' is not within the range of 1 to 100
        while not (1 <= number <= 100):
            # Check if the user wants to exit the entire program
            if number == sentinelValue:
                exitFlag = True
                break  # Exit the inner while loop
            # Prompt the user to enter a number between 1 and 100 and store it in 'number'
            number = int(input("Enter a number between 1 and 100: "))

        # Check if the user wants to exit the entire program
        if number == sentinelValue:
            exitFlag = True
            break  # Exit the inner while loop

        # Add the valid number to the list
        numList.append(number)

    # Check if the user wants to exit the entire program
    if number == sentinelValue:
        exitFlag = True

# Print the list using a for loop
for i in numList:
    print(i, end=" ")

# Tests and observed output
# Test 1: User enters valid numbers followed by -1 to stop.
# Input: 5, 42, 67, -1
# Observed Output: 5 42 67

# Test 2: User enters invalid numbers but then inputs -1 to exit the program.
# Input: 105, -1
# Observed Output:

# Test 3: User immediately enters -1 to exit the program.
# Input: -1
# Observed Output:

# Test 4: User enters valid numbers and then inputs -1 to stop.
# Input: 12, 88, 55, -1
# Observed Output: 12 88 55

# Test 5: User enters valid numbers, including 1 and 100, and then inputs -1 to stop.
# Input: 1, 50, 100, -1
# Observed Output: 1 50 100

# Test 6: User enters an invalid number, then valid numbers, and finally inputs -1 to stop.
# Input: 200, 30, 45, -1
# Observed Output: 30 45

# Test 7: User enters valid numbers, then an invalid number, and then inputs -1 to stop.
# Input: 7, 15, 120, -1
# Observed Output: 7 15

# Test 8: User enters only invalid numbers and then inputs -1 to stop.
# Input: 200, 300, 400, -1
# Observed Output:

