import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("movies.txt","w",newline='') as f:
    w = csv.writer(f, delimiter=",")
    for list in movies:
        w.writerow(list)
