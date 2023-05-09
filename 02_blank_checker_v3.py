"""Puts code from version 2 into a function and also having an error message
for when the user clicks cancel"""

import easygui


# Function to make sure input is entered and not left blank
def blank_checker(question, title):
    error_message = "You must fill out every field"

    # Asks user for input
    answer = easygui.enterbox(question, title)

    while True:  # Loops until valid input is entered
        if answer == "":  # Checks if it is blank
            easygui.msgbox(error_message, "ERROR")  # Display error message
            answer = easygui.enterbox(question, title)

        if not answer:
            easygui.msgbox(error_message, "ERROR")  # Display error message
            answer = easygui.enterbox(question, title)
        else:
            return answer


# Main Routine
monster = blank_checker("Enter monster name", "MONSTER")
easygui.msgbox(f"Monster name: {monster}")
