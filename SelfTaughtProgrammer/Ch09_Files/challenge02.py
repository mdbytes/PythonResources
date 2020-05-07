breakfast = input("What did you have for breakfast?  ")
with open("breakfast.txt","w") as f:
    f.write(breakfast)
