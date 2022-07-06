y=1
def A():
    global y
    y=2
    print("A", y)
A()
print("Global", y)
