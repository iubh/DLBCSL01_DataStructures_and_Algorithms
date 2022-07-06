def insertionSort(aList):
    seqLen = len(aList)
    for index in range(1, seqLen):
        toInsert = aList[index]
        j = index
        while j > 0:
            if(toInsert >= aList[j-1]):
                break
            aList[j] = aList[j-1]
            j -= 1
        aList[j] = toInsert
        
aList = [12,3,22,44,15,13,7,45,77,33]
insertionSort(aList)
print(aList)
