
starting_organisms = int(input("Starting number of organisms: "))
average_daily_increase = float(input("Average daily increase (example: 30% enter .30):"))
number_days = int(input("Number of days to multiply"))

print("Day Approximate\tPopulation")

total_population = starting_organisms
print("1\t\t",total_population)

for i in range(2,number_days+1):
    total_population *= (1 + average_daily_increase)
    print(i,"\t\t",total_population)


