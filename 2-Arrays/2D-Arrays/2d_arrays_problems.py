def sumTriangles(matrix, n):
  """
  https://www.geeksforgeeks.org/problems/sum-of-upper-and-lower-triangles-1587115621/1
  """
  #Upper triangle
  print("Upper Triangle")
  upper_sum = 0
  for i in range(n):
    for j in range(i, n):
      upper_sum += matrix[i][j]
      print(matrix[i][j], end=" ")
    print()

  print("Lower Triangle")
  #Lower Triangle
  lower_sum = 0
  for i in range(n):
    for j in range(i + 1):
      lower_sum += matrix[i][j]
      print(matrix[i][j], end=" ")
    print()
  return upper_sum, lower_sum


def snakePattern(matrix):
  """
  https://www.geeksforgeeks.org/problems/print-matrix-in-snake-pattern-1587115621/1
  """
  output = []
  n = len(matrix)
  for i in range(len(matrix)):
    if i % 2 == 0:
      for j in range(n):
        output.append(matrix[i][j])
    else:
      for j in range(n, -1, -1):
        output.append(matrix[i][j])

  return output


def transpose(matrix, n):
  for i in range(n):
    # print(matrix[i])
    for j in range(0, i):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

  for i in range(n):
    for j in range(n):
      print(matrix[i][j], end=" ")
    print()


def rotateby90(a, n):
  #Transpose
  for i in range(n):
    for j in range(i):
      a[i][j], a[j][i] = a[j][i], a[i][j]

  # print(f"Transpose")
  # for i in range(n):
  #   for j in range(n):
  #     print(a[i][j], end = " ")
  #   print()

  #Mirror

  for i in range(0, n // 2):
    for j in range(n):
      a[i][j], a[n - i - 1][j] = a[n - i - 1][j], a[i][j]


def multiply(A, B, C, n):

    n1, n2 = len(A), len(A[0])
    m1, m2 = len(B), len(B[0])

    if n2 != m1:
        return -1

    for i in range(n1):
        for j in range(n2):
            total = 0
            for k in range(m1):
                total += A[i][k] * B[k][j]
            C[i][j] = total

def spirallyTraverse(matrix):
  n = len(matrix)
  m = len(matrix[0])
  
  top = 0
  bottom = n-1
  left = 0
  right = m-1

  while(top<=bottom and left<=right):
    #left to right
    for i in range(left,right+1):
      print(matrix[top][i])
    top+=1

    #top to bottom
    for i in range(top,bottom+1):
      print(matrix[i][right])
    right-=1

    if top <= bottom:
    #right to left
      for i in range(right,left-1,-1):
        print(matrix[bottom][i])
      bottom -= 1

    #bottom to top
    if left<= right:
      for i in range(bottom,top-1,-1):
        print(matrix[i][left])
      left+=1

def interchangeRows(a):
  n = len(a)
  m = len(a[0])
  for i in range(n//2):
    for j in range(m):
      a[i][j], a[n-i-1][j] =  a[n-i-1][j], a[i][j]

  for i in range(n):
    for j in range(m):
      print(a[i][j], end = " ")
    print()

def interchangeColumns(a):
  n = len(a)
  m = len(a[0])

  for i in range(n):
    for j in range(m//2):
      a[i][j],a[i][m-j-1] = a[i][m-j-1],a[i][j]

  for i in range(n):
    for j in range(m):
      print(a[i][j], end = " ")
    print()
  
matrix = [[1, 2, 3, 4],
  [5, 6, 7, 8],
  [0, 0, 0, 0],
  [9, 10, 11, 12],
  [13, 14, 15,16]]
interchangeColumns(matrix)