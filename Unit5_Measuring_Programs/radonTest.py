aList = [23,34,2,13,11,-1,33,-44]
def linSearch(numList, keyValue):
    index = 0
    while(index < len(numList)):
        if(keyValue == numList[index]):
            return index
        index += 1
    return -1
def typeCheck(num):
    if(num%2):
        x = 123
    else:
        x = "123"
print(type(x)) 
def testMax(num1, num2, num3):
    if(num1 > num2):
        maxNum = num1
    else:
        maxNum = num2
    if(num3 > maxNum):
        maxNum = num3
    return maxNum
