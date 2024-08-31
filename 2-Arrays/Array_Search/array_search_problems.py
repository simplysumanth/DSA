def findCommonElements(a, b, c):
    """
  https://www.geeksforgeeks.org/problems/common-elements1132/1
  """
    """
  Let's take 1 pointer for each array (i,j,k)
  i,j,k=0,0,0
  l = []
  while(i<len(a) and j<len(b) and k<len(c)):
    if a[i] == b[j] == c[k] : 
      l.append(a[i])
      i,j,k = i+1,j+1,k+1
    elif (a[i] < b[j]) and (a[i] < c[k]) : i++
    elif (b[j] < a[i]) and (b[j] < c[k]) : j++
    else: k++
  return l
  """
    #Init 3 pointers to 0
    i, j, k = 0, 0, 0
    #get the len of each array
    n1, n2, n3 = len(a), len(b), len(c)
    #To avoid duplicated, let check for prev common value, so init it to -inf
    p = float("-inf")
    ans = []
    while (i < n1 and j < n2 and k < n3):
        ###check if the common element exists and is not equal to previous common ele
        if a[i] == b[j] == c[k] and a[i] != p:
            ans.append(a[i])
            #This will be the prev common ele in next iter
            p = a[i]
            i += 1
            j += 1
            k += 1

        elif min(a[i], b[j], c[k]) == a[i]:
            i += 1
        elif min(a[i], b[j], c[k]) == b[j]:
            j += 1
        elif min(a[i], b[j], c[k]) == c[k]:
            k += 1
    return ans

def intersection(a, b):
    a.sort()
    b.sort()
    i, j = 0, 0
    n, m = len(a), len(b)
    p = -1
    ans = []
    while (i < n and j < m):
        if a[i] == b[j]:
            if a[i] != p:
                ans.append(a[i])
                p = a[i]
            i += 1
            j += 1

        elif a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
    return ans


def majorityElement_linearSearch(A, N):
    """
    https://www.geeksforgeeks.org/problems/majority-element-1587115620/1
    
    Given an array A of N elements. Find the majority element in the array. A majority     element in an array A of size N is an element that appears strictly more than N/2     times in the array.

    Input:
        N = 3 
        A[] = {1,2,3} 
    Output:
        -1

    Input:
        N = 5 
        A[] = {3,1,3,3,2} 
    Output:
        3
    """
    d = {}
    for i in A:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in d:
        if d[i] > N // 2:
            return i
    return -1


def majorityElement_MooresVoting(A, N):
    """
    https://www.geeksforgeeks.org/problems/majority-element-1587115620/1

    Given an array A of N elements. Find the majority element in the array. A majority     element in an array A of size N is an element that appears strictly more than N/2     times in the array.

    Input:
        N = 3 
        A[] = {1,2,3} 
    Output:
        -1

    Input:
        N = 5 
        A[] = {3,1,3,3,2} 
    Output:
        3
    """
    """
    Moore's Voting Algorithm:
    1. count = 0, ele = A[0]
    2. Loop thru the array and check if i == ele :
        1. If Yes, increase count
        2. Else, descrease count
    3. If count == 0, it means count(ele) - count(others) = 0, so in that subArray             ele can't be > N/2, it can be <= N/2. So, assign ele to i
    """
    count = 0
    ele = A[0]
    for i in A:
        if count == 0:
            ele = i
        if i == ele:
            count += 1
        else:
            count -= 1

    count = 0
    for i in A:
        if i == ele:
            count += 1
    return (ele if count > N // 2 else -1)


def leaders(n, a):
    """
    https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1

    Given an array arr of n positive integers, your task is to find all the leaders         in the array. 
    1.An element of the array is considered a leader if it is greater than all the            elements on its right side (or) 
    2. if it is equal to the maximum element on its right side. The rightmost element         is always a leader.

    Input: n = 6, arr[] = {16,17,4,3,5,2}
    Output: 17 5 2

    Input: n = 5, arr[] = {10,4,2,4,1}
    Output: 10 4 4 1

    Input: n = 4, arr[] = {5, 10, 20, 40} 
    Output: 40

    Input: n = 4, arr[] = {30, 10, 10, 5} 
    Output: 30 10 10 5
    """
    #Code here
    maxi = a[n - 1]
    ans = []
    for i in range(n - 1, -1, -1):
        if (a[i] >= maxi):
            maxi = a[i]
            ans.append(maxi)
    ans.reverse()
    return ans


def findEquilibrium(a):
    """
    https://www.geeksforgeeks.org/equilibrium-index-of-an-array/?ref=roadmap

    Given an array arr[] of size n, return an equilibrium index (if any) or -1 if no      equilibrium index exists. The equilibrium index of an array is an index such that     the sum of elements at lower indexes equals the sum of elements at higher indexes.

    Input: arr[] = {-7, 1, 5, 2, -4, 3, 0}
    Output: 4
    Explanation: In 1-based indexing, 4 is an equilibrium index, because: arr[1] +                     arr[2] + arr[3] = arr[5] + arr[6] + arr[7]

    Input: arr[] = {1, 2, 3}
    Output: -1
    Explanation: There is no equilibrium index in the array.
    """
    prefix, suffix = [], []
    total = 0
    for i in a:
        total += i
        prefix.append(total)
    print(prefix)
    total = 0
    for i in range(len(a) - 1, -1, -1):
        total += a[i]
        suffix.append(total)
    suffix.reverse()
    print(suffix)

    for i in range(len(a)):
        if prefix[i] == suffix[i]:
            return i
    return -1


def majorityElement2(nums):
    """
    https://leetcode.com/problems/majority-element-ii/
    """
    count1, count2 = 0, 0
    element1, element2 = float("-inf"), float("-inf")

    for i in nums:
        if count1 == 0 and i != element2:
            element1 = i
            count1 = 1
        elif count2 == 0 and i != element1:
            element2 = i
            count2 = 1

        elif i == element1:
            count1 += 1
        elif i == element2:
            count2 += 1

        else:
            count1 -= 1
            count2 -= 1

    count1, count2 = 0, 0
    for i in nums:
        if i == element1:
            count1 += 1
        elif i == element2:
            count2 += 1

    res = []
    mini = len(nums) // 3 + 1
    if count1 >= mini:
        res.append(element1)
    if count2 >= mini:
        res.append(element2)

    return res