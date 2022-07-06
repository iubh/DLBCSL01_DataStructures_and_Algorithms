def linearFibonacci(n):
    #Return F(n) and F(n-1)
    if (n <= 1):
        return (1,0)
    else:
        (current, prev) = linearFibonacci(n-1)
        return (current+prev, current)
    
print(linearFibonacci(6))

#Binary Recursive Fibonnaci
def fib(n):
          if(n==0):
             return 0
          elif(n==1):
             return 1
          else:
             return(fib(n-1)+fib(n-2))
print(fib(6))


