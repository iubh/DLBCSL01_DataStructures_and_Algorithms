def maxContiguousSubseq(A):
    maxSum = 0
    n = len(A)
    for i in range(0,n):
        for j in range(i,n):
            subseqSum = 0
            for k in range(i,j+1):
                subseqSum += A[k]
                maxSum=max(maxSum, subseqSum)
    print("maxSum =", maxSum)          
listA=[-6, -22, 1, 6, -5, 3, 4]
maxContiguousSubseq(listA)
