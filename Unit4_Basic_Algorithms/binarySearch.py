def binarySearch(numList, keyValue):
    left = 0
    right = len(numList) - 1
    found = -1
    while left <= right:
        mid = (left + right) // 2
        if numList[mid] == keyValue:
            found = mid
            break
        else:
            if keyValue < numList[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return found   

aList = [-17, -1, 12, 13, 27, 45, 57, 82]
print(binarySearch(aList, 13))
print(binarySearch(aList,28))

        
