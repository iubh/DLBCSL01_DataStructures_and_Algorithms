alist = list(range(1,21))
i = iter(alist)         #creates iterator
while (1):
    try:
        print(next(i))  #iterates through list
    except StopIteration:
        break
