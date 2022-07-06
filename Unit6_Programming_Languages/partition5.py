from kanren import run, eq, membero, var, conde
from kanren.arith import lt,gt

x =var()
L=[11,59,26,17,2,1,25,9,3,15]
pivot = 11
a=run(0,x,(membero, x, L),(lt,x,pivot))
b=run(0,x,(membero, x, L),(eq,x,pivot))
c=run(0,x,(membero, x, L),(gt,x,pivot))
d=run(0,x,(membero,x,a+b+c))
print(d)
