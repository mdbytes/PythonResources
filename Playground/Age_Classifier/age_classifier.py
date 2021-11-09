#   FILE:   age_classifier.py
#   DATE:   2021-09-24
#   AUTHOR: <student name here>
#   DESCRIPTION:    A program for classifying ages
"""
User enters age and program determines classification

"""

import sys

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80

def main(argv):
    """
    A program for User to enter age and determine age classification

    INPUTS:
    age, an integer
        
    OUTPUT:
    age classification, a string

    """
    # Show the program title
    program_title = "Age Classifier"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    
    age = int(input("Please enter age: "))

    if age <= 1:
        age_classification = "infant"
    elif age < 13:
        age_classification = "child"
    elif age < 20:
        age_classification = "teenager"
    else:
        age_classification = "adult"
    
    print("The age classification for", age,"years old is", age_classification)

    print("\nProgram complete.\n")


# Call main()
if __name__ == "__main__":
    main(sys.argv)

