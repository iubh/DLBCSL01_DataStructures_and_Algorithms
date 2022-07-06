def bubbleSort(aList): 
    seqLen = len(aList)
    swapped = True
    for lastIndex in range(seqLen-1, 0, -1):
        if not swapped:
            break
        swapped = False
        for k in range(0, lastIndex):
            if aList[k] > aList[k+1]:
                aList[k],aList[k+1]=aList[k+1],aList[k]
                swapped = True
aList = [12,3,22,44,15,13,7,45,77,33]
bubbleSort(aList)
print(aList)                
