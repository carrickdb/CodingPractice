def isToeplitz(arr):
  if len(arr) < 1:
    return True
  n = len(arr)
  m = len(arr[0])
  for j in range(m):
    targetNum = arr[0][j]
    for i in range(1, n):
      col = j+i
      if col >= m:
        break
      if arr[i][col] != targetNum:
        return False
  for i in range(1,n):
    targetNum = arr[i][0]
    for j in range(1,m):
      row = i+j
      if row >= n:
        break
      if arr[row][j] != targetNum:
        return False
  return True
