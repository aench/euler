
# Project Euler Problem 6: the sum of square of the first ten natural numbers is, 385, the square of the sum is 3025
# then the difference is 3025-385=2640. Compute the difference of the square of the sum and sum of squares of numbers
# from 1 to 100

def sumOfSquares(n):

    list = [3]
    for i in range(1,n-1):
        list.append(3+2*i)

    result = n
    for k in range(0,n-1):
        result = result + list[k]*(n-k-1)

    return result


def sumOfNumbers(n):
    return (n*(n+1))//2


print("Solution of Problem 6: " + str(((sumOfNumbers(100))**2)-sumOfSquares(100)))

