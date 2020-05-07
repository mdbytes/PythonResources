print("Challenge #1")

def challenge_one():
    """
    Returns a number squared
    Accepts integer from user
    """
    a = int(input("Enter a number: "))
    b = a**2
    print("That number squared is " + str(b))

challenge_one()

print("\nChallenge #2")

def challenge_two(x):
    """
    Prints a string
    :param x: str
    :return: str
    """
    print(x)

challenge_two(input("Enter a string: "))

print("\nChallenge #3")

def challenge_three(a,b,c,d=0,e=0):
    """
    Returns a + b + c + d + e
    :param a: int
    :param b: int
    :param c: int
    :param d: int
    :param e: int
    :return: int
    """
    return a + b + c + d + e

print("Here is the answer for challenge_three(1,1,1): " + str(challenge_three(1,1,1)))
print("Here is the answer for challenge_three(1,1,1,1,1): " + str(challenge_three(1,1,1,1,1)))

print("\nChallenge #4")

def divide_by_two(x):
    """
    Returns half of a number
    :param x: int
    :return: float
    """
    return x/2

def multiply_by_four(y):
    return y*4

def main():
    a = int(input("Enter an integer: "))
    b = divide_by_two(a)
    c = multiply_by_four(b)
    print("That number divided by two and multiplied by four is: " + str(c))

main()

print("\nChallenge #5")

def convert_to_float(x):
    try:
        a = float(x)
        return a
    except (ValueError):
        print("Oops.  Couldn't convert that string to float.  Try again")
        return None

convert_to_float(input("Enter a string to convert to float: "))
