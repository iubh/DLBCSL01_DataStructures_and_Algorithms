n = 1
while (n <= 25):
    n += 1
    print(n)

for i in range(21,35):
    print(i)

fruitBasket=["apple","banana","mango","cherry","kiwi"]
for i in fruitBasket:
	print(i)

for i in (2,4,6,8):
           print(i)
for i in [2,4,6,8]:
           print(i)
for i in "2468":
           print(i)

for i in range(501,1000,2):
    print(i)
    if(i % 37==0):
        break

for i in range(501,1000,2):
    if(i % 37!=0):
        continue
    print(i)

alist = list(range(1,21))
i = iter(alist)         #creates iterator
while (1):
    try:
        print(next(i))  #iterates through list
    except StopIteration:
        break

def generatePrimeFactors(num):
    fact = 2
    while fact * fact <= num:
        if num % fact:
            fact += 1
        else:
            num //= fact
            yield fact
    if num > 1:
        yield num

for i in generatePrimeFactors(3000):
    print(i)
