def bubbleSort(aList):

    sortedList = []
    count = 0
    for passNumber in range(len(aList)-1,0,-1):
        for i in range(passNumber):
            count += 1
            if aList[i] > aList[i+1]:
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp

    sortedList = aList

    return sortedList, count


dataSet = [10,9,8,7,6,5,4,3,2,1]
print(bubbleSort(dataSet))

dataSet = [1,8,9,7,10,4,5,6,2,3]
print(bubbleSort(dataSet))