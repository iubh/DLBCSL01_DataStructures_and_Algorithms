def partition(L,p):
    i=1
    j=len(L)-1
    while True:
        while (i <= j) and (L[i] <= p):
            i+=1
        while (i <=j) and (L[j] > p):
            j-=1
        if(i <= j):
            L[i],L[j] = L[j],L[i]
        else:
            break
    return L
aList=[11,59,26,17,2,1,25,9,3,15]
partition(aList,11)
