def getStudents(arr,x):
    count = 1
    curr = 0
    for i in arr:
        if curr+i <= x:
            curr += i
        else:
            count+=1
            curr= i
    
    return count

def linear():
    n = 4
    arr = [12, 34, 67, 90]
    m = 2

    if m>n:
        print(-1)

    l = max(arr)
    r = sum(arr)

    for i in range(l,r+1):
        if getStudents(arr,i) == m:
            return i


def binary():
    n = 4
    arr = [12, 34, 67, 90]
    m = 2

    if m>n:
        print(-1)

    l = max(arr)
    r = sum(arr)
    ans = -1
    while(l <= r):
        mid = l + (r-l)//2
        
        if getStudents(arr,mid) <= m:
            r = mid - 1
        elif getStudents(arr,mid) > m:
            l = mid + 1
            
    return l

print(binary())