"""Version 2 of blank checker, puts code from v2 into a loop"""

import easygui

# Asks user for input
monster_name = easygui.enterbox("Enter monster name", "MONSTER NAME")

while True:
    if monster_name == "":  # Checks if it's blank
        # Display error message
        easygui.msgbox("You must fill out every field", "ERROR")

        # Asks again
        monster_name = easygui.enterbox("Enter monster name", "MONSTER NAME")

    else:
        easygui.msgbox(f"Monster name: {monster_name}")  # Display answer
        break
