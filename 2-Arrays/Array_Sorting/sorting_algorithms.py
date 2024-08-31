def selectionSort(a):
  #select the smallest element and swap with i
  for i in range(len(a)-1):
    min_idx = i
    for j in range(i+1,len(a)):
      #check if a[j] < a[min_idx] (getting the min of [i+1:])
      if a[j] < a[min_idx]:
        min_idx = j
    a[i],a[min_idx] = a[min_idx],a[i]
  print(a)

def bubbleSort(a):
  """
  In Bubble Sort algorithm, 

  traverse from left and compare adjacent elements and the higher one is placed at       right side. 
  In this way, the largest element is moved to the rightmost end at first. 
  This process is then continued to find the second largest and place it and so on       until the data is sorted.
  """
  n = len(a)
  for i in range(n):
    swapped = False
    for j in range(0,n-i-1):
      if a[j] > a[j+1]:
        a[j],a[j+1] = a[j+1],a[j]
        swapped = True
    if not swapped:
      break
  print(a)

def insertionSort(a):
  """
  take a element and compare it with all elements to it's left and swap if the element is smaller

  Time Complexity of Insertion Sort:
  Best case: O(n) , If the list is already sorted, where n is the number of elements in the list.
  Average case: O(n^2 ) , If the list is randomly ordered
  Worst case: O(n^2 ) , If the list is in reverse order
  
  Space Complexity of Insertion Sort:
  Auxiliary Space: O(1), Insertion sort requires O(1) additional space, making it a space-efficient sorting algorithm.

  """
  n = len(a)
  for i in range(n):
    j = i
    while(j>0 and a[j]<a[j-1]):
      a[j],a[j-1] = a[j-1],a[j]
      j-=1
  print(a)

def mergeSort(a):
  if len(a) <= 1:
    return
  mid = len(a)//2
  left = a[:mid]
  right = a[mid:]

  mergeSort(left)
  mergeSort(right)
  mergeSortedArrays(a,left,right)
  

def mergeSortedArrays(a,left,right):
  i=j=k=0
  while i<len(left) and j<len(right):
    if left[i] <= right[j]:
      a[k] = left[i]
      i+=1
    else:
      a[k] = right[j]
      j+=1
    #Increase k
    k+=1
  while i < len(left):
    a[k] = left[i]
    k+=1
    i+=1
  while j < len(right):
    a[k] = right[j]
    k+=1
    j+=1
      

nums = [4, 5, 2, 1, 9]
print(f"Main list : {nums}")
mergeSort(nums)
print(f"sorted : {nums}")
