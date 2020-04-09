effTerm = 0
effRate = 0
mortgageAmount = float(input('Please enter mortgage amount ($):  '))
while mortgageAmount <= 0:
    mortgageAmount = float(input('Please re-enter mortgage amount greater than zeror(4)  :'))
mortgageTerm = int(input('Please enter the mortgage term (years):  '))
while mortgageTerm <=0:
    mortgageTerm = float(input('Please re-enter mortgage term greater than zero(years)  :'))
annualInterestRate = float(input('Please enter annual interest rate as decimal (5% = 0.05) :'))
while annualInterestRate <=0:
    annualInterestRate = float(input('Please re-enter interest rate as a positive number (5% = 0.05) :'))
effTerm = mortgageTerm * 12
effRate = annualInterestRate / 12
paymentAmount = mortgageAmount*(effRate*((1+effRate)**effTerm))/(((1+effRate)**effTerm)-1)

print(paymentAmount)
