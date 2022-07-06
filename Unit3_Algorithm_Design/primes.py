def primeFactors (num, fact):
    if num < fact*fact:
        return [num]
    if num % fact == 0:
        return [fact] + primeFactors (num // fact, 2)
    return primeFactors (num, fact + 1)
print(primeFactors(3000,2))


