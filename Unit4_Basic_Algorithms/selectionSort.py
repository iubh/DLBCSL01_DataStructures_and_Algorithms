def selectionSort(aList):
    seqLen = len(aList)
    for lastIndex in range(seqLen-1, 0, -1):
        maxIndex =0
        for k in range(1, lastIndex + 1):
            if aList[k] > aList[maxIndex]:
                maxIndex = k
        aList[lastIndex], aList[maxIndex] \
            = aList[maxIndex],aList[lastIndex] 
aList = [12,3,22,44,15,13,7,45,77,33]
selectionSort(aList)
print(aList)     
