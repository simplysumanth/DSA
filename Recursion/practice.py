def reverseString(s):
    #your code goes here
    start, end = 0, len(s)-1
    while(start<end):
        s[start], s[end] = s[end],s[start]
        start+=1
        end-=1
    return s

def reverseString_recursive(s,start,end):
    if start > end:
        return s
    s[start], s[end] = s[end],s[start]
    return reverseString_recursive(s, start+1, end-1)

def checkPrime(num, div):
    if div == num:
        return True
    if num % div == 0:
        return False
    return checkPrime(num, div+1)
    

def addDigits(num):
        if num == 0:
            return 0
        rem = num%10
        return rem + addDigits(num//10) 

def addDigitsOfSum(num):
    """
    print(addDigitsOfSum(1234))

    https://takeuforward.org/plus/data-structures-and-algorithm/beginner-problems/basic-recursion/sum-of-digits-in-a-given-number
    """
    if num < 10:
        return num
    total = addDigits(num)
    return addDigitsOfSum(total)

def findMinMax_helper(nums,index, mini, maxi):
    if index == len(nums):
        return mini, maxi
    if nums[index] < mini:
        mini = nums[index]
    if nums[index] > maxi:
        maxi = nums[index]
    return findMinMax_helper(nums, index+1, mini, maxi)

def findMinMax(nums):
    """
    Input -> [-3,-6,2,1,0]
    min = -6, max = 2
    """
    mini = float("inf")
    maxi = float("-inf")
    return findMinMax_helper(nums,0, mini, maxi)

def findMin_Better(nums, index):
    """
    print(findMin_Better([-3,-6,2,1,0], 5))
    """
    if index == 1:
        return nums[0]
    return min(nums[index-1], findMin_Better(nums, index- 1))

def pow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return x * pow(x, n-1)

print(pow(2,10))

    



