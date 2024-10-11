import math

def printN(n):
    if n == 0:
        return
    print(n)
    return printN(n-1)

def printTillN(n):
    if n == 0:
        return n
    printTillN(n-1)
    print(n)

def factorial(n):
    if n == 0:
        return 0
    return n * factorial(n-1)

def sumOfdigits(n):
    if n == 0:
        return 0
    #Or return (n%10) + sumOfdigits(n//10) 
    return sumOfdigits(n//10) + (n%10)

def productOfdigits_1(n):
    #123
    if n//10 == 0:
        return n%10
    return  (n%10) * productOfdigits_1(n//10) 

def productOfDigits_2(n):
    #123
    if (n%10 == n):
        return n
    return (n%10) * productOfDigits_2(n//10)

total = 0
def reverseNumber_1(n):
    #Store the value outside, hence we are not returning any value
        # print(reverseNumber_1(123))
        # print(total)
    global total
    #123 -> 321
    if n == 0:
        return
    rem = n%10
    total  = total * 10 + rem
    reverseNumber_1(n//10)

def reverseNumber_2(n):
    #print(reverseNumber_2(1234))

    #get the total digits of the number
    digit = int(math.log10(n)) + 1

    return reverseNumber_2_helper(n,digit)

def reverseNumber_2_helper(n, digit):
    #1234 -> 4321
    #4 * 10^3 + 3 * 10^2 + 2 * 10^1 + 1 * 10^0 -> 4321
    
    #return number if the number is single digit
    if n%10 == n:
        return n
    
    #calculate -> rem * 10^digit-1
    rem = n%10 #stores 4, we need to get 4 * 10^3 -> 4 * 10^digit-1

    return rem * int(math.pow(10,digit-1)) + reverseNumber_2_helper(n//10,digit-1)


def palindrome(n) -> bool:
    #1221
    if n == reverseNumber_2(n):
        return True
    return False

def countZeros(n):
    return countZeros_helper(n,0)

def countZeros_helper(n,count):
    
    if n == 0:
        return count
    if n%10 == 0:
        return countZeros_helper(n//10, count+1)
    else:
        return countZeros_helper(n//10,count)

def numberOfSteps(num):
    #https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

    """
    Given an integer num, return the number of steps to reduce it to zero.

    In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
    """    
    return numberOfSteps_helper(num, 0)

def numberOfSteps_helper(num, steps):
    if num == 0:
        return steps
    if num%2 == 0:
        return numberOfSteps_helper(num//2, steps+1)
    else:
        return numberOfSteps_helper(num-1, steps+1)

print(numberOfSteps(14))