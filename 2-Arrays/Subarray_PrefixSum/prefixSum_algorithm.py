from typing import List


class PrefixSum1D:

  def __init__(self, arr: List):
    self.prefix = []
    total = 0
    for i in arr:
      total += i
      self.prefix.append(total)

  def rangeSum(self, left, right):
    #Find the sum of the subarray arr[left:right]
    print(f"Prefix Total : {self.prefix}")
    preRight = self.prefix[right]
    preLeft = self.prefix[left - 1] if left > 0 else 0
    return preRight - preLeft

class PrefixSum2D:

  def __init__(self, arr: List):
    """
       0 1 2
    0  1 2 3
    1  4 5 6
    2  7 8 9

    prefix(1,1) -> prefix([0,0] -> [0,1]) + prefix([1,0] -> [1,1])
                              above       +        Currentprefix
    But when row = 0 or col = 0, if we check above/left it will throw out of bounds
    So, add zero padding -> row,col = row+1,col+1
      
    """
    ROWS, COLS = len(arr),len(arr[0])
    #Zero Padded Array
    self.matrix = [[0] * (COLS+1) for r in range(ROWS+1)]
    for i in range(ROWS):
      currentPrefix = 0
      for j in range(COLS):
        currentPrefix += arr[i][j]
        above =self.matrix[i][j+1]
        self.matrix[i+1][j+1] = currentPrefix + above
  
  def rangeSum(self, row1, col1, row2, col2):
    """
       0 1 2 3
    0  0 0 0 0 
    1  0 1 3 6 
    2  0 5 12 21 
    3  0 12 27 45 

    Now we have this matrix with preSum computed.
    To get the rangeSum([1,1], [2,2]) -> 1 3
                                         5 12
    1.[2,2] contains the prefixSum of [0,0] -> [2,2] :
      * To get for [1,1] -> [2,2]:
            ([0,0] -> [2,2]) - ([0,0] -> [0,2]) - ([0,0] -> [2,0]) + ([0,0])
               bottomLeft    -     Above        -      left        + topLeft
    """
    #We have zero padding, so let's icrement the row,col by 1
    row1, col1, row2, col2 = row1 + 1, col1+1, row2+1, col2+1
    bottomLeft = self.matrix[row2][col2]
    above = self.matrix[row1-1][col2]
    left = self.matrix[row2][col1-1]
    topLeft = self.matrix[row1-1][col1-1]
    return bottomLeft - above - left + topLeft
    

p = PrefixSum2D([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
