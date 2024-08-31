def longestConsecutive_better(nums):
  """
  Space Complexity : O(NlogN)
  """
  #Sort the array
  nums.sort()
  #init variables
  count = 0
  longest = 0
  lastSmallest = float("-inf")

  #loop thru array
  for i in range(len(nums)):
    if nums[i]-1 == lastSmallest:
      #We have a sequence
      count += 1
      lastSmallest = nums[i]
    elif nums[i] != lastSmallest:
      #new sequence
      count = 1
      lastSmallest = nums[i]
    longest = max(longest,count)
  return longest

def longestConsecutive_optimal(nums):
  """
  Space complexity : O(N)
  Using set
  """
  hashSet = set(nums)
  longest = 0
  #Check if the nums[i]-1 exists in hashSet
  for i in hashSet:
    if i-1 not in hashSet:
      length = 0
      while i+length in hashSet:
        length+=1
      longest = max(longest,length)
  return longest
    
  
print(longestConsecutive_optimal([100, 4, 200, 1, 3, 2]))