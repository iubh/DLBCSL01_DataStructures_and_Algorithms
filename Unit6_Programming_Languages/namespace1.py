x=1
def A():
    y=2
    def B():
        z=3
        print(vars())
        print(dir())
    B()
    print(vars())
    print(dir())
A()
