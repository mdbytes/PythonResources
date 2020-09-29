"""
Binary search of an ordered list.  Complexity O(log n)
Notice for the example: 2 - 7 iterations
"""
import random

def binarySearch(aList, dataItem, iterations):
    if len(aList) == 0:
        return (False, iterations)
    else:
        midPoint = len(aList)//2
        if aList[midPoint] == dataItem:
            return (True, iterations)
        else:
            iterations += 1
            if dataItem < aList[midPoint]:
                return binarySearch(aList[0:midPoint],dataItem, iterations)
            else:
                return binarySearch(aList[midPoint:len(aList)-1], dataItem, iterations)


dataSet = []

for i in range(99):
    dataSet.append(100*random.random())
dataSet.append(58.0)
dataSet.sort()

print(binarySearch(dataSet,58.0, 0))
print(binarySearch(dataSet,55.0, 0))

