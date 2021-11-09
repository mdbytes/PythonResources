
number = int(input("Please enter an integer greater than zero?"))

number_factorial = 1

for x in range(1,number+1):
    number_factorial *= x

print("The factorial of",number,"is",number_factorial)
