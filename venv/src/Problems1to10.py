# Project Euler: Problem 1
def problem1():
    n = 999//5
    multiples5 = 5*(n*(n+1)//2)
    k = 999//3
    multiples3 = 3*(k*(k+1)//2)
    j = 999//15
    multiples15 = 15*(j*(j+1)//2)
    totale = multiples5+multiples3-multiples15
    # print("totale:")
    # print(totale)
    return totale

print("Problem 1: " + str(problem1()))

# Project Euler: Problem 2
def problem2():
    term = 0
    el1 = 0
    el2 = 1
    sum = 0
    for count in range(1,33):
        # print("el1 = " + str(el1) + " el2 = " + str(el2))
        term = el1 + el2
        if (term % 2 == 0):
            sum = sum + term
            # print("sum: " + str(sum))
        el1 = el2
        el2 = term
        print("term: " + str(term))
    return sum

print("Problem 2: " + str(problem2()))