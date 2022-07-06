from memory_profiler import profile

@ profile

@profile
def profileAnalysis():
    a=[]
    b=[]
    for i in range(0,10**5):
        a.append(0)
        b.append(0)
    c = a.copy()
    d = a[:]
    del d
    del c
    del b
    return a


if __name__ == '__main__':
    profileAnalysis()
    
