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
import tkinter as tk

# Function to update the "Waiting" label when a Checkbutton is checked
def checkbutton_checked():
    selected_meals = [meal for meal, var in zip(meals, meal_vars) if var.get() == 1]
    waiting_label.config(text=f"Waiting for: {', '.join(selected_meals)}")

# Create the main application window
app = tk.Tk()
app.title("Favorite Meal")

# List of meal options and their associated IntVar
meals = ["Breakfast", "Second Breakfast", "Lunch", "Dinner"]
meal_vars = [tk.IntVar() for _ in range(len(meals))]

# Create Checkbuttons for each meal
for i, meal in enumerate(meals):
    checkbutton = tk.Checkbutton(app, text=meal, variable=meal_vars[i], command=checkbutton_checked)
    checkbutton.grid(row=i, column=0, sticky=tk.W)

# Create the "Waiting" label
waiting_label = tk.Label(app, text="Waiting for:")
waiting_label.grid(row=4, column=0, sticky=tk.W)

# Create the "Exit" button
exit_button = tk.Button(app, text="Exit", command=app.quit)
exit_button.grid(row=5, column=0)

# Start the Tkinter main loop to run the application
app.mainloop()


