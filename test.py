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
# Let's set the maximum and minimum values.
MAX = 10
MIN = 0

# Now, we'll assign a value to 'y'.
y = 4

# Is 'y' above the maximum?
if y > MAX:
    print("Yes, 'y' is above the maximum.")
else:
    print("No, 'y' is not above the maximum.")

# Is 'y' below the minimum?
if y < MIN:
    print("Yes, 'y' is below the minimum.")
else:
    print("No, 'y' is not below the minimum.")

# Now, let's set a value for 'x'.
x = 8

# Is 'x' between the minimum and maximum, but not equal to them?
if MIN < x < MAX:
    print("'x' is between the minimum and maximum, but not equal to either.")
else:
    print("'x' is not between the minimum and maximum in the specified way.")

# Is 'x' within the range from the minimum up to, but not including, the maximum?
if MIN <= x < MAX:
    print("'x' is within the range from the minimum up to (but not including) the maximum.")
else:
    print("'x' is not within that range.")

# Finally, is 'x' above the minimum up to and including the maximum?
if MIN <= x <= MAX:
    print("'x' is above the minimum up to and including the maximum.")
else:
    print("'x' is not in this range.")
