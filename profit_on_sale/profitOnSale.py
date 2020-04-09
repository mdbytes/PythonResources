# Goal is to determine profit from stock transaction
# Welcome user and state purpose
print('WELCOME TO OUR STOCK PROFIT CALCULATOR!')
print(' ')
print('This program save you time and give you quick insight!')
print(' ')
print('Your profit or loss on the sale of stock will be calculated.')
print('We will just need to collect some information first:')
print(' ')
# Now the program will prompt user for stock purchase information.
# Variables will be defined for shares purchased, purchase price, commission.
numSharesBuy = int(input('How many shares did you purchase? '))
pricePerShareBuy = float(input('What was the price per share purchased? '))
commRateBuy = float(input('What percentage commission was paid? '))
# Now the program will prompt user for stock sale information.
# Variables will be defined for shares sold, sales price, commission.
print(' ')
print(' ')
numSharesSold = int(input('How many shares did you sell? '))
pricePerShareSold = float(input('What was the price per share sold? '))
commRateSold = float(input('What percentage commission was paid? '))
# Calculate total purchase cost, net sale proceeds, and profit.
totalBuyPrice = pricePerShareBuy * numSharesBuy *(1 + (commRateBuy/100))
totalSellPrice = pricePerShareSold * numSharesSold * (1 - (commRateSold/100))
profitStockSell = totalSellPrice - totalBuyPrice
# Print formatted output and statement of appreciation.
print('  ')
print('  ')
print('HERE IS A SUMMARY OF YOUR STOCK TRANSACTION:')
print('  ')
print('Cost of buying',numSharesBuy,'shares was $',format(totalBuyPrice,',.2f'))
print('  ')
print('Net proceeds from selling',numSharesSold,'shares was $',\
      format(totalSellPrice,',.2f'))
print('  ')
print('The net profit/(loss) on the sale was $', \
      format(profitStockSell,',.2f'))
print('  ')
print('Thank you for using our stock profit calculator!')
print('  ')
print('HAVE A GREAT DAY!')
