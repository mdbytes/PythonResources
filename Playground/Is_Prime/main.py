"""
A prime number (or a prime) is a natural number greater than 1 
that is not a product of two smaller natural numbers. 

define a function is_prime which will determine if a number is prime
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2,n):
            if n%x == 0:
                return False
        return True

def test():
    nums = [1,2,4,11,13,7,20,21]
    for num in nums:
        print(is_prime(num))


test()
