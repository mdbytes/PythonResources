martin = {"height": 76, "favorite_color": "blue","favorite_author": "Ernest Hemingway"}

def app():
    print("Which would you like to know?")
    print("1. Height")
    print("2. Favorite Color")
    print("3. Favorite Author")
    selection = int(input("Selection: "))
    if(selection == 1):
        print(martin["height"])
    elif(selection == 2):
        print(martin["favorite_color"])
    else:
        print(martin["favorite_author"])

if __name__ == "__main__":
    app()