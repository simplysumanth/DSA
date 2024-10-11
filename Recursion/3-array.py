def checkIfSorted(arr, start_index):
    """
    print(checkIfSorted(arr = [1,2,5,2], start_index = 0))
    """
    if start_index == len(arr)-1:
        return True
    return (arr[start_index] < arr[start_index+1]) and checkIfSorted(arr, start_index+1)

def searchEleInarray_index(arr, index, target):
    """
    print(searchEleInarray_index(arr = [3,4,1,2,6], index=0, target=6))
    """
    if index == len(arr):
        return -1
    
    if arr[index] == target:
        return index
    else:
        return searchEleInarray_index(arr, index+1,target)

def searchEleInarray_checkExists(arr, index, target) -> bool:
    """
    print(searchEleInarray_checkExists(arr=[1,5,3,2],index=0, target=4))
    """
    if index == len(arr):
        return False
    return (arr[index] == target) or searchEleInarray_checkExists(arr, index+1, target)

def searchEleInarray_index_fromLast(arr,index,target):
    """
    print(searchEleInarray_index_fromLast([1,2,3,4], 3, 2))
    """
    if index == -1:
        return -1
    if arr[index] == target:
        return index
    else:
        return searchEleInarray_index_fromLast(arr,index-1,target)

def findAllIndex(arr,index,target,ans):
    """
    print(findAllIndex([1,2,2,2,3,4,2,1,2], index=0, target=2, ans=[]))
    """
    if index == len(arr):
        return ans
    if arr[index] == target:
        ans.append(index)
    return findAllIndex(arr,index+1, target, ans)

def findAllIndex_withoutList(arr,index,target):
    """
    VERYYY IMPORTANT
    Without passing ans list in arguments, we are returning list of all occurances of target

    print(findAllIndex_withoutList([1,2,4,4,5,2,4], 0, 2))
    """
    ansList = []
    if index == len(arr):
        return ansList
    if arr[index] == target:
        ansList.append(index)
    ansFromBelow = findAllIndex_withoutList(arr,index+1, target)
    ansList.extend(ansFromBelow)
    return ansList

def search_in_rotated_sorted_array(arr,target, s, e):
    """
    print(search_in_rotated_sorted_array([6,7,8,1,2,3,4], 1, 0, 6))
    """
    if s > e:
        return -1

    m = s + (e-s)//2
    if arr[m] == target:
        return m

    # check if [s:m] is sorted
    if arr[s]<=arr[m]:
        #let's check if the target lies in this sorted range
        if arr[s] <= target <= arr[m]:
            #e = m-1
            return search_in_rotated_sorted_array(arr, target, s, m-1)
        else:
            #search in other part [m+1 : e] -> s = m+1
            return  search_in_rotated_sorted_array(arr, target, m+1, e)

    #If [s:m] isn't sorted, then the other half should be sorted
    if arr[m] <= target <= arr[e]:
        # s=m+1
        return  search_in_rotated_sorted_array(arr, target, m+1, e)

    #The only part left is [s:e] in case of [s:e] being unsorted
    else:
        #e = m-1
        return  search_in_rotated_sorted_array(arr, target, s , m-1)

