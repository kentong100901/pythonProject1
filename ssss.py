# ***************************************************************
# Name : average_scores
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

def main():
    try:
        # Prompt the user for input
        last_name = input("Enter your last name: ")
        first_name = input("Enter your first name: ")
        age = int(input("Enter your age: "))

        # Define the number of scores to input
        NUM_SCORES = 3

        # Prompt the user for the test scores
        total_score = 0
        for i in range(NUM_SCORES):
            while True:
                try:
                    score = int(input(f"Enter score {i + 1} out of 100: "))
                    if score < 0 or score > 100:
                        raise ValueError("Score must be between 0 and 100.")
                    total_score += score
                    break  # Exit the loop if input is valid
                except ValueError as e:
                    print(f"Error: {e}. Please enter a valid score.")

        # Calculate the average score
        average_score = total_score / NUM_SCORES

        # Print the formatted output
        print(f"{last_name}, {first_name} age: {age} average grade: {average_score:.2f}")

    except ValueError as e:
        print(f"Error: {e}. Please enter a valid age.")

if __name__ == "__main__":
    main()
#Enter your last name: Tong
#Enter your first name: Than
#Enter your age: 21
#Enter score 1 out of 100: 100
#Enter score 3 out of 100: 100
#Tong, Than age: 21 average grade: 100.00



