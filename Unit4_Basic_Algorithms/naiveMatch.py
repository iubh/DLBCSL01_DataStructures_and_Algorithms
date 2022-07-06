def naiveMatch(p,t):
    if not p or not t:
        return 0
    m = len(p)
    n = len(t)
    found = False
    for i in range(n-m+1):
        j=0
        k=i
        while j < m and i < n and p[j]==t[k]:
            j+=1
            k+=1
        if j== m:
            print("Found valid shift", i, "for", p)
            found = True
    if not found:
        print("No match for",p)
                
naiveMatch('aba','cbabababaa')
naiveMatch('abc','cbabababaa')
