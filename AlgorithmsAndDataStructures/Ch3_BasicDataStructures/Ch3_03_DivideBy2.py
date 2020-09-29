
from Ch3_BasicDataStructures.Ch3_01_Stack import Stack

def divideBy2(decimalNumber):
    remainderStack = Stack()
    while decimalNumber > 0:
        remainder = decimalNumber % 2
        remainderStack.push(remainder)
        decimalNumber = decimalNumber // 2

    binString = ""
    while not remainderStack.isEmpty():
        binString = binString + str(remainderStack.pop())

    return binString


print(divideBy2(2))
print(divideBy2(5))
print(divideBy2(16))
print(divideBy2(17))
print(divideBy2(255))
