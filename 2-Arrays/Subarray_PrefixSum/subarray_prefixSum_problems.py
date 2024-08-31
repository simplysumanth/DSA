from typing import List


def productExceptSelf(nums: List[int]):
  """
  https://leetcode.com/problems/product-of-array-except-self/
  
  Given an integer array nums, return an array answer such that answer[i] is equal to    the product of all the elements of nums except nums[i].

  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

  You must write an algorithm that runs in O(n) time and without using the division      operation.

  Example 1:

  Input: nums = [1,2,3,4]
  Output: [24,12,8,6]
  Example 2:

  Input: nums = [-1,1,0,-3,3]
  Output: [0,0,9,0,0]
  """
  ans = [1] * len(nums)
  prefix = 1
  postfix = 1
  for i in range(len(nums)):
    prefix = prefix * nums[i - 1] if (i - 1) >= 0 else 1
    ans[i] *= prefix
  print(ans)
  for i in range(len(nums) - 1, -1, -1):
    postfix = postfix * nums[i + 1] if (i + 1) < len(nums) else 1
    ans[i] *= postfix
  print(ans)


#productExceptSelf([-1, 1, 0, -3, 3])


def leftRightDifference(nums):
  leftSum, rightSum = [], []
  currentSum = 0
  for i in range(0, len(nums)):
    if i == 0:
      currentSum += 0
    else:
      currentSum += nums[i - 1]
    leftSum.append(currentSum)

  currentSum = 0
  for i in range(len(nums) - 1, -1, -1):
    if i == len(nums) - 1:
      currentSum += 0
    else:
      currentSum += nums[i + 1]
    rightSum.append(currentSum)
  rightSum = rightSum[::-1]
  print(leftSum)
  print(rightSum)
  ans = []
  for i in range(len(nums)):
    ans.append(abs(leftSum[i] - rightSum[i]))
  return ans


def leftRightDifference_optimized(nums):
  prefix = 0
  suffix = sum(nums)
  ans = []
  for i in nums:
    prefix += i
    ans.append(abs(prefix - suffix))
    suffix -= i
  return ans


def pivotInteger(n: int) -> int:
  prefix = 0
  total = n * (n + 1) // 2
  for i in range(1, n + 1):
    prefix += i
    if (prefix == (total - prefix + i)):
      return i
  return -1


def sumOddLengthSubarrays(arr: List[int]):
  prefixSum = []
  current = 0
  for i in arr:
    current += i
    prefixSum.append(current)
  #[1,5,7,12,15]
  total = sum(arr)
  i = 0
  while (i < len(prefixSum) - 1):
    j = i
    if i + 2 <= len(prefixSum) - 1:
      total += sum(prefixSum[i:i + 3])
      print(f"i: {i} , i+2 : {i+2} ,total : {total}")
    else:
      i += 1
  return total


def subarraySum(nums: List[int], k: int):
  """
  Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
  A subarray is a contiguous non-empty sequence of elements within an array.

  Example 1:
  Input: nums = [1,1,1], k = 2
  Output: 2

  Example 2:
  Input: nums = [1,2,3], k = 3
  Output: 2

  p -> [1,2,3]
  s -> [3,2,1]

  preSum = {}
  {1:1,3:1,6:1}

  """
  res = 0
  curr = 0
  prefixMap = {0: 1}
  diff = 0

  for n in nums:
    curr += n
    diff = curr - k
    res += prefixMap.get(diff, 0)
    prefixMap[curr] = 1 + prefixMap.get(curr, 0)
  print(res)


def maxProduct(nums):
  """
  https://leetcode.com/problems/maximum-product-subarray/
  Given an integer array nums, find a subarray that has the largest product, and return the product.

  Example 1:
  Input: nums = [2,3,-2,4]
  Output: 6
  Explanation: [2,3] has the largest product 6.
  
  Example 2:
  Input: nums = [-2,0,-1]
  Output: 0
  Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

  Example 3:
  Input: nums = [1, -2, 3, 4, -4, -3]
  Output : 144
  """
  maxi = float("-inf")
  prefix = 1
  suffix = 1
  n = len(nums)
  for i in range(len(nums)):
    if prefix == 0:
      prefix = 1
    if suffix == 0:
      suffix = 1
    prefix *= nums[i]
    suffix *= nums[n - i - 1]
    maxi = max(maxi, max(prefix, suffix))
  return maxi


print(maxProduct([1, -2, 3, 4, -4, -3]))


def subarraySum(nums: List[int], k: int):
  """
  Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
  A subarray is a contiguous non-empty sequence of elements within an array.

  Example 1:
  Input: nums = [1,1,1], k = 2
  Output: 2

  Example 2:
  Input: nums = [1,2,3], k = 3
  Output: 2

  p -> [1,2,3]
  s -> [3,2,1]

  preSum = {}
  {1:1,3:1,6:1}

  """
  res = 0
  curr = 0
  prefixMap = {0: 1}
  diff = 0

  for n in nums:
    curr += n
    diff = curr - k
    res += prefixMap.get(diff, 0)
    prefixMap[curr] = 1 + prefixMap.get(curr, 0)
  print(res)


subarraySum([1, 1, 2, 3], 2)
