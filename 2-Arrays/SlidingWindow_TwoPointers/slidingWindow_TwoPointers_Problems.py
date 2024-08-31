def largestSubArrayWithSum_brute(arr, k):
  """
  Get the largest subarray <= k
  arr -> [3,2,5,1,10,7]
  k = 10

  Space : O(n^2)
  """
  #Brute Force
  maxLen = 0
  subArrays = []
  for i in range(0, len(arr) - 2):
    sum = 0
    for j in range(i, len(arr) - 1):
      sum += arr[j]
      if sum <= k:
        maxLen = max(maxLen, j - i + 1)
        subArrays.append(arr[i:j + 1])
  print(subArrays)
  return maxLen


def largestSubArrayWithSum_better(arr, k):
  """
  Get the largest subarray <= k
  arr -> [3,2,5,1,10,7]
  k = 10

  Space : O(N+N) - >O(2N)

  [3,2,5,1,10,7]
   l
   r
  """
  l = r = 0
  sum = 0
  maxLen = 0
  subArrays = []
  while (r < len(arr)):
    sum += arr[r]

    while (sum > k):
      sum -= arr[l]
      l += 1

    if sum <= k:
      maxLen = max(maxLen, r - l + 1)
      subArrays.append(arr[l:r + 1])
    r += 1
  print(subArrays)
  return maxLen


def largestSubArrayWithSum_optimal(arr, k):
  """
  Get the largest subarray <= k
  arr -> [3,2,5,1,10,7]
  k = 10

  Space : O(N)

  [3,2,5,1,10,7]
   l
   r
  """
  l = r = 0
  sum = 0
  maxLen = 0
  subArrays = []
  while (r < len(arr)):
    sum += arr[r]

    if (sum > k):
      sum -= arr[l]
      l += 1

    if sum <= k:
      maxLen = max(maxLen, r - l + 1)
      subArrays.append(arr[l:r + 1])
    r += 1
  print(subArrays)
  return maxLen


def subarraySum(nums, k) -> int:
  hashMap = {0: 1}
  sum = 0
  count = 0
  for i in nums:
    sum += 1
    if sum == k:
      count += 1
    if sum - k in hashMap:
      count += hashMap[sum - k]

    if sum in hashMap:
      hashMap[sum] += 1
    else:
      hashMap[sum] = 1

  return count


def getSmallest(a):
  a.sort()
  return a[0], a[1]


def pairWithMaxSum(arr):
  """
  https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/0

  Given an array arr[], with 0-based indexing, select any two indexes, i and j such that i < j. From the subarray arr[i...j], select the smallest and second smallest numbers and add them, you will get the score for that subarray. Return the maximum possible score across all the subarrays of array arr[].

  Input : arr[] = [4, 3, 1, 5, 6]
  Output : 11
  Explanation : Subarrays with smallest and second smallest are:- 
  [4, 3] smallest = 3,second smallest = 4
  [4, 3, 1] smallest = 1, second smallest = 3
  [4, 3, 1, 5] smallest = 1, second smallest = 3
  [4, 3, 1, 5, 6] smallest = 1, second smallest = 3
  [3, 1] smallest = 1, second smallest = 3
  [3, 1, 5] smallest = 1, second smallest = 3
  [3, 1, 5, 6] smallest = 1, second smallest = 3
  [1, 5] smallest = 1, second smallest = 5
  [1, 5, 6] smallest = 1, second smallest = 5
  [5, 6] smallest = 5, second smallest = 6
  Maximum sum among all above choices is, 5 + 6 = 11.
  """
  l = 0
  r = 1
  n = len(arr)
  maxi = -1
  # maxSum = -1
  # while(l<n-1 and r<n):
  #   smallest,secondSmallest = getSmallest(arr[l:r+1])
  #   currentSum = smallest + secondSmallest
  #   print(currentSum)
  #   maxSum = max(maxSum, currentSum)
  #   print(f"l : {l}, r : {r}")
  #   if r < n-1:
  #     r+=1
  #   else:
  #     l+=1
  for i in range(len(arr) - 1):
    curr = arr[i] + arr[i + 1]
    maxi = max(maxi, curr)
  print(maxi)


#pairWithMaxSum([228, 394, 463, 227, 388, 757, 782, 238, 967] )


def rearrangeArray(nums):
  """
  https://leetcode.com/problems/rearrange-array-elements-by-sign/

  You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

  You should return the array of nums such that the the array follows the given conditions:

  Every consecutive pair of integers have opposite signs.
  For all integers with the same sign, the order in which they were present in nums is preserved.
  The rearranged array begins with a positive integer.
  Return the modified array after rearranging the elements to satisfy the aforementioned conditions.



  Example 1:

  Input: nums = [3,1,-2,-5,2,-4]
  Output: [3,-2,1,-5,2,-4]
  Explanation:
  The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
  The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
  Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
  Example 2:

  Input: nums = [-1,1]
  Output: [1,-1]
  Explanation:
  1 is the only positive integer and -1 the only negative integer in nums.
  So nums is rearranged to [1,-1].

  """
  p = []
  n = []
  res = []
  for i in nums:
    if i < 0:
      n.append(i)
    else:
      p.append(i)

  for i in range(len(p)):
    res.append(p[i])
    res.append(n[i])
  print(res)


def maxArea(height):
  """
  https://leetcode.com/problems/container-with-most-water/description/

  Input: height = [1,8,6,2,5,4,8,3,7]
  Output: 49
  Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
  """
  l = 0
  r = len(height) - 1
  maxArea = float("-inf")
  while (l < r):
    currArea = min(height[l], height[r]) * (r - l)
    maxArea = max(maxArea, currArea)
    if height[l] < height[r]:
      l += 1
    else:
      r -= 1
  return maxArea


def printClosest(arr, brr, n, m, x):
  """
  https://www.geeksforgeeks.org/problems/find-the-closest-pair-from-two-arrays4215/1

  Given two sorted arrays arr and brr and a number x, find the pair whose sum is closest to x and the pair has an element from each array. In the case of multiple closest pairs return any one of them

  Input : N = 4, M = 4
  arr[ ] = {1, 4, 5, 7}
  brr[ ] = {10, 20, 30, 40} 
  X = 32
  Output : 
  1, 30
  Explanation:
  The closest pair whose sum is closest
  to 32 is {1, 30} = 31.
  
  """

  l, r = 0, m - 1
  minSum = float("inf")
  minPairs = []

  while (l < n and r >= 0):
    currSum = (arr[l] + brr[r]) - x
    if abs(currSum) < minSum:
      minSum = abs(currSum)
      minPairs = [arr[l], brr[r]]
    print(f"l : {l}, r : {r}")
    print(f"currSum : {currSum}, minSum : {minSum}, minPairs : {minPairs} ")
    if currSum < 0:
      l += 1
    elif currSum > 0:
      r -= 1
    else:
      break
  return minPairs


def sumClosest(arr, k):
  """
  https://www.geeksforgeeks.org/problems/pair-in-array-whose-sum-is-closest-to-x1124/1

  Given a sorted array arr[]  and a number k, find a pair in sorted order in an array whose sum is closest to k.
  Note: If there are multiple such pairs return the pair with maximum absolute difference.

  Input: arr[] = [10, 22, 28, 29, 30, 40], k = 54
  Output: [22, 30]
  Explanation: As 22 + 30 = 52 is closest to 54.
  """
  # code here
  l = 0
  r = len(arr) - 1
  minDiff = float("inf")
  minPairs = []
  while (l < r):
    currSum = arr[l] + arr[r]
    absDiff = abs(currSum - k)
    if absDiff < minDiff:
      minDiff = absDiff
      minPairs = [arr[l], arr[r]]
    if currSum < k:
      l += 1
    elif currSum > k:
      r -= 1
    else:
      break
  return minPairs

def findTriplets(arr, n):
  """
  https://www.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1

  Given an array arr[] of n integers. Check whether it contains a triplet that sums up to zero. Return true, if there is at least one triplet following the condition else return false.

  Input: n = 5, arr[] = {0, -1, 2, -3, 1}
  Output: 1
  Explanation: 0, -1, and 1 form a triplet with a sum equal to 0.
  
  Input: n = 3, arr[] = {1, 2, 3}
  Output: 0
  Explanation: No triplet with zero sum exists. 

  Time Complexity : O(n^2) ; Space : O(1)
  """
  if len(arr) < 3:
    return False
  #sort the array -> nLogn
  arr.sort()
  
  for i in range(len(arr)):
    l,r = i+1,n-1
    while(l<r):
      currSum = arr[i] + arr[l] + arr[r] 
      if currSum == 0:
        return True
      elif currSum < 0:
        l+=1
      else:
        r-=1
  return False

print(findTriplets([97, -27, 2, -34, 61, -39], 6))
    
    
  
  
