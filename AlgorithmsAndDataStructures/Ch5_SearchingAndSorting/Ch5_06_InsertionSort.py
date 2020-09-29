def insertionSort(aList):
    for index in range(1,len(aList)):
        currentValue = aList[index]
        position = index
        while position > 0 and aList[position-1] > currentValue:
            aList[position] = aList[position-1]
            position = position-1
        aList[position] = currentValue

    return aList


dataSet = [10,9,8,7,6,5,4,3,2,1]
print(insertionSort(dataSet))