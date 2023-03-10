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
    
print(gcd_euclidean(0, 46))