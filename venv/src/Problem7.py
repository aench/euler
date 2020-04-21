
# Project Euler Problem 6: the sum of square of the first ten natural numbers is, 385, the square of the sum is 3025
# then the difference is 3025-385=2640. Compute the difference of the square of the sum and sum of squares of numbers
# from 1 to 100

def isDivisibleby(n,a):
    if (n % a == 0):
        return True
    return False

def nextPrime(primes):
    n = primes[len(primes)-1]
    count = 0
    candidate = n
    found = False
    while (found == False):
        candidate = candidate + 1
        count = 0
        for j in primes:
            # print("Checking if " + str(candidate) + " is divisible by " + str(j))
            if (isDivisibleby(candidate, j)):
                # print(str(candidate) + " is divisible by " + str(j))
                count = 0
                break;
            else:
                count = count + 1
        if (count == len(primes)):
            primes.append(candidate)
            found = True


primes = [2]
for i in range(1,10001):
    nextPrime(primes)
#print(primes)
print(primes[len(primes)-1])