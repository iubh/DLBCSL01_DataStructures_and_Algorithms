def orderedLinearSearch(numList, keyValue):
    index = 0
    success = False
    stop = False
    listLen = len(numList)
    while index < listLen and not success and not stop: 
        if(keyValue == numList[index]):
            success = True
        else:
            if(numList[index] > keyValue):
                stop = True
            else:
                index+=1
    return success

aList=[12, 15, 22, 25, 33, 47] 
if(orderedLinearSearch(aList,33)):
    print("found")
else:
    print("not found")
       
