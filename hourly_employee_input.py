# ***************************************************************
# Name : hourly_employee_input
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
def hourly_employee_input():

    try:
        name = input("Enter the employee's name: ")
        hours_worked = int(input("Enter the hours worked: "))
        hourly_rate = float(input("Enter the hourly pay rate: "))

        if hours_worked < 0 or hourly_rate < 0:
            raise ValueError("Hours worked and hourly rate cannot be negative.")

        total_earnings = hours_worked * hourly_rate
        print(f"Employee: {name}\nHours Worked: {hours_worked}\nHourly Rate: ${hourly_rate:.2f}\nTotal Earnings: ${total_earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid input.")

if __name__ == "__main__":
    # Call the function with valid input
    print("Test 1: Valid Input")
    hourly_employee_input()

    # Call the function with negative numbers
    print("\nTest 2: Negative Numbers")
    hourly_employee_input()

    # Call the function with bad input (letters, symbols)
    print("\nTest 3: Bad Input")
    hourly_employee_input()
