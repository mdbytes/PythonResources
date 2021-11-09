

new_number = 0.0
sum_of_numbers = 0.0

while new_number >=0:
    new_number = float(input("Enter another number (negative numbers mark the end)"))
    if new_number >= 0:
        sum_of_numbers += new_number

print(sum_of_numbers)