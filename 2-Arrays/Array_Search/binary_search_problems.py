def searchInsert(nums, target):
    low, high = 0, len(nums)-1
    ans = len(nums)
    while(low<=high):
        mid = low + (high - low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
            ans = low
    return ans

print(searchInsert([1,2,3,4,6], 7))