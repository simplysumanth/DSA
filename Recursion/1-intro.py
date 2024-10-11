def fibo(n):
    #n-1 + n-2
    if (n<2):
        return n
    return fibo(n-1) + fibo(n-2)


def binarySearch(a,target, s, e):
    """
    Inputs:
    a = [12,14,15,23,25,35,56]
    target = 35
    print(binarySearch(a,target,0,len(a)-1))
    """

    if (s>e):
        return -1
    m = s + (e-s)//2

    if a[m] == target:
        return m
    elif a[m] < target:
       return binarySearch(a,target,m+1,e)
    else:
       return binarySearch(a,target,s,m-1)


