
# Project Euler: Problem 4: what is the biggest palindromic number product of 3-digit numbers?

def isPalindromic(n):
    # print("checking the number " + str(n))
    list = []
    for i in range(1,7):
        tmp = ((n)%(10**i))//(10**(i-1))
        list.append(tmp)
    list.reverse()

    digit = 0
    counter = 0
    while (digit == 0):
        digit = list[counter]
        if (digit==0):
            list.remove(list[counter])
        else:
            digit = list[counter]

    list2 = list[:] # attention, this way we clone a list and not assign another pointer to the same object!!
    list.reverse()
    if (list2 == list):
        return True
    return False


def problem4():
    result = 0
    for i in range(999,0,-1):
        for j in range(999,0,-1):
            # sprint("checking the couple " + str(i) + " and " + str(j))
            if(isPalindromic(i*j)):
                if (i*j > result):
                    result = i*j
    return result

print("Problem 4: " + str(problem4()))