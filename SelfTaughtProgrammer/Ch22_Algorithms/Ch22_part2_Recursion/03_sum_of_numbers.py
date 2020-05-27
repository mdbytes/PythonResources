"""
Write a function named sum that accepts a variable containing an integer
value as its parameter and returns the sum of the numbers from 1 to to
the parameter (calculated recursively).
"""


def sum_of_numbers(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n-1)


print(sum_of_numbers(1))
print(sum_of_numbers(2))
print(sum_of_numbers(5))
print(sum_of_numbers(100))



