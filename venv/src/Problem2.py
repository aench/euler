
# Project Euler: Problem 2: the sum of the even terms of the Fibonacci's series less than 4 millions

def problem2():
    term = 0
    el1 = 0
    el2 = 1
    result = 0
    for count in range(1,33):
        # print("el1 = " + str(el1) + " el2 = " + str(el2))
        term = el1 + el2
        if (term % 2 == 0):
            result = result + term
            # print("sum: " + str(sum))
        el1 = el2
        el2 = term
        # print("term: " + str(term))
    return result

print("Problem 2: " + str(problem2()))
