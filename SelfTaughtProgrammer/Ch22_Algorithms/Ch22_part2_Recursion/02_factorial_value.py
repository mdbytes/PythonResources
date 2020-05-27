"""
Write a function called fact that recursively calculates the factorial value of its parameter, which is an integer value.
"""


def n_factorial(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n*n_factorial(n-1)


print(n_factorial(3))


