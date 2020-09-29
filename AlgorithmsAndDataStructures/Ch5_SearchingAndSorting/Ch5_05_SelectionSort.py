def selectionSort(aList):
    for fillSlot in range(len(aList)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillSlot+1):
            if aList[location] > aList[positionOfMax]:
                positionOfMax = location

        temp = aList[fillSlot]
        aList[fillSlot] = aList[positionOfMax]
        aList[positionOfMax] = temp

    return aList

dataSet = [10,9,8,7,6,5,4,3,2,1]
print(selectionSort(dataSet))