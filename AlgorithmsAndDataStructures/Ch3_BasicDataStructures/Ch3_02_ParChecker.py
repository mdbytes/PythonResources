from Ch3_BasicDataStructures.Ch3_01_Stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        elif symbol == ")":
            if s.isEmpty():
                balanced = False
            else: 
                s.pop()
        index = index + 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False
    
expressionOne = "(8+4)*(5+6)"
expressionTwo = "(8+4))*(5+6)"

print(parChecker(expressionOne))
print(parChecker(expressionTwo))




