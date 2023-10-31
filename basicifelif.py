# ***************************************************************
# Name : Basic if-elif Statement Assignment
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
while True:
    print("Welcome to Programmer's Toolkit Monthly Subscription Box!")
    print("Please select your membership level:")
    print("1. Platinum")
    print("2. Gold")
    print("3. Silver")
    print("4. Bronze")
    print("5. Free Trial")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        cost = 60.0
    elif choice == 2:
        cost = 50.0
    elif choice == 3:
        cost = 40.0
    elif choice == 4:
        cost = 30.0
    elif choice == 5:
        cost = 0.0
    else:
        print("Invalid choice. Please select a valid membership level.")
        continue

    print(f"You have selected the membership level and the cost is ${cost:.2f}.")

    another_choice = input("Do you like another level? (yes/no): ")
    if another_choice.lower() != "yes":
        print("Thank you for choosing Programmer's Toolkit Monthly Subscription Box!")
        break
