magic_number = 2

while(True):
    selection = int(input("I'm thinking of a number between 0 and 10.  Can you guess it?\nEnter Here:  "))
    if selection==magic_number:
        print("Right!  Your're good!")
    else:
        print("Wrong!")
    play_again = input("Enter q to quit, or Enter to play again.")
    if play_again == "q":
        print("Thanks for playing")
        break