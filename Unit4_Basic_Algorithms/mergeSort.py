def merge(A,B,C):
    a=b=0
    la, lb, lc = len(A), len(B), len(C)
    while(a+b < lc):
        if((b==lb) or ((a < la) and (A[a]<B[b]))): 
            C[a+b],a,b=A[a],a+1,b #Select from A
        else:
            C[a+b],a,b = B[b],a,b+1 #Select from B
    return C
    
def mergeSort(aList):
    seqLen = len(aList);
    if seqLen <= 1:
        return
    mid = seqLen//2
    lower = aList[:mid] #Copy lower half
    upper = aList[mid:] #Copy upper half
    mergeSort(lower) #Sort lower half
    mergeSort(upper) #Sort upper half
    aList = merge(lower,upper,aList)
    
aList = [12,3,22,44,15,13,7,45,77,33]
mergeSort(aList)
print(aList)     

bList = [3,12,15,22,44,7,13,33,45,77]
merge(bList[:5],bList[5:10],bList)
print(bList)
        
