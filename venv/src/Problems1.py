
# Project Euler: Problem 1: the sum of the multiples of 3 or 5 less than 1000

def problem1():
    n = 999//5
    multiples5 = 5*(n*(n+1)//2)
    k = 999//3
    multiples3 = 3*(k*(k+1)//2)
    j = 999//15
    multiples15 = 15*(j*(j+1)//2)
    result = multiples5+multiples3-multiples15
    # print("totale:")
    # print(totale)
    return result

print("Problem 1: " + str(problem1()))

