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
def measurements(a_list):
    def area(a_list):
        if len(a_list) == 1:
            # Calculate the area of a square
            return a_list[0] ** 2
        elif len(a_list) == 2:
            # Calculate the area of a rectangle
            return a_list[0] * a_list[1]

    def perimeter(a_list):
        if len(a_list) == 1:
            # Calculate the perimeter of a square
            return 4 * a_list[0]
        elif len(a_list) == 2:
            # Calculate the perimeter of a rectangle
            return 2 * (a_list[0] + a_list[1])

    # Calculate the area and perimeter based on the length of the input list
    if len(a_list) == 1:
        area_value = area(a_list)
        perimeter_value = perimeter(a_list)
        return f"Perimeter = {perimeter_value:.2f} Area = {area_value:.2f}"
    elif len(a_list) == 2:
        area_value = area(a_list)
        perimeter_value = perimeter(a_list)
        return f"Perimeter = {perimeter_value:.2f} Area = {area_value:.2f}"
    else:
        return "Invalid input: The input list must contain 1 or 2 values."

if __name__ == '__main__':
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    print(result)
    square = [3.5]
    result = measurements(square)
    print(result)
