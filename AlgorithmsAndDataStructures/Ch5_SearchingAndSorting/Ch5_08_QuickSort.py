
def quickSortHelper(aList, first, last):
    if first < last:
        splitPoint = partition(aList,first,last)

        quickSortHelper(aList,first,splitPoint-1)
        quickSortHelper(aList,splitPoint+1,last)

def partition(aList,first,last):
    pivotValue = aList[first]

    leftMark = first + 1
    rightMark = last

    done = False
    while not done:

        while leftMark <= rightMark and aList[leftMark] <= pivotValue:
            leftMark = leftMark + 1

        while aList[rightMark] >= pivotValue and rightMark >= leftMark:
            rightMark = rightMark - 1

        if rightMark < leftMark:
            done = True

        else:
            temp = aList[leftMark]
            aList[leftMark] = aList[rightMark]
            aList[rightMark] = temp

    temp = aList[first]
    aList[first] = aList[rightMark]
    aList[rightMark] = temp

    return rightMark

def quickSort(aList):
    quickSortHelper(aList,0,len(aList)-1)


dataSet = [10,9,8,7,6,5,4,3,2,1]
print(quickSort(dataSet))

