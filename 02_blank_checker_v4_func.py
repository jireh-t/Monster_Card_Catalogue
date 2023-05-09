"""Allows for blank checker function to be used on an integer box"""

import easygui


# Function to make sure input is entered and not left blank
def blank_checker(question, title, box):
    error_message = "You must fill out every field"

    if box == "enter":
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

    elif box == "integer":
        # Asks user for input
        answer = easygui.integerbox(question, title, lowerbound=1,
                                    upperbound=25)

        while True:  # Loops until valid input is entered
            if not answer:
                easygui.msgbox(error_message, "ERROR")  # Display error message
                answer = easygui.integerbox(question, title, lowerbound=1,
                                            upperbound=25)
            else:
                return answer


# Main Routine
monster = blank_checker("Enter monster name", "MONSTER", "enter")
easygui.msgbox(f"Monster name: {monster}")

speed = blank_checker("Enter the value for speed", "SPEED", "integer")
easygui.msgbox(f"Speed: {speed}")
