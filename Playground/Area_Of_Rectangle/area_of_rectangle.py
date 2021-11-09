
#   FILE:   area_of_rectangle.py
#   DATE:   2021-09-24
#   AUTHOR: <student name here>
#   DESCRIPTION: Calculating and comparing areas of rectangles
"""
This file calculates and compares rectangles

"""

import sys

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80

def main(argv):
    """
    A program allowing users to input rectangle length and width
    The program calculates the areas and determines which rectangle is bigger

    INPUTS:
    rectangle length, float
    rectangle width, float

    OUTPUTS:
    area of two rectangles
    display of which rectangle is bigger

    """
    
    # Show the program title
    program_title = "Area of Rectangles"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    
    rectangle_one_length = float(input("What is the length of the first rectangle? "))
    rectangle_one_width = float(input("What is the width of the first rectangle? "))

    rectangle_one_area = rectangle_one_length * rectangle_one_width

    rectangle_two_length = float(input("What is the length of the second rectangle? "))
    rectangle_two_width = float(input("What is the width of the second rectangle? "))

    rectangle_two_area = rectangle_two_length * rectangle_two_width

    if rectangle_one_area > rectangle_two_area:
        bigger_rectangle = "rectangle one"
    else:
        bigger_rectangle = "rectangle two"

    print("The area of rectangle one: ", rectangle_one_area)
    print("The area of rectangle two: ", rectangle_two_area)
    print("The rectangle with the bigger area is", bigger_rectangle)

    print("\nProgram complete.\n")


# Call main()
if __name__ == "__main__":
    main(sys.argv)



