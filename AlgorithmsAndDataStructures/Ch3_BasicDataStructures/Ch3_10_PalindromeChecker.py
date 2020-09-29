from Ch3_BasicDataStructures.Ch3_09_Deque import Deque

def palindromeChecker(aString):

    charDeque = Deque()

    for ch in aString:
        charDeque.addFront(ch)

    stillEqual = True

    while charDeque.size() > 1 and stillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        print(first," ",last)
        if first != last:
            stillEqual = False

    return stillEqual

print(palindromeChecker("toot"))
print(palindromeChecker("pickles"))