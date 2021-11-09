
total_expenses = 0
budget_amount = float(input("What is your budget for the month? "))

spending = True
expense_number = 1

while spending: 
    question = "How much is expense number " + str(expense_number) + "?"
    expense = float(input(question))
    total_expenses = total_expenses + expense
    expense_number += 1
    answer = input("Do you want to enter another expense? (enter 'Y')")
    if answer != "Y":
        spending = False

over_under_budget = budget_amount - total_expenses

if over_under_budget >= 0:
    print("Congrats!  You are ",format(over_under_budget,'.2f')," under budget for spending.")
else:
    print("Bummer!  You are ",format(over_under_budget,'.2f')," over budget for spending.")
