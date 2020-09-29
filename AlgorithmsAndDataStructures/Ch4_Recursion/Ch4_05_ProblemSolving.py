"""
Continued solutions to select problems from MyProgrammingLab problems - Getting started with Python
"""

"""
Write a function called fact that recursively calculates the factorial value of its parameter, which is an integer value.
"""


def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(10))

"""
The sum of the numbers 1 to n can be calculated recursively as follows:
The sum from 1 to 1 is 1.
The sum from 1 to n is n more than the sum from 1 to n-1
Write a function named sum that accepts a variable containing an integer value as its parameter and returns the sum of the numbers from 1 to to the parameter (calculated recursively).

"""


def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


"""
Given non-negative integers x and n, x to the nth power can be defined as:
x to the 0th power is 1
x to the nth power can be obtained by multiplying x to the (n-1)th power with x
Write a function named power that accepts two parameters containing integer values (x and n, in that order) and recursively calculates and returns the value of x to the nth power.
"""


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


"""
The nth harmonic number is defined non-recursively as: 1+1/2+1/3+1/4+...+1/n. Come up with a recursive definition and use it to write a function called harmonic that accepts a parameter n that contains an integer value and returns the nth harmonic number.
"""


def harmonic(n):
    if n <= 1:
        return n
    else:
        return 1.0 / n + harmonic(n - 1)


"""
The "odd/even factorial" of a positive integer n is represented as n and is defined non-recursively as: (n)(n-2)(n-4)...(4)(2) if n is even and (n)(n-2)(n-4)...(5)(3)(1) if n is odd. For example, the odd factorial of 7 equals 7*5*3*1 or 105, and the even factorial of 6 equals 6*4*2 or 48.

Come up with a recursive definition for the odd/even factorials and use it to write a function called oddevenfact that recursively calcules that odd/even factorial value of its single parameter, which contains an integer value.

"""


def oddevenfact(n):
    if n > 2:
        return n * oddevenfact(n - 2)
    else:
        return n


"""
The Fibonacci series (0, 1, 1, 2, 3, 5, 8, 13, 21) has as its first two values 0 and 1; each successive value is then calculated as the sum of the previous two values. The first element in the series is considered the 0th element.

The nth element in the series, written as fib(n), is thus defined as:
n if n=0 or n=1
fib(n-1)+fib(n-2) otherwise
Write a function fib, that takes a single parameter, n, which contains an integer value, and recursively calculates and returns the nth element of the Fibonacci series.
"""


def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

