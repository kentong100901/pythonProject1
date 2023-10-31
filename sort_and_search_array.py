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
my_list = [5, 3, 6, 2, 10]

def sort_array(nums):
    """Sorts the list in-place."""
    nums.sort()

def search_array(nums, target):
    """Searches for target in nums and returns the index if found, else -1"""
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

# Sort the list using sort_array() (in-place)
sort_array(my_list)
print("Sorted List:", my_list)

# Search for an item in the list using search_array() and print the result
target_item = 5
result = search_array(my_list, target_item)

if result != -1:
    print(f"{target_item} found at index {result}")
else:
    print(f"{target_item} not found in the list")
#The sort_array() function sorts the list in-place so there is no need to return anything. The comment explains why there is no return statement.

#The search_array() function returns either the index if the target is found, or -1 if not found.