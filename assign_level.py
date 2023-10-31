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
def switch_level(level):
    points_dict = {
        'N': 50,
        'B': 150,
        'E': 300,
        'A': 500
    }

    # Use get() method to handle the case where the level is not found in the dictionary.
    points = points_dict.get(level, "Invalid level")

    return points


def main():
    levels = ['N', 'B', 'E', 'A', 'S']  # 'S' is an example of an invalid level

    for level in levels:
        points = switch_level(level)
        print(f"Level: {level}, Points: {points}")


if __name__ == "__main__":
    main()
