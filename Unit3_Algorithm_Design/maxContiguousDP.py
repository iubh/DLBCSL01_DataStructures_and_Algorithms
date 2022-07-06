def maxContiguousSubseqDP(A):
    maxSum = 0
    n = len(A)
    for i in range(0,n):
        subseqSum = 0
        for j in range(i,n):
            subseqSum += A[j] #Compute Sum(i,j) from Sum(i,j-1)
            maxSum=max(maxSum, subseqSum)
    print("maxSumDP =", maxSum)          
listA=[-6, -22, 1, 6, -5, 3, 4]
maxContiguousSubseqDP(listA)    

