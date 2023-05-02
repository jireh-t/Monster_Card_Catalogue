"""Version 1 of blank checker, makes sure the input is not left blank"""

import easygui

# Asks user for input
monster_name = easygui.enterbox("Enter monster name", "MONSTER NAME")

if monster_name == "":  # Checks if it's blank
    easygui.msgbox("You must fill out every field", "ERROR")  # Display error
    # message

    # Asks again
    monster_name = easygui.enterbox("Enter monster name", "MONSTER NAME")
    easygui.msgbox(f"Monster name: {monster_name}")  # Displays answer

else:
    easygui.msgbox(f"Monster name: {monster_name}")  # Display answer
