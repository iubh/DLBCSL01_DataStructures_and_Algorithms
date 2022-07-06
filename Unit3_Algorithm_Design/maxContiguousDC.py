def maxContiguousSubseqDC(A, low, high):
    if(low == high):
        return max(0,A[low]) #Only 1 element, if negative return 0
    mid=(low+high)//2
    
   
    #find max crossing subsequence to the left
    subseqSum = 0
    maxLeftSum = 0
    for i in range(mid,low-1,-1):
        subseqSum += A[i]
        maxLeftSum=max(maxLeftSum, subseqSum)
        
    #find max subsequence exclusively to the right 
    subseqSum = 0
    maxRightSum = 0
    for i in range(mid+1,high+1):
        subseqSum += A[i]
        maxRightSum=max(maxRightSum, subseqSum)  
        
    #find max subsequence exclusively to the left
    left = maxContiguousSubseqDC(A, low, mid)
    
    #find max subsequence exclusively to the 
    right = maxContiguousSubseqDC(A, mid+1, high)
    
    print("low, mid, high, left, right, maxLeft, maxRight", low, mid, high, left, right, maxLeftSum, maxRightSum)
    return(max(left, maxLeftSum+maxRightSum, right))
    
listA=[-6, -22, 1, 6, -5, 3, 4]
print("maxSumDC=", maxContiguousSubseqDC(listA,0,6))

