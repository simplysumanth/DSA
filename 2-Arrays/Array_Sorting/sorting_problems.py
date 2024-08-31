from typing import List
def waveSort_better(a, n):
  """
  Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place). In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
  If there are multiple solutions, find the lexicographically smallest one.

  Input: n = 5, arr[] = {1,2,3,4,5}
  Output: 2 1 4 3 5
  Explanation: Array elements after sorting it in the waveform are 2 1 4 3 5.
  
  Input: n = 6, arr[] = {2,4,7,8,9,10}
  Output: 4 2 8 7 10 9
  Explanation: Array elements after sorting it in the waveform are 4 2 8 7 10 9.

  Time Complexity : O(N*LogN) -> for unsorted array
  """
  for i in range(0, n - 1, 2):
    temp = a[i]
    a[i] = a[i + 1]
    a[i + 1] = temp
  print(a)


def waveSort_optimal(a, n):
  #Here for i, we are checking and swapping both i-1 and i+1,
  #hence loop starts from 1 to n-1.
  for i in range(1, n - 1, 2):
    #Check if the element before is smaller -> swap
    if i > 0 and a[i] > a[i - 1]:
      a[i], a[i - 1] = a[i - 1], a[i]

    #check if next elemt is bigger
    if i <= n - 2 and a[i] < a[i + 1]:
      a[i], a[i + 1] = a[i + 1], a[i]
  print(a)


def minAdjacentSwaps(nums):
  """
  https://www.geeksforgeeks.org/minimum-swaps-required-sort-binary-array/?ref=roadmap

  Given a binary array, task is to sort this binary array using minimum swaps. We are   allowed to swap only adjacent elements

  Examples: 

  Input : [0, 0, 1, 0, 1, 0, 1, 1]
  Output : 3
  1st swap : [0, 0, 1, 0, 0, 1, 1, 1]
  2nd swap : [0, 0, 0, 1, 0, 1, 1, 1]
  3rd swap : [0, 0, 0, 0, 1, 1, 1, 1]

  Input : Array = [0, 1, 0, 1, 0]
  Output : 3
  """
  i= 1
  count = 0
  while(i<len(nums)):
    if (nums[i] == 0 and nums[i-1] == 1):
      nums[i],nums[i-1] = nums[i-1],nums[i]
      i = i - 1
      count += 1
    else:
      i+=1
  print(count)

def merge3SortedArrays(a, b, c):
  """
  https://www.geeksforgeeks.org/problems/merge-k-sorted-arrays/1
  
  Given k sorted arrays arranged in the form of a matrix of size k * k. The task is to merge them into one sorted array. Return the merged sorted array ( as a pointer to the merged sorted arrays in cpp, as an ArrayList in java, and list in python).


  Examples :

  Input: k = 3, arr[][] = {{1,2,3},{4,5,6},{7,8,9}}
  Output: 1 2 3 4 5 6 7 8 9
  Explanation: Above test case has 3 sorted arrays of size 3, 3, 3 arr[][] = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]. The merged list will be [1, 2, 3, 4, 5, 6, 7, 8, 9].
  Input: k = 4, arr[][]={{1,2,3,4},{2,2,3,4},{5,5,6,6},{7,8,9,9}}
  Output: 1 2 2 2 3 3 4 4 5 5 6 6 7 8 9 9 
  Explanation: Above test case has 4 sorted arrays of size 4, 4, 4, 4 arr[][] = [[1, 2, 2, 2], [3, 3, 4, 4], [5, 5, 6, 6], [7, 8, 9, 9 ]]. The merged list will be [1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9].
  """
  i=j=k=p=0
  arr = [0] * (len(a) + len(b) + len(c))
  while i < len(a) and j < len(b) and k< len(c):
    if min(a[i],b[j],c[k]) == a[i]:
      arr[p] = a[i]
      i+=1
    elif min(a[i],b[j],c[k]) == b[j]:
      arr[p] = b[j]
      j+=1
    else:
      arr[p] = c[k]
      k+=1
    p+=1

  while i < len(a):
    arr[p] = a[i]
    i+=1
    p+=1
  while j < len(b):
    arr[p] = b[j]
    j+=1
    p+=1
  while k< len(c):
    arr[p] = c[k]
    k+=1
    p+=1

  print(arr)

def sortColors(nums) -> None:
  """
  https://leetcode.com/problems/sort-colors/
  
  Do not return anything, modify nums in-place instead.
  """
  low = mid = 0
  high = len(nums)-1

  while(mid<=high):
      if nums[mid] == 0:
          #Swap low and mid and increase low and mid
          nums[low], nums[mid] = nums[mid], nums[low]
          low+=1
          mid+=1
      elif nums[mid] == 1:
          #We have 1 in right place, so increase mid
          mid += 1
      else:
          #Swap mid and high and decrease high
          nums[mid], nums[high] = nums[high], nums[mid]
          high-=1

def nobleInteger(nums):
  """
  https://www.interviewbit.com/problems/noble-integer/
  https://leetcode.com/problems/majority-element/

  Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.

  Input:
   A = [3, 2, 1, 3]
  Output : 1

  Input:
   A = [1, 1, 3, 3]
  Output : -1
  """

  nums.sort()
  count = 0
  element = nums[0]

  for i in nums:
      if i == element:
          count += 1
      else:
          count -=1
      if count <= 0:
          element = i

  count = 0
  for i in nums:
      if i == element:
          count += 1
  return element if count >= len(nums)/2 else -1
    
def mergeSortedArrays_inplace(nums1: List[int], m: int, nums2: List[int], n: int) ->None:
  """
  https://leetcode.com/problems/merge-sorted-array/

  You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,     and two integers m and n, representing the number of elements in nums1 and nums2      respectively.

  Merge nums1 and nums2 into a single array sorted in non-decreasing order.

  Example 1:

  Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
  Output: [1,2,2,3,5,6]
  Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
  The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from     nums1.

  Solution:
  We need to fill nums1 with the merge. We have 0 at the end, so instead of checking from start, we can check from end and put the max(nums1[m-1],nums2[n-1]) in nums1[k]
  where k = m+n-1 (5)
  """
  k = m + n - 1
  while m>0 and n>0:
    if nums1[m-1] >= nums2[n-1]:
      nums1[k] = nums1[m-1]
      m-=1
    else:
      nums1[k] = nums2[n-1]
      n-=1
    k-=1

  #Fill nums1 with leftover nums2 elements
  while n>0:
    nums1[k] = nums2[n-1]
    n-=1
    k-=1
  print(nums1)

mergeSortedArrays_inplace(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)

