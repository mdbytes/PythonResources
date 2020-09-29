# -*- coding: utf-8 -*-

class Fraction: 
    
    numerator:int
    denominator:int
    
    def __init__(self, num: int, den: int):
        
        if not (isinstance(num, int) and isinstance(den,int)):
            raise TypeError("Invalid input: numerator and denominator must be integers")
        
        m = num
        n = den
        
        while m % n != 0:
            m_old = m
            n_old = n
            m = n_old
            n = m_old % n_old
        
        commonDen = n
        
        self.numerator = int(num / commonDen)
        self.denominator = int(den / commonDen)

    
    def getNum(self):
        return self.numerator
    
    def getDen(self):
        return self.denominator
    
    def __add__(self, of):
        newnum = self.numerator*of.denominator + self.denominator*of.numerator
        newden = self.denominator*of.denominator
        return Fraction(newnum,newden)
    
    def __eq__(self, other):
        
        firstnum = self.numerator * other.denominator
        secondnum = self.denominator * other.numerator
        
        return firstnum == secondnum
    
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    
    
my_fraction = Fraction(3,5)

print(my_fraction)

print("I ate ",my_fraction," of the pizza")

fraction_one = Fraction(1,4)
fraction_two = Fraction(1,2)
fraction_three = fraction_one + fraction_two
fraction_four = Fraction(2,8)

print(f"Fraction One: {fraction_one}")
print(f"Fraction Two: {fraction_two}")

print(f"Fraction one plus Fraction Two: {fraction_three}")

print(f"Fraction(2,4) : {fraction_four}")
