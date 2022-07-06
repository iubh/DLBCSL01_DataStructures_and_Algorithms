L=[11,59,26,17,2,1,25,9,3,15]
pivot = 11
i=0
j=len(L)-1
while True:
    while (i <= j) and (L[i] <= pivot):
        i+=1
    while (i <=j) and (L[j] > pivot):
        j-=1
    if(i <= j):
        L[i],L[j] = L[j],L[i]
    else:
        break
print(L)

