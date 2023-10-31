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
def hourly_employee_input():

    try:
        name = input("Enter the employee's name: ")
        hours_worked = float(input("Enter the hours worked: "))
        hourly_rate = float(input("Enter the hourly pay rate: "))

        if hours_worked <= 0 or hourly_rate < 0:
            raise ValueError("Hours worked must be greater than 0, and hourly rate cannot be negative.")

        total_pay = weekly_pay(hours_worked, hourly_rate)
        return f"{name} made ${total_pay:.2f} after working {hours_worked} hours at a rate of ${hourly_rate:.2f}"

    except ValueError as e:
        return f"Error: {e}. Please enter valid input."

def weekly_pay(hours_worked, hourly_rate):
    """
    Calculate the weekly pay based on hours worked and hourly pay rate.
    """
    return hours_worked * hourly_rate

if __name__ == "__main__":
    result = hourly_employee_input()
    print(result)
