first = eval(input('Enter first positive integer:'))
second = eval(input('Enter second positive integer:'))
answer = 1
divisor = 2
while ((divisor <= first) and (divisor <= second)):
    if(((first % divisor)==0) and ((second % divisor)==0)):
        answer = divisor
    divisor += 1
print(answer)
