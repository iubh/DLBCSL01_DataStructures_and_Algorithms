def testMax(num1, num2, num3):
    if(num1 > num2):
        maxNum = num1
    else:
        maxNum = num2
    if(num3 > maxNum):
        maxNum = num3
    return maxNum
