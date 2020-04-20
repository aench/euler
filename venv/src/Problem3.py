
# Project Euler: Problem 3: the largest divisor of 600851475143

def problem3():

    n = 600851475143
    partial = 1
    finish = False
    error = False
    division = n
    candidate = 1
    count = 1
    while (finish == False):
        print("candidate at guess " + str(count) + " is " + str(candidate))
        partial = bigDivisor(division)
        if (bigDivisor(division // partial) == division):
            print("division is likely prime!")
            error = False
            break
        if (partial == 1):
            error = True
            finish = True
        division = division // partial
        if (candidate < partial):
            candidate = partial
        count = count + 1

    if (error == True):
        print("Too difficult!")
        return 0

    return candidate

def bigDivisor(n):

    list = [2, 3, 5, 7, 11, 13, 19, 23, 29]
    listLength = 8
    for i in range(30, 100000):
        prime = True
        for j in range(0, listLength):
            # print("checking if " + str(i) + " is divisible by " + str(list[j]))
            if (i % list[j] == 0):
                # print("Not prime!")
                prime = False
                break;
        if (prime == True):
            # print(str(i) + " is prime")
            list.append(i)
            listLength = listLength + 1
    # print("The prime numbers less than 20000 are: ")
    # print(list)

    largestDivisor = 1
    for k in range(0, listLength):
        # print("checking if " + str(list[k]) + " divides " + str(n))
        if (n % list[k] == 0):
            # print(str(list[k]) + " divides " + str(n))
            largestDivisor = list[k]

    return largestDivisor

attenzione = problem3()
if (attenzione == 0):
    print("Cannot find solution to Problem 3")
else:
    print("Problem 3: " + str(attenzione))