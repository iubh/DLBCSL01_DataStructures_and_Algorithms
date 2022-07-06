def prefix(p):
    m = len(p) #size of pattern
    table = [0]*m
    i = 0
    for j in range(1,m):
        while i > 0 and p[i] != p[j]:
            i=table[i-1]
        if p[i] == p[j]:
            i+=1
        table[j]=i
    return table

def kmp(p,t):
    m = len(p) #size of pattern
    n =len(t)
    table=prefix(p)
    j=0
    for i in range(n):
        while j > 0 and p[j] != t[i]:
             j=table[j-1]
        if(p[j] == p[i]):
            j+=1
        if j == m:
            print("Match found at", i)
            return i-m+1
                
        
     
    
    
