from memory_profiler import profile

@ profile

def profileAnalysis():
    a = [0] * (10**7)
    b = a.copy()
    c = a[:]
    del c
    del b
    return a

if __name__ == '__main__':
    profileAnalysis()
    
