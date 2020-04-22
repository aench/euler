
# Project Euler Problem 10: find the sum of the prime less than 2 millions

def primesLess(n):
    a = [True] * n
    c = int(n ** 0.5) + 1

    for i in range(2, c):
        for j in range(i * i, n, i):
            a[j] = False

    b = [x for x in range(2, n) if a[x]]

    return b

n = int(input("Enter n: ")) + 1

a = [True] * n
c = int(n ** 0.5) + 1
primes = primesLess(c)

for i in primes:
    for j in range (i*i, n, i):
        a[j] = False

b = [x for x in range(2,n) if a[x]]

print("The Solution to Problem 10 is: " + str(sum(b)))
