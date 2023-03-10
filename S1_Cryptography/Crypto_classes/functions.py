# IMPORTS

##############################
# FUNCTIONS #

def gcd_euclidean(num1: int, num2: int):
    if num1 < 0 or num2 < 0:
        raise ValueError("Cannot calculate GCD of negative number!")
    if num1 == 0 and num2 == 0:
        return 0
    elif num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    
    if num2 > num1:
        num1, num2 = num2, num1
    
    # the remainder of divising both numbers is calculated and passed through recurrency
    return gcd_euclidean(num1%num2, num2)

# function for finding all prime numbers from given range based on Erathosthenes' sieve
def prime_finder(maxVal: int):
    numbers = []
    for enum in range(2, maxVal):
        numbers.append(enum)
    
    for num, it in zip(numbers, range(0, len(numbers))):
        if num == 0:
            continue
        for higherVals, it2 in zip(numbers[it+1:], range(it+1, len(numbers))):
            if higherVals % num == 0:
                numbers[it2] = 0
    
    return list(filter((0).__ne__, numbers))
    
# print(gcd_euclidean(0, 46))

print(prime_finder(200))