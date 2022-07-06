from   random import randint
def typeCheck(num):
    if(num%2):
        x = 123
    else:
        x = "123"
    print(type(x))
typeCheck(randint(1,1000))
