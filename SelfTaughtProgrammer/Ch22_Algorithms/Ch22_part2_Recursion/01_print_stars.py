"""
Write a function called printStars. The function receives a parameter containing an integer value.
If the parameter is positive, the function prints (to standard output) the given number of asterisks.
Otherwise the function does nothing. The function does not return a value.

Thus, if printStars(8) is called, ******** (8 asterisks) will be printed.

The function must not use a loop of any kind (for, while, do-while) to accomplish its job.

Instead, it should examine its parameter, returning if the parameters value is not positive.

If the parameter is positive, it:

prints a single asterisk (and no other characters)

then recursively calls itself to print the remaining asterisks
"""


def print_stars(num: int):
    if num > 0:
        print('*', end="")
        print_stars(num - 1)


def app():
    print_stars(5)


if __name__ == '__main__':
    app()
