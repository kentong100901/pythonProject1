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
def average_scores(*scores, **kwargs):
    name = kwargs.get('name', 'Unknown')
    course = kwargs.get('course', 'N/A')
    gpa = kwargs.get('gpa', 0.0)

    if len(scores) > 0:
        average = sum(scores) / len(scores)
    else:
        average = 0.0

    result = f"Result: name = {name} gpa = {gpa} course = {course} with current average {average:.1f}"
    return result

# Function calls with different number of scores and keyword arguments
result1 = average_scores(95, 87, 91, name="Ken", course="English", gpa=3.5)
result2 = average_scores(78, 85, 92, 88, name="Bo", course="History", gpa=3.2)
result3 = average_scores(name="HAM", course="Teachnolory", gpa=3.0)

# Print the results
print(result1)
print(result2)
print(result3)
