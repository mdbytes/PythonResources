


monthCount = 0
totalInterest = 0
mortgageAmount = float(input('Please enter mortgage amount ($):  '))
while mortgageAmount <= 0:
    mortgageAmount = float(input('Please re-enter mortgage amount greater than zeror(4)  :'))
mortgageTerm = int(input('Please enter the mortgage term (years):  '))
while mortgageTerm <=0:
    mortgageTerm = int(input('Please re-enter mortgage term greater than zero(years)  :'))
annualInterestRate = float(input('Please enter annual interest rate as decimal (5% = 0.05) :'))
while annualInterestRate <=0:
    annualInterestRate = float(input('Please re-enter interest rate as a positive number (5% = 0.05) :'))
effTerm = (mortgageTerm*12)
effRate = (annualInterestRate/12)
paymentAmount = mortgageAmount*(effRate*((1+effRate)**effTerm))/(((1+effRate)**effTerm)-1)

print('Payment Amount:  $',format(paymentAmount,',.2f'))
print('Your amortization schedule is printed below:  ')
print('')
print('Payment\t      Payment   \t    Principle  \t    Interest   \t      Total      \t    Balance')
print('Number \t       Amount    \t     Portion    \t     Portion    \t    Interest \t    Remaining')

for monthCount in range(1,effTerm+1):
    iPaidPeriod = effRate*mortgageAmount
    pPaidPeriod = paymentAmount - iPaidPeriod
    totalInterest = totalInterest + iPaidPeriod
    mortgageAmount = mortgageAmount - pPaidPeriod
    print(monthCount,'\t $',format(paymentAmount,'10,.2f'),'\t $',\
          format(pPaidPeriod,'10,.2f'),'\t $',format(iPaidPeriod,'10,.2f'),'\t $',\
          format(totalInterest,'10,.2f'),'\t $',format(mortgageAmount,'10,.2f'))
    
print('Thanks for using our program!')
print('')
print('You paid $',format(totalInterest,',.2f'),'in total interest')
