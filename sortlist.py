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
def sort_list(input_list):

    sorted_list = sorted(input_list)
    return sorted_list

def search_list(input_list, target):

    return target in input_list

def main():
    # Hard-coded list for demonstration purposes
    my_list = [1, 2, 3, 4, 5, 6]

    # Call sort_list() to sort the list
    sorted_my_list = sort_list(my_list)
    print("Sorted List:", sorted_my_list)

    # Call search_list() to search for an element
    target_element = 7
    if search_list(sorted_my_list, target_element):
        print(f"{target_element} found in the list.")
    else:
        print(f"{target_element} not found in the list.")

if __name__ == "__main__":
    main()
