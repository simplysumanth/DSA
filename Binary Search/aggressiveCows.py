#aggressive cows problem
#https://takeuforward.org/plus/data-structures-and-algorithm/binary-search/faqs/aggressive-cows

#Using Binary Search
# We need to find the maximum value of the minimum distance between any 2 cows
def isPossible(nums,k,x):
    count = 1
    last = nums[0]
    for i in range(1,len(nums)):
        #calculate the distance btw lastCow and current stall
        #if the condition satisfies : inc counter and place the cow in that stall
        if nums[i] - last >= x:
            count += 1
            last = nums[i]
    if count >= k:
        return True
    
    print(f"count : {count}, x : {x}")
    return False

def binary():
    #Stalls with positions
    nums = [4, 2, 1, 3, 6]
    #No. of cows
    k = 2

    nums.sort()
    if len(nums)<k:
        return -1
    l = 1
    r = nums[-1] - nums[0]
    
    ans = -1
    while(l<=r):
        mid = l + (r-l)//2

        if isPossible(nums, k , mid) == True:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans


print(f"Ans : {binary()}")