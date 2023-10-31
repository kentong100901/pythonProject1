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

# Function used to return the string with test name and score if it passes validation;
# otherwise return the test name with invalid_message
def score_input(test_name, test_score=-1, invalid_message='Invalid test score!'):
    # Try to validate test score
    try:

        # Convert test score into integer
        test_score = int(test_score)

        # If test score is between 0 to 100
        if 0 <= test_score <= 100:

            # Return the string with test name and score
            return f"{test_name}: {test_score}"

        # If test score is not between 0 to 100
        else:

            # Return the test name with invalid_message
            return f"{test_name}: {invalid_message}"

    # If the test score in not an integer
    except ValueError:

        # Return the test name with ValueError
        return f"{test_name}: ValueError encountered!"


# Main method
def main():
    # Test 1 for one good input
    display_string = score_input('Test 1', 70)
    print(display_string)

    # Test 2 for one value below range
    display_string = score_input('Test 2', -5)
    print(display_string)

    # Test 3 for one value above range
    display_string = score_input('Test 3', 110)
    print(display_string)

    # Test 4 for one non-numeric input
    display_string = score_input('Test 4', 'Seventy')
    print(display_string)


# Call main function
if __name__ == '__main__':
    main()