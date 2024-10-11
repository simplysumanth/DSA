def inverted_triangle_iter(n):
    """
    For n = 4 , print
    *   *   *   *
    *   *   *
    *   *
    *
    """
    
    for i in range(n,0,-1):
        for j in range(n):
            if j<i:
                print("*",end=" ")
        print()
        
def inverted_triangle_recurssion(r,c):
    #Base condition
    if r == 0:
        return
    if c < r:
        inverted_triangle_recurssion(r, c+1)
        print("*", end=" ")
        
    elif c == r:
        inverted_triangle_recurssion(r-1, 0)
        print()
        # r -= 1
        # c = 0     
    
def triangle_recurssion(r, c):
    """
    *
    *   *
    *   *   *
    *   *   *   *
    """
    if r == 0:
        return
    if c < r:
        triangle_recurssion(r,c+1)
        print("*", end=" ")
    elif c == r:
        triangle_recurssion(r-1,0)
        print()

def bubble_sort(arr, r,c ):
    """
    4,3,2,1
    Compare each element and push biggest to the end
    3,2,1,4
    2,1,3,4
    1,2,3,4
    """
    if r == 0:
        return arr
    if c == r:
        return bubble_sort(arr, r-1, 0)
    else:
        if arr[c] > arr[c+1]:
            arr[c], arr[c+1] = arr[c+1], arr[c]
            return bubble_sort(arr,r,c+1)

def selection_sort(arr,r,c, bigger):
    """
    Get the maximum of arr and put it in the end, then reduce array window to [0:len(a)-1]

    Search through 0 to r: when r == c: swap (bigger, r); r = r-1

    a = [4,3,2,1]
    selection_sort(a, 3, 0, 0)
    print(a)
    """
    if r == 0:
        return
    if c <= r:
        if arr[c] > arr[bigger]:
            bigger = c
        selection_sort(arr,r,c+1, bigger)
    else:
        arr[bigger], arr[r] = arr[r], arr[bigger]
        selection_sort(arr, r - 1, 0, 0)


    