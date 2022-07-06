def generateFib():
    one = 0
    other = 1
    while (1):
        yield one
        another = one + other
        one = other
        other = another

gen = generateFib()    

def getLessThan(g, n):
    i=next(g)
    while i < n:
        print(i)
        i=next(g)

getLessThan(gen, 100)
