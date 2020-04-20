
# Project Euler Problem 5: 2510 is the smallest number divisible by all the numbers form 1 to 10.
# What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

def isDivisible(n,a):
    if (n % a == 0):
        return True
    return False

primes = [16,9,5,7,11,13,17,19]

print("Solution: " + str(16*9*5*7*11*13*17*19))

# If we want to generalize the procedure (for numbers not too big):

divisors = []
n = int(input("Find the least common multiple of all the numbers from 1 to: "))
primes = [2,3,5,7,11,13,17,19,23,29]
for k in primes:
    count = 0
    while (k**count < n):
        count = count + 1
    divisors.append(k**(count-1))
print("Divisors : " + str(divisors))
result = 1
for j in divisors:
    result = result * j
print("Solution: " + str(result))