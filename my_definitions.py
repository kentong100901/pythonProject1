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




# Function to print a friendly greeting
def greeting():
    print("Hello! Welcome to my Python module.")

# Function to print the author's name
def message():
    print("Author: Than Tong")

# Function to print dictionary key-value pairs
def print_dict(input_dict):
    for key, value in input_dict.items():
        print(f"{key}: {value}")

# Function to print set items
def print_set(input_set):
    for item in input_set:
        print(item)

# Call the greeting function
greeting()

# Call the message function
message()

# Create a sample dictionary
sample_dict = {
    "name": "Ken",
    "age": 22,
    "city": "IOWA"
}


# Call the print_dict function to print the dictionary
print_dict(sample_dict)

# Create a sample set
sample_set = {1, 2, 3, 4, 5}

# Call the print_set function to print the set
print_set(sample_set)

