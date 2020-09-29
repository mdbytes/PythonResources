
from Ch3_BasicDataStructures.Ch3_01_Stack import Stack

def divideByBase(decimalNumber, base):
    hex_digits = "0123456789ABCDEF"
    bin_digits = "01"
    remainderStack = Stack()
    while decimalNumber > 0:
        remainder = decimalNumber % base
        remainderStack.push(remainder)
        decimalNumber = decimalNumber // base

    binString = ""
    if base == 2:
        while not remainderStack.isEmpty():
            binString = binString + bin_digits[remainderStack.pop()]
    elif base == 16:
        while not remainderStack.isEmpty():
            binString = binString + hex_digits[remainderStack.pop()]
    return binString


print(divideByBase(50, 2))
print(divideByBase(100, 2))
print(divideByBase(150, 2))
print(divideByBase(200, 2))
print(divideByBase(1000, 2))


print(divideByBase(50, 16))
print(divideByBase(100, 16))
print(divideByBase(150, 16))
print(divideByBase(200, 16))
print(divideByBase(1000, 16))

