
# Project Euler Problem 9: find the Pythagorean triplet for which a+b+c=1000

import math

squares = []
result = 0
for i in range(1,500):
    squares.append(i**2)
print(squares)
sol1 = 0
sol2 = 0
sol3 = 0
break2 = False
break3 = False
for j in squares:
    for k in squares:
        for l in squares:
            a = int(math.sqrt(l))
            b = int(math.sqrt(k))
            c = int(math.sqrt(j))
            if ((l == k + j) and (a+b+c == 1000)):
                sol1=a
                sol2=b
                sol3=c
                print(str(a) + "^2 = " + str(b) + "^2+" + str(c) + "^2")
                break2 = True
                break3 = True
                break
        if (break2 == True):
            break
    if (break3 == True):
        break


print("The solution is " + str(sol1*sol2*sol3))