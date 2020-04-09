# A Python Program to find the first xxx prime numbers, printing them out
# as a list:
#
# DEFINITION:  A prime number (or a prime) is a natural number greater than 1 
# that has no positive divisors other than 1 and itself. ... For example, 5 is 
# prime because 1 and 5 are its only positive integer factors, whereas 6 is 
# composite because it has the divisors 2 and 3 in addition to 1 and 6.

# Initializing key variables and lists
prime = [2,3]
primeCount = 2
y = 4
done = False

# Gathering the number of primes needed from the user
print('')
limit = int(input('How many prime numbers would you like? '))

# Algorithm to calculate prime numbers the needed number of times
while done != True:
    differences = []
    for x in range(2,y-1):
        diff = abs((y/x) - (y//x))
        differences.append(diff)
    minDiff = min(differences)
    if minDiff > 0:
        prime.append(y)
        primeCount += 1
    if primeCount == limit:
        done = True
    y += 1

# Printing results
print('')            
print('The first',limit,'prime numbers are as follows')
print('')
print(prime)
print('')
print('List size = ',len(prime))