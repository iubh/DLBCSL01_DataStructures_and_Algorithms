def linearFibonacci(n):
    #Return F(n) and F(n-1)
    if (n <= 1):
        return (1,0)
    else:
        (current, prev) = linearFibonacci(n-1)
        return (current+prev, current)
    
print(linearFibonacci(6))
