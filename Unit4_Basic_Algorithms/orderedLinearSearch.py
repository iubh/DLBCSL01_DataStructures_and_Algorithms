def orderedLinearSearch(numList, keyValue):
    index = 0
    stop = False
    listLen = len(numList)
    while index < listLen and not stop: 
        if(keyValue == numList[index]):
            return index
        else:
            if(numList[index] > keyValue):
                stop = True
            else:
                index+=1
    return -1

aList=[12, 15, 22, 25, 33, 47] 
print(orderedLinearSearch(aList,33))
       
