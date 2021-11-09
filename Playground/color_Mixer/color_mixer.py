#   FILE:   color_mixer.py
#   DATE:   2021-09-24
#   AUTHOR: <student name here>
#   DESCRIPTION: Determining Colors
"""
This file determines output of two primary colors

"""

import sys

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80

def main(argv):
    """
    A program allowing users to input rectangle length and width
    The program calculates the areas and determines which rectangle is bigger

    INPUTS:
    colors, strings

    OUTPUTS:
    secondary color

    """
    
    # Show the program title
    program_title = "Area of Rectangles"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    
    color_one = input("Color one: ")
    color_two = input("Color two: ")

    if color_one == "red" and color_two == "blue":
        secondary_color = "purple"
    elif color_one == "blue" and color_two == "red":
        secondary_color = "purple"
    elif color_one == "red" and color_two =="yellow":
        secondary_color = "orange"





    else:
        secondary_color = "Error:  Colors input not recognized."

    print(secondary_color)

    print("\nProgram complete.\n")


# Call main()
if __name__ == "__main__":
    main(sys.argv)



