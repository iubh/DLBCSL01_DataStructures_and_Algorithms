def powersOfFactor(num, fact):
    if(num == fact):
        return 1
    elif num % fact == 0:
        return(powersOfFactor(num//fact,fact) + 1)
    return 0

        






