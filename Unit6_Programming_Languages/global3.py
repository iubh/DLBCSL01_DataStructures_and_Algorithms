x=1
print("Global1", x)
def A():
    x=2
    print("A1",x)
    def B():
        x=3
        print("B", x)
    B()
    print("A2",x)
A()
print("Global2", x)
