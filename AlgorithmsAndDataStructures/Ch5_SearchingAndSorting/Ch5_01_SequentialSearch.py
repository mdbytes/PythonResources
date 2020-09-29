"""
Sequential search of a list.  Complexity O(n)
"""
import random

def sequentialSearch(aList, dataItem):
    pos = 0
    found = False

    while pos < len(aList) and not found:
        if aList[pos] == dataItem:
            found = True
        else:
            pos += 1

    print(pos)
    return found

dataSet = []

for i in range(99):
    dataSet.append(100*random.random())
dataSet.append(58.0)

print(sequentialSearch(dataSet,58.0))
print(sequentialSearch(dataSet,48.0))

