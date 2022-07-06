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
