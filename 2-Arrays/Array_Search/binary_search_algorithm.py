from typing import List


def binarySearch(a: List, k: int) -> int:
  # Array should be sorted -> [1,3,4,6,7,9] k = 7
  s = 0
  e = len(a) - 1

  while (s <= e):
    m = s + (e - s) // 2  #a[m] = 4
    if a[m] == k:
      return m
    elif a[m] < k:
      s = m + 1
    else:
      e = m - 1

  return -1


def binarySearchRecurssive(a, s, e, k) -> int:
  if s <= e:
    m = s + (e - s) // 2  #a[m] = 4
    if a[m] == k:
      return m
    elif a[m] < k:
      return binarySearchRecurssive(a, m + 1, e, k)
    else:
      return binarySearchRecurssive(a, s, m - 1, k)
  else:
    return -1


print(binarySearchRecurssive([1, 3, 4, 6, 7, 9], 0, 5, 7))
