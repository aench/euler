
# Project Euler Problem 7: what is the 10001th prime number?

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