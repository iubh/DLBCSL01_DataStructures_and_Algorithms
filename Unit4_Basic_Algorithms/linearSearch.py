def linearSearch(numList, keyValue):
    index = 0
    listLen = len(numList)
    while(index < listLen):
        if(keyValue == numList[index]):
            return index
        index += 1
    return -1

        
