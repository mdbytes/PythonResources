# Goal of program is to determine type of triangle given length of three sides.
# Program will consist of three parts;
# 1. Prompt and input of data
# 2. Triangle type testing (equilateral, isosceles, scalene)
# 3. Triangle class testing (right, acute, obtuse)

# Welcome user to program, including description of what will be needed.

print('Welcome to our program, the triangle analyzer!')
print('You give us the information - we do all the work!')
print('We only need the length of the three sides of a triangle')
print('The program will tell you the triangle type and class.')
print('Start now by entering your triangle side lengths')
print('')
print('')

# Prompt user for length of triangle sides.

sideOne = float(input('What is the length of the first side?  '))
sideTwo = float(input('What is the length of the second side?  '))
sideThree = float(input('What is the length of the third side?  '))
longestSide = max (sideOne, sideTwo, sideThree)

# Testing for equilateral triangles (equal sides)

if sideOne == sideTwo and sideTwo == sideThree and sideThree == sideOne:
    print('')
    print('')
    print('This triangle is an equilateral triangle with 3 equal sides.')
    print('')
        
# Testing for isosceles triangles (two equal sides)

if (sideOne == sideTwo and sideTwo != sideThree) \
   or (sideOne != sideTwo and sideTwo == sideThree) \
   or (sideOne == sideThree and sideTwo !=sideOne):
    print('')
    print('')
    print('This triangle is an isosceles triangle with 2 equal sides.')       
    print('')

# Testing for scalene triangles (unequal sides)

if sideOne != sideTwo and sideTwo != sideThree and sideOne != sideThree:
    print('')
    print('')
    print('This triangle is a scalene triangle, with no equal sides.')
    print('')
    
# Testing for angle class (acute, right, obtuse for scalene triangles)
# Scenario 1: SideOne is longest side
    
if sideOne == longestSide: 

    cSquared = sideOne**2

    if cSquared == (sideTwo**2 + sideThree**2):
        print('This is a right triangle.')
        print('')
        print('The angle opposite the longest side is 90 degrees')
        print('')

    if cSquared < (sideTwo**2 + sideThree**2):
        print('The triangle is acute.')
        print('')
        print('The angle opposite the longest side is less than 90 degrees.')
        print('')

    if cSquared > (sideTwo**2 + sideThree**2):
        print('The triangle is obtuse.')
        print('')
        print('The angle opposite the longest side is greater than 90 degrees.')
        print('')

# Testing for angle class (acute, right, obtuse for scalene triangles)
# Scenario 2: SideTwo is longest side
    
elif sideTwo == longestSide: 

    cSquared = sideTwo**2

    if cSquared == (sideOne**2 + sideThree**2):
        print('This is a right triangle.')
        print('')
        print('The angle opposite the longest side is 90 degrees')
        print('')
    
    if cSquared < (sideOne**2 + sideThree**2):
        print('The triangle is acute.')
        print('')
        print('The angle opposite the longest side is less than 90 degrees.')
        print('')

    if cSquared > (sideOne**2 + sideThree**2):
       print('The triangle is obtuse.')
       print('')
       print('The angle opposite the longest side is greater than 90 degrees.')
       print('')

# Testing for angle class (acute, right, obtuse for scalene triangles)
# Scenario 3: SideThree is longest side

elif sideThree == longestSide:
    
    cSquared = sideThree**2

    if cSquared == (sideOne**2 + sideTwo**2):
        print('This is a right triangle.')
        print('')
        print('The angle opposite the longest side is 90 degrees')
        print('')
    
    if cSquared < (sideOne**2 + sideTwo**2):
        print('The triangle is acute.')
        print('')
        print('The angle opposite the longest side is less than 90 degrees.')
        print('')

    if cSquared > (sideOne**2 + sideTwo**2):
        print('The triangle is obtuse.')
        print('')
        print('The angle opposite the longest side is greater than 90 degrees.')
        print('')

# Ending program with gratitude

print('Thank you for using our program!')
print('')
print('')

# Test Cases
# 3,3,3 equilateral, acute (all equilateral angles are less than 90 degrees)
# 9, 40, 41 scalene, right
# 9, 40, 35 scalene, obtuse
# 3, 3.05, 2.95 scalene, acute
# 10, 10, 3 isosceles, acute
# 10, 10, 18 isosceles, obtuse
# no test case (square root 2 involved) isosceles, right.


