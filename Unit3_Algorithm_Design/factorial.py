def factorial(n):
    index = 0
    value = 1
    while(index < n):
        index += 1
        value *= index
    return value
print(factorial(6))
