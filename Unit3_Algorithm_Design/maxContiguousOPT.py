def maxContiguousSubseqOpt(A):
    maxSum = 0
    subseqSum = 0
    n = len(A)
    for i in range(0,n):
            subseqSum = max(subseqSum+ A[i], 0)
            maxSum=max(maxSum, subseqSum)
    print("maxSumOpt =", maxSum)          
listA=[-6, -22, 1, 6, -5, 3, 4]
maxContiguousSubseqOpt(listA)   
