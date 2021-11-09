
bugs = 0
for x in range(5):
    question = "How many bugs on day " + str(x+1) +"?"
    new_bugs = int(input(question))
    bugs = bugs + new_bugs

print("There were a total of",bugs,"bugs over the five days.")
