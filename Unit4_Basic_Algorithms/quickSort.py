def partition(aList, left, right):
    pivot = aList[left]
    i=left + 1
    j=right
    while True:
        while (i <= j) and (aList[i] <= pivot):
            i+=1
        while (i <=j) and (aList[j] >= pivot):
            j-=1
        if(i <= j):
            aList[i],aList[j] = aList[j],aList[i]
        else:
            break
    aList[left],aList[j]= aList[j],aList[left]
    return j
        
def qSort(aList, left, right):
    if(left >= right):
        return
    partIndex = partition(aList, left, right)
    qSort(aList,left,partIndex-1)
    qSort(aList,partIndex+1,right)

def quickSort(aList):
    seqLen = len(aList)
    qSort(aList, 0, seqLen-1)
    
aList = [12,3,22,44,15,13,7,45,77,33]
quickSort(aList)
print(aList) 
