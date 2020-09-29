"""
This file contains solutions to Pearson MyProgramming Lab
Starting Out with Python
Section 12.1 (Introduction to Recursion)
"""

"""
Write a function called printStars. The function receives a parameter containing an integer value. If the parameter is positive, the funciton prints (to standard output) the given number of asterisks. Otherwise the function does nothing. The function does not return a value. Thus, if printStars(8) is called, ******** (8 asterisks) will be printed. The function must not use a loop of any kind (for, while, do-while) to accomplish its job. Instead, it should examine its parameter, returning if the parameters value is not positive. If the parameter is positive, it:
prints a single asterisk (and no other characters)
then crecursively calls itself to print the remaining asterisks
"""


def printStars(num: int):
    if num > 0:
        print('*', end="")
        printStars(num - 1)


"""
Assume the availability of a function named printStars that can be passed a parameter containing a non-negative integer value. The function prints out the given number of asterisks.

Write a function named printTriangle that receives a parameter that holds a non-negative integer value and prints a triangle of asterisks as follows: first a line of n asterisks, followed by a line of n-1 askterisks, and then a line of n-2 asterisks, and so on.

For example, if the function received 5, it would print:
*****
****
***
**
*

The function must not use a loop of any kind (for, while, do-while) to accomplish its job. The function should invoke printStars to accom;lish the task of printing a single line.

"""


def printTriangle(n):
    if n == 0:
        return
    else:
        printStars(n)
        print()
        printTriangle(n - 1)
