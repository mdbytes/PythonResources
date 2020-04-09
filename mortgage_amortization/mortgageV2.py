#  Martin Dwyer
#  Introduction to Programming Logic
#  Kirkwood Community College
#  Spring 2017
#  Chapter Five Howework
#
#  Mortgage Amortization Schedule:  With Functions
#
#  This programm will request input of mortgage loan data including the
#  mortgage dollar amount, interest rate, and term.  The program will use this
#  input to calculate a monthly amortization table for the term of the loan. 
#
#  The program is structured in eight functions:
#
#    main => the main function controlling the flow and final output
#            of the program.
#    paymentAmount => calculates fixed monthly payment given the loan input
#    printHeadings => function to format and print the headings
#    interestPaidThisPeriod => calculates monthly interest paid
#    principalPaidThisPeriod => calculates principal paid monthly    
#    totalInterestCalculator => calculates cumulative interest each month
#    remainingBalance => Calculates the remaining balance per month
#    endWell => A function to print summary data regarding the loan


#  The main function calls for data and controls the flow of the program
def main():

    # Step 1: Input and validate mortgage loan data (Amount, Rate, Term)
    print('')
    mortgageAmt = float(input('Enter mortgage amount ($):  '))
    while mortgageAmt <= 0:
        mortgageAmt = float(input('Re-enter positive amount  :'))
    print('')
    mortgageTerm = int(input('Enter the mortgage term (years):  '))
    while mortgageTerm <=0:
        mortgageTerm = int(input('Enter positive amount  :'))
    print('')
    interestRate = float(input('Enter interest rate (e.g. 5% = 5) :  '))
    while interestRate <=0:
        interestRate = float(input('Enter positive amount: '))
    #  Input for interest rate converted to percentage for calculation purposes
    annualIntRate = interestRate / 100
    
    #Step 2: Call function to calculate fixed monthly payment amount
    moPayment = paymentAmount(mortgageAmt,annualIntRate,mortgageTerm)
    
    #Step 3: Print headings for the amortization table
    printHeadings(moPayment)
  
    #Step 4: Product amortation table with loop including execution
    #        of functions for table elements each month.  Loop executes until
    #        the last month of the program, at which time the balance is zero.
    monthCount = 0
    totalInterest = 0
    endMonth = int(mortgageTerm*12)
    newBalance = mortgageAmt
    for monthCount in range(1,endMonth+1):
        iPaidPeriod = interestPaidThisPeriod(moPayment,annualIntRate,\
                                            newBalance)
        pPaidPeriod = principalPaidThisPeriod(moPayment,iPaidPeriod)
        totalInterest = totalInterestPaid(totalInterest,iPaidPeriod)
        newBalance = remaingingBalance(newBalance,pPaidPeriod)
        print(monthCount,'\t $',format(moPayment,'10,.2f'),'\t $',\
               format(pPaidPeriod,'10,.2f'),'\t $',\
               format(iPaidPeriod,'10,.2f'),'\t $',\
               format(totalInterest,'10,.2f'),'\t $',\
               format(newBalance,'10,.2f'))
  
    endWell(mortgageAmt,mortgageTerm,moPayment,totalInterest)

# Payment amount function (see https://www.mtgprofessor.com/formulas.htm)    
def paymentAmount(mortgageAmt,annualIntRate,mortgageTerm):
    effTerm = (mortgageTerm*12)
    effRate = (annualIntRate/12)
    moPayment = mortgageAmt*(effRate*((1+effRate)**effTerm))/\
                                        (((1+effRate)**effTerm)-1)
    return moPayment

# Headings, including fixed monthly payment amount, produced by this function
def printHeadings(moPayment):
    print('')
    print('')
    print('Payment Amount:  $',format(moPayment,',.2f'))
    print('')
    print('Your amortization schedule is printed below:  ')
    print('')
    print('\t\tMonthly\t\tMonthly\t\tMonthly\tCumulative\tRemaining')
    print('Month #\t\tPayment\t\tPrincipal\tInterst\tInterest\tBalance')
    print('')
    
#  Executing a loop for each loan month, up until the present month of the 
#  loop in main(), the interest paid in monthCount is calculated and returned
#  to the main function to continue processing.
def interestPaidThisPeriod(moPayment,annualIntRate,newBalance):
    effRate = annualIntRate / 12
    iPaidPeriod = effRate*newBalance
    return iPaidPeriod

#  Executing a loop for each loan month, up until the present month of the 
#  loop in main(), the principal paid in monthCount is calculated and returned
#  to the main function to continue processing.
def principalPaidThisPeriod(moPayment,iPaidPeriod):
    pPaidPeriod = moPayment - iPaidPeriod
    return pPaidPeriod

#  Executing a loop for each loan month, up until the present month of the 
#  loop in main(), the principal paid in monthCount is calculated and returned
#  to the main function to continue processing.
def totalInterestPaid(totalInterest,iPaidPeriod):
    totalInterest = totalInterest + iPaidPeriod
    return totalInterest

def remaingingBalance(newBalance,pPaidPeriod):
    nextBalance = newBalance - pPaidPeriod
    return nextBalance

#  Summary data and instructions printed at end of program    
def endWell(mortgageAmt,mortgageTerm,moPayment,totalInterest):
    print('')
    print('')
    print('Thank you for using our mortgage analyzer!')
    print('')
    print('We have analyzed your $',format(mortgageAmt,',.2f'),'mortgage.')
    print('')
    print('With term of',mortgageTerm,'years.')
    print('')
    print('And fixed monthly payment of $',format(moPayment,',.2f'))
    print('')
    print('TOTAL INTEREST over the term equal $',format(totalInterest,',.2f'))
    print('')
    print('Scroll up to review monthly amortization')
    
main()
