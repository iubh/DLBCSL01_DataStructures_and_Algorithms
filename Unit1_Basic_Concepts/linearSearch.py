aList = [23,34,2,13,11,-1,33,-44]
def linSearch(numList, keyValue):
    index = 0
    while(index < len(numList)):
        if(keyValue == numList[index]):
            return index
        index += 1
    return -1
        
print(linSearch(aList,11))
