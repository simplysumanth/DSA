#https://takeuforward.org/plus/data-structures-and-algorithm/binary-search/faqs/kth-element-of-2-sorted-arrays
#Kth element of 2 sorted arrays

def kthElement(a, b, k):
    """
    Given two sorted arrays a and b of size m and n respectively. Find the kth element of the final sorted array.

    Example 1
    Input: a = [2, 3, 6, 7, 9], 
           b = [1, 4, 8, 10], k = 5

    Output: 6

    Explanation: The final sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.
    """

    c = [0] * (len(a) + len(b))
    
    l = 0
    r = min(len(a)-1, len(b))





a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5

kthElement(a,b,k)

s = ["h", "e" ,"l" ,"l" ,"o"]
print(s[::-1])