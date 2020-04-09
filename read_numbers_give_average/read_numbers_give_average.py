#   Martin Dwyer
#   Introduction to Programming Logic
#   Kirkwood Community College
#   Chapter Six: In-Class Assignment
#
#   Prompt the user for the name of a file. Attempt to open the file.
#   Keep prompting the user to enter a name until a valid filename is given.
#   Once open, add up all of the values in the file and calculate and print 
#   the average. Note, the file may contain invalid values, such as a letter
#   instead of a number, or possibly NO values. Deal with it!

#   Create your own input file to test with, using your own first name.txt

#   Submit both your .py file and your sample .txt input file. \

def main():
    #Welcome the user
    print('')
    print('This program is intended to receive a text file with a series')
    print('of numnbers, take those numbers, and return to the user an')
    print('accurate count and average for the numbers.')
    print('')
    
    #Setting condition fileName to reflect whether or not proper name has been
    #acquired from the user
    fileName = False
    
    while fileName == False:
        
        #Attempt to get a proper filename from the user
        try:
            getFile = input('Enter filename here: ')
            numberFile = open(getFile,'r')
    
        #If filename not valid, advise user to verify file and try again
        except FileNotFoundError: 
            print('')
            print('You did not enter a proper filename')
            print('Please verify the filename and try again!')
            print('')
        
        #If filename is valid, acknowledge and move onto data analysis    
        else:
            print('')
            print('Filename',getFile,'has been validated')
            print('')
            fileName = True
    
    #Initializing accumulator variables for calculation of average
    count = 0
    total = 0
    invalids = 0
    
    #Initiating reading and validation of data in file
    for line in numberFile:
        
        #Convert the string text to numeric data
        try:
            value = float(line)    
        
        #Exclude invalid data from the calculations
        except ValueError:
            invalids +=1

        #Accumulate valid numeric data from the file for analysis
        else:
            total += value
            count += 1
    
    if count > 0:
        #Calculate the average using the valid numeric data accumulated above
        average = total / count
    
        #Report the average of the numeric file data
        print('The average of the numbers in the file is:  ',\
              format(average,'.2f'))
        print('')
        print('The program found',count,'valid numbers in the file.')
        print('')
    
        #Report a warning to the user if the file contained invalid data
        if invalids > 0:
            print('WARNING: The file included invalid numeric items which ')
            print('are excluded from the average calculation.')
            print('')
            print('A total of',invalids,'invalid numbers were in the file.')
            print('')
            print('Please review the file and resubmit if necessary')

    else:
        print('The file contains no valid numeric data to be gathered.')
        print('Please review the file and run the program again.')

    numberFile.close()
    
main()        
        
    
