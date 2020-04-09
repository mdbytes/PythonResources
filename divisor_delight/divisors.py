# Martin Dwyer
# Introduction to Programming Logic
# Homework:  Chapter 4
#
# Solve the following problem:
# Prompt the user to enter 2 numbers, x and y. 
# Then, output all of the common divisors of x and y, one per line, 
# excluding 1 and 2. Note, x may be greater than, less than, or equal to y 
# so you may want to check that.   Also, make sure that both x and y are 
# positive values.  Keep repeating the program until the user replies "n" 
# or "N" if they'd like to continue.

#Welcome user
print('')
print('Welcome to Divisor Delight')
print('')
print('Where we will find all common divisors for two positive integers')
print('You will need to provide two positive integers greater than zero')
print('')

#set initial values of key variables
d = 'c'

#initiate program loop with sentinel value "n" or "N"
while d != 'n' and d != 'N':
    print('')
    
    #Input x and y and validate input
    x = float(input('Value for first integer: '))
    while (x < 0) or (x != int(x)):
        print('')
        print('ERROR: Must enter integer greater than zero.')
        x = int(input('Value for first integer: '))
    y = float(input('Value for second integer: '))
    while (y < 0) or (y != int(y)):
        print('')
        print('ERROR: Must enter integer greater than zero.')
        y = int(input('Value for second integer: '))
    
    #Calculate and print common divisors    
    g = int(max(x,y))
    print('')
    print('The common divisors of ',x,' and ',y,' excluding 1 and 2 are:')
    print('')
    for k in range(3,g+1):
        if (x%k) == 0:
            if (y%k) == 0:
                print('\t\t',k)
            else:
                k += 1
        else: 
            k += 1
    
    #Prepare to continue on to next pair of integers
    print('')
    print('Press ENTER to continue to next pair of integers')
    d = input('Enter "n" or "N" to quit:  ')
    print('')
    
#End with gratitude
print('')
print('')
print('Thank you for using Divisor Delight')
print('We hope you found the answers you were looking for')
print('Have a great day!')
print('')
print('')

#This program was tested for the following test cases
#
#     x    y    Result
#    -1    7    Re-input valid data for x
#     1    7    None
#    7    -1    Re-input valid data for y
#    7     1    None
#    5    10    5
#    6   162    3, 6
#   1360 640    4, 5, 8, 10, 16, 20, 40, 80
        
    
        
