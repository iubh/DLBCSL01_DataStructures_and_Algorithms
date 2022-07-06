aList = [23,34,2,13,11,-1,33,-44]
def linSearch(numList, keyValue):
    """Search for keyValue in numList.
    Args:
        numList: a list of values
    
        keyValue: a value being searched for in numList.
    Returns:
        index of keyValue in numList if found.
        -1 otherwise.
    """
    index = 0
    while(index < len(numList)):
        if(keyValue == numList[index]):
            return index
        index += 1
    return -1
     
print(linSearch(aList,11))
help(linSearch)

a= 123
b = [a, 456]
c = {'rst': a}
print(a)

from   random import randint
def typeCheck(num):
    if(num%2):
        x = 123
    else:
        x = "123"
    print(type(x))
typeCheck(randint(1,1000))

def testMax(num1, num2, num3):
    if(num1 > num2):
        maxNum = num1
    else:
        maxNum = num2
    if(num3 > maxNum):
        maxNum = num3
        return maxNum
        
from radon.visitors import ComplexityVisitor
v = ComplexityVisitor.from_code('''
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

''')
print(v.functions)

from radon.complexity import cc_rank
print(cc_rank(5), cc_rank(8), cc_rank(13), \
      cc_rank(26), cc_rank(36), cc_rank(45))

alist=[]
pi=3.14
for index in range(0,20):
    alist.append(2*pi*index)
  
print(alist)

alist=[]
pi=3.14
twoPi=2*3.14
for index in range(0,20):
    alist.append(twoPi*index)
    
print(alist)
    
a=2
b=3
y=3**a + 3**a*b
print(y)

y=3**a*(1+b)
print(y)

flag=True
if flag:
    a += 1
else:
    b+=1
    