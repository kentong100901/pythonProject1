# ***************************************************************
# Name : list program
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
# Create the list
list_one = ['the', 'big', 'dog']
print(list_one)


# append another string to the list
list_one.append('pig')

#  print the new list
print(list_one)

# copy the list to another list
list_two = list_one.copy()

# print both lists
print("list One: ")
print(list_one)
print("List two: ")
print(list_two)

# get string at index 2
print("String at index 2: ")
print(list_one[2])

# first add dog 3 times to the list
list_one.append('dog')
list_one.append('dog')
list_one.append('dog')

# print the list
print("List one: ")
print(list_one)

# count the number of times dog is in the list
print("Number of times dog is in the list: ")
print(list_one.count('dog'))

#  print the list
print("List one: ")
print(list_one)

# insert a string at index 2
list_one.insert(2, 'fox')

# print the list
print("List one after inserting fox: ")
print(list_one)

# remove the string at index 2
list_one.remove('fox')

# print the list
print("List one after removing fox: ")
print(list_one)

# reverse the list
list_one.reverse()

# print the list
print("List one after reversing: ")
print(list_one)

# sort the list
list_one.sort()

# print the list
print("List one after sorting: ")
print(list_one)

# clear the list
list_one.clear()

# print the list
print("List one after clearing: ")
print(list_one)