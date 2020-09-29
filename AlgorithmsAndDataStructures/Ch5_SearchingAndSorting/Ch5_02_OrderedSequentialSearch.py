"""
Ordered sequential search of a list.  Complexity still O(n) worst case
However, average case is O(n/2) when item is not present versus O(n) for sequential search
"""
import random

def orderedSequentialSearch(aList, dataItem):
    pos = 0
    found = False
    stop = False

    while pos < len(aList) and not found and not stop:
        if aList[pos] == dataItem:
            found = True
        else:
            if aList[pos] > dataItem:
                stop = True
            else:
                pos += 1

    print(pos)
    return found

dataSet = []

for i in range(99):
    dataSet.append(100*random.random())
dataSet.append(58.0)
dataSet.sort()

print(orderedSequentialSearch(dataSet,58.0))
print(orderedSequentialSearch(dataSet,48.0))


